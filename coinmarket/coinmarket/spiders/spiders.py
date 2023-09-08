import scrapy
from pathlib import Path
import time

class CoinMarketSpider(scrapy.Spider):
    '''
        This spider will crawl the coinmarketcap.com website and extract the
    '''
    name = "coinmarket"
    start_urls = [
        "https://coinmarketcap.com/?page=1",
    ]


    def parse(self, response):
        '''
            This function will parse the response and extract the data.
        '''
        data_count = 0
        for coin in response.css("tr"):
            if data_count == 10:
                time.sleep(5)
                coin_name = coin.css("p.sc-4984dd93-0::text").getall()
                coin_price = coin.css("div.sc-a0353bbc-0 a.cmc-link span::text").getall()

                data = {
                    "coin_name": coin_name,
                    "coin_price": coin_price,
                }
                data_count += 1
                print(data, data_count)
            else:
                coin_name = coin.css("p.sc-4984dd93-0::text").getall()
                coin_price = coin.css("div.sc-a0353bbc-0 a.cmc-link span::text").getall()

                data = {
                    "coin_name": coin_name,
                    "coin_price": coin_price,
                }
                data_count += 1
                print(data, data_count)


            # page = response.url.split("=")[-1]
            # if page is not None:
            #     filename = f"page-{page}.txt"
            #     with open(filename, 'a') as f:
            #         f.write(f"{data}\n")

        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
        
class CryptoSpider(scrapy.Spider):
    '''
        get crypto data from crypto.com
    '''
    name = "crypto"
    start_urls = [
        "https://crypto.com/price/?page=1",
    ]

    def parse(self, response):
        '''
            This function will parse the response and extract the data.
        '''
        page = int(response.url.split("=")[-1])
        print(page)
        for coin in response.css("tr"):
            coin_name = coin.css("p.chakra-text.css-rkws3::text").getall()
            coin_price = coin.css("p.chakra-text.css-13hqrwd::text").getall()

            data = {
                "coin_name": coin_name,
                "coin_price": coin_price,
            }
            print(data)

        next_button = response.css("button.css-1gov58q svg path::attr(fill)").get()
        if next_button is not None and page < 3:
            next_url = '/price/?page=' + str(page + 1)
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)


            
           
