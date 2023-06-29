import requests
import json
import pkg_resources
import numpy as np
from bs4 import BeautifulSoup
from typing import Union, Optional

class Corona:
    def __init__(self):
        self.countries = json.dumps(json.loads(open(pkg_resources.resource_filename("coroapi", "countries.json")).read()), indent=4, sort_keys=True)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        self.country, self.rank = None, None # temporary variables used by country_by_rank and rank_by_country

    def country_stats(self, country: str, infected: Optional[bool] = True, deaths: Optional[bool] = True, recovered: Optional[bool] = True, country_rank: Optional[bool] = True, text: Optional[bool] = True) -> Union[bool, list, dict]:
        resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=self.headers)
        if resp.status_code == 200:
            body = BeautifulSoup(resp.content, 'html.parser').find('tbody').find('tr', {'onclick': f"window.location='coronavirus/{country}';"}).findAll('td')
            infected_data, deaths_data, recovered_data = body[1].text, body[2].text, body[3].text
            country_rank_data = ''.join(self.rank_by_country(country, text=False))

            if not text:
                return np.array([infected_data, deaths_data, recovered_data.strip(), country_rank_data])[[infected, deaths, recovered, country_rank]].tolist()
            d = {'Infected': infected_data, 'Deaths': deaths_data, 'Recovered': recovered_data.strip(), 'Rank': country_rank_data}
            return dict(np.array(list(d.items()))[[infected, deaths, recovered, country_rank]])
        return False

    def global_stats(self, text: Optional[bool] = True, infected: Optional[bool] = True, deaths: Optional[bool] = True, recovered: Optional[bool] = True, rank_country: Optional[bool] = True) -> Union[bool, list, dict]:
        resp = requests.get('https://epidemic-stats.com/coronavirus/', headers=self.headers)
        if resp.status_code == 200:
            body = BeautifulSoup(resp.content, 'html.parser').find('div', class_='row')
            infected_data = body.find('div').find('div', class_='card-body').find('span', class_='h5 card-title').text
            deaths_data = body.find('div', class_='card text-white col-md-3 ml-auto mr-auto mb-2').find('div').find('span', class_='h5 card-title').text.split()[0]
            recovered_data = body.findAll('div', class_='card text-center text-white col-md-3 ml-auto mr-auto mb-2')[1].find('div').find('span', class_='h5 card-title').text.split()[0]
            rank_country_data = ''.join(self.country_by_rank('1', text=False))

            if not text:
                return np.array([infected_data, deaths_data, recovered_data.strip(), rank_country_data])[[infected, deaths, recovered, rank_country]].tolist()
            d = {'Infected': infected_data, 'Deaths': deaths_data, 'Recovered': recovered_data, 'Highest Cases': rank_country_data}
            return dict(np.array(list(d.items()))[[infected, deaths, recovered, rank_country]])
        return False

    def rank_by_country(self, country: str, text: Optional[bool] = True) -> Union[bool, list, dict]:
        resp = requests.get('https://virusncov.com/', headers=self.headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')

            for country_ in soup.find('tbody').findAll('tr'):
                if country_.find('a', href=True)['href'] == f'/covid-statistics/{country}':
                    rank = country_.find('td').text

            return [rank] if not text else {'Rank': rank}
        return False

    def country_by_rank(self, rank: str, text: Optional[bool] = True) -> Union[bool, list, dict]:
        resp = requests.get('https://virusncov.com/', headers=self.headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')

            for country_ in soup.find('tbody').findAll('tr'):
                if country_.find('td').text == rank:
                    self.country = country_.find('a', href=True)['href'].split('/')[2]

            return [self.country] if not text else {'Country': self.country}
        return False # return False if status code != OK (200)
    
    def is_country_valid(self, country: str) -> bool:
        return True if country in self.countries else False