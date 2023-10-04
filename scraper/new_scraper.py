from parsel import Selector
import requests


class NewScraper:
    URL = "https://ru.sputnik.kg"
    LINK_XPATH = '//div[@class="cell-list__list"]/a/@href'

    def parse_data(self):
        html = requests.get(url=self.URL).text
        tree = Selector(text=html)
        links = tree.xpath(self.LINK_XPATH).extract()
        # for link in links:
        #     print(self.URL + link)
        return links[0:5]


if __name__ == "__main__":
    scraper = NewScraper()
    scraper.parse_data()