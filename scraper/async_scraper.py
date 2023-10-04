import httpx
import asyncio
from parsel import Selector


class AsyncScraper:
    TARGET_URL = 'https://www.ts.kg/selection/top_2022_multy_dlya_vzroslykh'
    LINK_XPATH = '//div[@class="row selection-show"]/a[1]/@href'
    PLUS_LINK = 'https://www.ts.kg'
    YEAR_XPATH = '//div[@class="app-show-header-years"]/text()'
    NAME_XPATH = '//div[@class="app-show-header"]/div[1]/text()'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
    }

    async def parse_data(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            return await self.get_url(client, url=self.TARGET_URL)

    # async def parse_data(self):
    #     async with httpx.AsyncClient(headers=self.HEADERS) as client:
    #         for page in self.async_generate():
    #             await self.get_url(client, url=self.TARGET_URL.format(page))

    async def get_url(self, client, url):
        response = await client.get(url)
        return await self.scrape_links(content=response.text, client=client)

    async def scrape_links(self, content, client):
        tree = Selector(text=content)
        links = tree.xpath(self.LINK_XPATH).extract()
        return reversed(links[10:16])

    # async def detail_scrape(self, client, link):
    #     response = await client.get(link)
    #     tree = Selector(text=response.text)
    #     name = tree.xpath(self.NAME_XPATH).extract_first()
    #     # print(response.url)
    #     print(name)

    # async def async_generate(self):
    #     for page in range(1,3):
    #         yield page

    # async def async_generate_details(self, links):
    #     for link in links:
    #         yield link


if __name__ == "__main__":
    scraper = AsyncScraper()
    asyncio.run(scraper.parse_data())
