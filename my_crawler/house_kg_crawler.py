import requests
from parsel import Selector
from pprint import pprint


class HouseParser:
    MAIN_URL = 'https://www.house.kg/snyat-kvartiru'
    BASE_URL = 'https://www.house.kg/'

    def get_page(self):
        response = requests.get(HouseParser.MAIN_URL)
        print(response.status_code)
        self.page = response.text

    def get_page_title(self):
        html = Selector(text=self.page)
        title = html.css('title::text').get()
        print(title)

    def get_house_links(self):
        selector = Selector(text=self.page)
        links = selector.css('div.listings-wrapper div.listing div.left-image a::attr(href)').getall()
        pprint(links)
        links = list(map(lambda l: f"{HouseParser.BASE_URL}{l}", links))
        return links[:3]


if __name__ == '__main__':
    parser = HouseParser()
    parser.get_page()
    parser.get_page_title()
    links = parser.get_house_links()
    pprint(links)
