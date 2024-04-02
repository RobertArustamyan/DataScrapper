import json
import random
import concurrent.futures
import requests
from fake_useragent import UserAgent
import csv
import urllib3
urllib3.disable_warnings()

DRAM_TO_USD = 400
proxies = [
    'https://nTaBjw:oHWnkr@217.29.53.64:10776',
    'https://nTaBjw:oHWnkr@217.29.53.64:10775',
    'https://nTaBjw:oHWnkr@217.29.53.70:10801',
    'https://nTaBjw:oHWnkr@217.29.53.70:10800',
    'https://nTaBjw:oHWnkr@217.29.53.70:10799',

]
class GettingData():
    cookies = {
        '_gcl_au': '1.1.1578380407.1708608289',
        '_ym_uid': '1708608289339730971',
        '_ym_d': '1708608289',
        '_fbp': 'fb.1.1708608290017.2116922163',
        '_gac_UA-215674752-1': '1.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE',
        '_gcl_aw': 'GCL.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE',
        '_gid': 'GA1.2.1815942576.1711469028',
        '_ym_isad': '2',
        '_clck': '12tethq%7C2%7Cfkg%7C0%7C1513',
        '_ym_visorc': 'w',
        '_ga': 'GA1.2.710196867.1708608290',
        '_clsk': '10vgwrb%7C1711631168390%7C9%7C1%7Cn.clarity.ms%2Fcollect',
        'XSRF-TOKEN': 'eyJpdiI6IkdjMFNMejNETitQSDJ4eFJSN2lqQ1E9PSIsInZhbHVlIjoiZXlzeXI3VjY3NnkxdFp4V1YzT0JqbFpuZnBQNE5FU0ZiV25sWUJMaDI2MU5zYjNhTXE5Ky9kRWIycGd5b1hCU2hTd2hobmRaSG1FbGxyRDB1amYxN1ZjR0RBWVJmbHBTcW93bFFIUlc5VUZKNXFJdU1tZmU3T0ZzTDFxc0lkcHEiLCJtYWMiOiIxZGQ3MmQ0NGVlMWQ4ZmFmMmJlYWE5YTU2ZjM1NTYxNzZjZjBkOWVjMjc0ODRmYWY4NGIwMDdkMjhlYjBkNGYzIiwidGFnIjoiIn0%3D',
        'banali_session': 'eyJpdiI6ImMxUUdlYkRBZUsyNnkwbzFEamM3d1E9PSIsInZhbHVlIjoiZlh6WklEa3RIaGhoMjMvdVBDSHlQM0o3dndkNTJVd1VaOWJtb09SOWRFdHNTZzBsNjc4VnhMaUJuQ2U0aFFZay9rWW9oZ1BSL3Z1MHJZcE1LdVNrSzRDbjI5K0FqK1VTb2JSYjEzbElDNW5SSko4VEw2NFNEczUxSmJkVXhxMGciLCJtYWMiOiIwODJkYTVjNjEyNDZkMTk4NWI3MGIzMmJkYTk3NzQ4ZGRhM2ExM2QwMjBhNWJhZGZjNDRlNWM0NzdkNWRlYzViIiwidGFnIjoiIn0%3D',
        '_ga_5LHZPJK3WL': 'GS1.1.1711629741.7.1.1711631185.43.0.0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'hy',
        # 'cookie': '_gcl_au=1.1.1578380407.1708608289; _ym_uid=1708608289339730971; _ym_d=1708608289; _fbp=fb.1.1708608290017.2116922163; _gac_UA-215674752-1=1.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE; _gcl_aw=GCL.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE; _gid=GA1.2.1815942576.1711469028; _ym_isad=2; _clck=12tethq%7C2%7Cfkg%7C0%7C1513; _ym_visorc=w; _ga=GA1.2.710196867.1708608290; _clsk=10vgwrb%7C1711631168390%7C9%7C1%7Cn.clarity.ms%2Fcollect; XSRF-TOKEN=eyJpdiI6IkdjMFNMejNETitQSDJ4eFJSN2lqQ1E9PSIsInZhbHVlIjoiZXlzeXI3VjY3NnkxdFp4V1YzT0JqbFpuZnBQNE5FU0ZiV25sWUJMaDI2MU5zYjNhTXE5Ky9kRWIycGd5b1hCU2hTd2hobmRaSG1FbGxyRDB1amYxN1ZjR0RBWVJmbHBTcW93bFFIUlc5VUZKNXFJdU1tZmU3T0ZzTDFxc0lkcHEiLCJtYWMiOiIxZGQ3MmQ0NGVlMWQ4ZmFmMmJlYWE5YTU2ZjM1NTYxNzZjZjBkOWVjMjc0ODRmYWY4NGIwMDdkMjhlYjBkNGYzIiwidGFnIjoiIn0%3D; banali_session=eyJpdiI6ImMxUUdlYkRBZUsyNnkwbzFEamM3d1E9PSIsInZhbHVlIjoiZlh6WklEa3RIaGhoMjMvdVBDSHlQM0o3dndkNTJVd1VaOWJtb09SOWRFdHNTZzBsNjc4VnhMaUJuQ2U0aFFZay9rWW9oZ1BSL3Z1MHJZcE1LdVNrSzRDbjI5K0FqK1VTb2JSYjEzbElDNW5SSko4VEw2NFNEczUxSmJkVXhxMGciLCJtYWMiOiIwODJkYTVjNjEyNDZkMTk4NWI3MGIzMmJkYTk3NzQ4ZGRhM2ExM2QwMjBhNWJhZGZjNDRlNWM0NzdkNWRlYzViIiwidGFnIjoiIn0%3D; _ga_5LHZPJK3WL=GS1.1.1711629741.7.1.1711631185.43.0.0',
        'referer': 'https://banali.am/hy/vardzakalutyun/bnakaran/3-senyakanoc/Erevan/Kentron/Zaqiyan-poxoc-B12414',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-csrf-token': 'OuumFZsU141IWNS5y5NQ4aZWnU4I3HIcqM8rijHg',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6IkdjMFNMejNETitQSDJ4eFJSN2lqQ1E9PSIsInZhbHVlIjoiZXlzeXI3VjY3NnkxdFp4V1YzT0JqbFpuZnBQNE5FU0ZiV25sWUJMaDI2MU5zYjNhTXE5Ky9kRWIycGd5b1hCU2hTd2hobmRaSG1FbGxyRDB1amYxN1ZjR0RBWVJmbHBTcW93bFFIUlc5VUZKNXFJdU1tZmU3T0ZzTDFxc0lkcHEiLCJtYWMiOiIxZGQ3MmQ0NGVlMWQ4ZmFmMmJlYWE5YTU2ZjM1NTYxNzZjZjBkOWVjMjc0ODRmYWY4NGIwMDdkMjhlYjBkNGYzIiwidGFnIjoiIn0=',
    }

    def __init__(self):
        self.ua = UserAgent()
        self.data = []

    def _get_response(self, url: str) -> str or None:
        '''
        Gets a URL and returns the response text if the status code is 200.
        :param url: The URL from the Data folder.
        :return: The response text.
        '''
        self.headers['User-Agent'] = self.ua.random

        # Removing "https://banali.am/hy/" from the URL
        shorted_url = url.replace("https://banali.am/hy/", "")
        proxy = random.choice(proxies)
        # Making a GET request to the constructed URL
        response = requests.get(
            f'https://banali.am/api/post/slug/{shorted_url}',
            cookies=self.cookies,
            headers=self.headers,
            verify=False,
            proxies={'http': proxy}
        )

        # Returning the response text if the status code is 200, otherwise None
        return response.text if response.status_code == 200 else None

    def _making_json(self, text: str) -> dict or None:
        '''
        Transforms the response text into a JSON type object.
        :param text: The result from the _get_response function.
        :return: The JSON type object.
        '''
        if text:
            return json.loads(text)
        return None

    def _getting_url_data(self, url: str) -> None:
        '''
        Gets all information out of link (category, price, area, floor and etc)
        :param url: the link of the house
        :return: appends the data in self.data
        '''
        pure_data = self._making_json(self._get_response(url))

        if not pure_data:
            return None

        parsed_data = {}

        try:
            parsed_data['link'] = url
        except KeyError:
            parsed_data['link'] = None

        try:
            parsed_data['category'] = pure_data['post']['deal']
        except KeyError:
            parsed_data['category'] = None

        try:
            parsed_data['address'] = pure_data['post']['location']['addressData']['address']
        except KeyError:
            parsed_data['address'] = None

        try:
            parsed_data['district'] = pure_data['post']['location']['addressData']['district']
        except KeyError:
            parsed_data['district'] = None

        try:
            parsed_data['state'] = pure_data['post']['location']['addressData']['state']
        except KeyError:
            parsed_data['state'] = None

        try:
            parsed_data['latitude'] = pure_data['post']['location']['location']['lat']
        except KeyError:
            parsed_data['latitude'] = None

        try:
            parsed_data['longitude'] = pure_data['post']['location']['location']['lng']
        except KeyError:
            parsed_data['longitude'] = None

        try:
            parsed_data['animals'] = pure_data['post']['animals']
        except KeyError:
            parsed_data['animals'] = None

        try:
            parsed_data['phone'] = pure_data['post']['contacts'][0]['formattedPhone']
        except KeyError:
            parsed_data['phone'] = None

        try:
            if pure_data['post']['dailyPriceFull'][0]['price'] and pure_data['post']['dailyPriceFull'][0]['currency'] == '051':
                parsed_data['dailyPriceFull'] = float(pure_data['post']['dailyPriceFull'][0]['price']) / DRAM_TO_USD
            elif pure_data['post']['dailyPriceFull'][0]['price']:
                parsed_data['dailyPriceFull'] = float(pure_data['post']['dailyPriceFull'][0]['price'])
            else:
                parsed_data['dailyPriceFull'] = None
        except (KeyError,TypeError):
            parsed_data['dailyPriceFull'] = None

        try:
            parsed_data['dailiPrice'] = pure_data['post']['daily_price']
        except KeyError:
            parsed_data['dailiPrice'] = None

        try:
            parsed_data['monthly_mortgage_amd'] = pure_data['post']['monthly_mortgage_amd']
        except KeyError:
            parsed_data['monthly_mortgage_amd'] = None

        try:
            if pure_data['post']['priceFull'][0]['price'] and pure_data['post']['priceFull'][0]['currency'] == '051':
                parsed_data['priceFull'] = float(pure_data['post']['priceFull'][0]['price']) /  DRAM_TO_USD
            elif pure_data['post']['priceFull'][0]['price']:
                parsed_data['priceFull'] = float(pure_data['post']['priceFull'][0]['price'])
            else:
                parsed_data['priceFull'] = None
        except (KeyError,TypeError):
            parsed_data['priceFull'] = None

        try:
            parsed_data['propertyType'] = pure_data['post']['propertyType']
        except KeyError:
            parsed_data['propertyType'] = None

        try:
            parsed_data['building_floors'] = pure_data['post']['sections']['about_building']['building_floors']
        except KeyError:
            parsed_data['building_floors'] = None

        try:
            parsed_data['building_type'] = pure_data['post']['sections']['about_building']['building_type']
        except KeyError:
            parsed_data['building_type'] = None

        try:
            parsed_data['area'] = pure_data['post']['sections']['apartment_info'][0]['area']
        except KeyError:
            parsed_data['area'] = None

        try:
            parsed_data['bathrooms'] = pure_data['post']['sections']['apartment_info'][0]['bathrooms']
        except KeyError:
            parsed_data['bathrooms'] = None

        try:
            parsed_data['bedrooms'] = pure_data['post']['sections']['apartment_info'][0]['bedrooms']
        except KeyError:
            parsed_data['bedrooms'] = None

        try:
            parsed_data['ceiling_height'] = pure_data['post']['sections']['apartment_info'][0]['ceiling_height']
        except KeyError:
            parsed_data['ceiling_height'] = None

        try:
            parsed_data['cooling'] = pure_data['post']['sections']['apartment_info'][0]['cooling']
        except KeyError:
            parsed_data['cooling'] = None

        try:
            parsed_data['description_en'] = pure_data['post']['sections']['apartment_info'][0]['description_en']
        except KeyError:
            parsed_data['description_en'] = None

        try:
            parsed_data['floor'] = pure_data['post']['sections']['apartment_info'][0]['floor']
        except KeyError:
            parsed_data['floor'] = None

        try:
            parsed_data['renovation'] = pure_data['post']['sections']['apartment_info'][0]['renovation']
        except KeyError:
            parsed_data['renovation'] = None

        try:
            parsed_data['rooms'] = pure_data['post']['sections']['apartment_info'][0]['rooms']
        except KeyError:
            parsed_data['rooms'] = None

        try:
            parsed_data['sqm_price'] = pure_data['post']['sections']['apartment_info'][0]['sqm_price']
        except KeyError:
            parsed_data['sqm_price'] = None

        try:
            parsed_data['email'] = pure_data['post']['user']['email']
        except KeyError:
            parsed_data['email'] = None

        try:
            parsed_data['first_name'] = pure_data['post']['user']['first_name']
        except KeyError:
            parsed_data['first_name'] = None

        try:
            parsed_data['last_name'] = pure_data['post']['user']['last_name']
        except KeyError:
            parsed_data['last_name'] = None

        try:
            parsed_data['username'] = pure_data['post']['user']['username']
        except KeyError:
            parsed_data['username'] = None

        self.data.append(parsed_data)

    def start_parse(self):
        with open("../Data/CombinedRentLinks.json", 'r') as f:
            data1 = json.load(f)
        with open("../Data/CombinedSellLinks.json", 'r') as f:
            data2 = json.load(f)
        data1.extend(data2)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self._getting_url_data, data1)

        with open("../Data/result.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = list(self.data[0].keys()) if self.data else []
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            print(self.data)
            writer.writerows(self.data)

if __name__ == "__main__":

    # Creating GettingData class object
    parser = GettingData()
    # Start_parse starts parsing and returns result in result.csv file
    parser.start_parse()