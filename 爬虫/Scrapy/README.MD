scrapy：
    1、主要爬虫部分是在mySpider/mySpider/spiders/tencentposition.py文件里面
    2、用yield自动调用pipelines文件，将爬取的内容写道文件中，是在pipelines.py中
    3、报头、pipelines等配置在settings中