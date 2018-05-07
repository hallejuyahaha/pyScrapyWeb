# -*- coding: utf-8 -*-
import scrapy
from SpiderWeb.items import CnblogsItem
from SpiderWeb.items import CnblogsItemLoader

from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader




class JobboleSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['news.cnblogs.com']
    start_urls = ['https://news.cnblogs.com/']

    def parse(self, response):
        # 解析列表页中的所有文章url并交给scrapy下载后并进行解析
        post_nodes = response.css(".news_entry a")
        for post_node in post_nodes:
            # image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        next_url = response.xpath("//div[@class='pager']/a[last()]/@href").extract_first("")
        if next_url:
            uurl = parse.urljoin(response.url, next_url)
            yield Request(url=uurl, callback=self.parse)

        pass

    def parse_detail(self, response):
        # article_item = CnblogsItem()
        # # 通过item loader加载item
        # front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        item_loader = CnblogsItemLoader(item=CnblogsItem(), response=response)
        item_loader.add_css("title", "#news_title a::text")
        item_loader.add_value("url", response.url)
        # item_loader.add_value("url_object_id", get_md5(response.url))

        item_loader.add_css("content", "#news_body p::text")
        # item_loader.add_value("favorite", [front_image_url])
        item_loader.add_css("favorite", ".diggnum ::text")
        item_loader.add_css("comment", "#News_CommentCount_Head::text")
        item_loader.add_css("watch", "#News_TotalView::text")
        item_loader.add_css("author", ".news_poster a::text")

        article_item = item_loader.load_item()
        yield article_item
        pass