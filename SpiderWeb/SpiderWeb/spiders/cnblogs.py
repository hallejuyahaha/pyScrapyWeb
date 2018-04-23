# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

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
            yield Request(url=self.parse.urljoin(response.url, post_url), callback=self.parse_detail)
            pass
        # 提取下一页并交给scrapy进行下载
        next_url = response.css("").extract_first("")
        if next_url:
            yield Request(url=self.parse.urljoin(response.url, next_url), callback=self.parse)

        pass

    def parse_detail(self, response):
        # article_item = JobBoleArticleItem()
        # # 通过item loader加载item
        # front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        # item_loader = ArticleItemLoader(item=JobBoleArticleItem(), response=response)
        # item_loader.add_css("title", ".entry-header h1::text")
        # item_loader.add_value("url", response.url)
        # item_loader.add_value("url_object_id", get_md5(response.url))
        # item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        # item_loader.add_value("front_image_url", [front_image_url])
        # item_loader.add_css("praise_nums", ".vote-post-up h10::text")
        # item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
        # item_loader.add_css("fav_nums", ".bookmark-btn::text")
        # item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
        # item_loader.add_css("content", "div.entry")
        #
        # article_item = item_loader.load_item()
        #
        # yield article_item
        pass