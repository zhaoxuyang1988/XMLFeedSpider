# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem


class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/1615888477.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, node):
        i = MyxmlItem()
        # 利用xpath表达式将对应信息提取出来，并存储到对应的ITEM中
        i['title'] = node.xpath("title/text()").extract()
        i['link'] = node.xpath("link/text()").extract()
        i['author'] = node.xpath("author/text()").extract()
        return i
