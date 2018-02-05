# coding:utf-8
import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 做记录 当前我们爬取的是第几个url
        count = 1
        # 这个是加入单个url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 这个是批量加入 加入一个集合
                self.urls.add_new_urls(new_urls)
                # 数据的收集
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except :
                print("craw failed")
        # 输出收集的数据
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
