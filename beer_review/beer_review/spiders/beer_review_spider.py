from beer_review.items import BeerReviewItem
import scrapy

class BeerReviewSpider(scrapy.Spider):
    name = 'beer_review_spider'
    allowed_urls = ['https://www.beeradvocate.com/']
    start_urls = ['https://www.beeradvocate.com/lists/top/']

    def parse(self, response):
        url_list = response.xpath('//tr/td/a/@href').extract()
        pageurl = ['https://www.beeradvocate.com' + l for l in url_list]
        
        raw_list = response.xpath('//td[@class="hr_bottom_light"]/b/text()').extract()
        new_list = raw_list[1::2]
        list1 = list(map(lambda x: x.replace(',',''), new_list))

        for x in range(250):
            
            endindex = int(list1[x])/25
            review_urls = [pageurl[x]+ '?view=beer&sort=&start=' + str(25*i) for i in range(int(endindex) + 1)]
            for url_ in review_urls:
                yield scrapy.Request(url_, callback=self.parse_beer)

    




    def parse_beer(self, response):

        name = response.xpath('//div[@class="titleBar"]/h1/text()').extract_first()
        rating = response.xpath('//span[@class="ba-ravg"]/text()').extract_first()
        brewery = response.xpath('//div[@id="info_box"]/a/b/text()').extract()[0]
        beer_type = response.xpath('//div[@id="info_box"]/a/b/text()').extract()[1]
        abv = response.xpath('//div[@id="info_box"]/text()').extract()[13]
        rank = response.xpath('//div[@id="item_stats"]/dl/dd/text()').extract()[0]
        location1 = response.xpath('//div[@id="info_box"]/a/text()').extract()[0]
        location2 = response.xpath('//div[@id="info_box"]/a/text()').extract()[1]

        rows = response.xpath('//div[@id="rating_fullview_content_2"]')

        for i in range(len(rows)):
            #review data
            rdev = rows[i].xpath('.//span/text()').extract()[2]
            score = rows[i].xpath('.//span/text()').extract()[0]
            score_list = rows[i].xpath('.//span/text()').extract()[3].split(' | ')
            look = score_list[0]
            smell = score_list[1]
            taste = score_list[2]
            feel = score_list[3]
            overall = score_list[4]
            content = ''.join(rows[i].xpath('./text()').extract()).strip()
            author = rows[i].xpath('.//span[@class="muted"]/a/text()').extract()[0]
            date = rows[i].xpath('.//span[@class="muted"]/a/text()').extract()[1]
            #review urls
            #url_beer = 'https://www.beeradvocate.com' + rows[i].xpath('.//h6/a/@href').extract_first()
            #url_brewery = 'https://www.beeradvocate.com' + rows[i].xpath('.//a/@href').extract()[2]
            #url_beer_type = 'https://www.beeradvocate.com' + rows[i].xpath('.//a/@href').extract()[3]
            url_author = 'https://www.beeradvocate.com' + rows[i].xpath('.//a/@href').extract()[0]

            item = BeerReviewItem()
            item['name'] = name
            item['brewery'] = brewery
            item['beer_type'] = beer_type
            item['abv'] = abv
            item['rating'] = rating
            item['rank'] = rank
            item['location1'] = location1
            item['location2'] = location2
            item['rdev'] = rdev
            item['score'] = score
            item['look'] = look
            item['smell'] = smell
            item['taste'] = taste
            item['feel'] = feel
            item['overall'] = overall
            item['content'] = content
            item['author'] = author
            item['date'] = date
            #item['url_beer'] = url_beer
            #item['url_brewery'] = url_brewery
            #item['url_beer_type'] = url_beer_type
            item['url_author'] = url_author

            yield item

