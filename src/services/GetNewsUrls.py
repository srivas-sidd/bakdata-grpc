from pygooglenews import GoogleNews
from pprint import pprint
import logging

class GetUrls():

    def __init__(self):
        self.gn = GoogleNews()

    async def get_urls(self):
        query_terms = ("Pre-Seed funding Seed funding Venture funding Series A funding Series B funding \
                       Series C funding Series D funding Series E funding Series F funding \
                       Series G funding Series H funding Series I funding Series J funding Angel funding \
                       Private Equity funding Debt financing Equity Crowdfunding Post-IPO Equity \
                       Convertible Note funding Post-IPO Debt Funding round")
        try:
            self.search = self.gn.search(query_terms, when='1d')
        except Exception as e:
            logging.info("Exception searching for data ", e)

        self.urls = [res['link'] for res in self.search['entries'] if 'link' in res]

        logging.info(self.urls)
        return self.urls

if __name__ == '__main__':
    news = GetUrls()
    news.get_urls()