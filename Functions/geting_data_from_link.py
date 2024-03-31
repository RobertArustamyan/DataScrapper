import json

import requests
from fake_useragent import UserAgent


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

        # Making a GET request to the constructed URL
        response = requests.get(
            f'https://banali.am/api/post/slug/{shorted_url}',
            cookies=self.cookies,
            headers=self.headers,
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
        pure_data = self._making_json(self._get_response(url))

        if not pure_data:
            return None

        # List of data per item
        parsed_data = {}

        # Link of item
        parsed_data['link'] = url

        # Category (sell, rent)
        parsed_data['category'] = pure_data['post']['deal']

        # Address of item
        parsed_data['address'] = pure_data['post']['location']['addressData']['address']
        parsed_data['district'] = pure_data['post']['location']['addressData']['district']
        # City of item
        parsed_data['state'] = pure_data['post']['location']['addressData']['state']

        # Latitude and Longtitude
        parsed_data['latitude'] = pure_data['post']['location']['location']['lat']
        parsed_data['longtitude'] = pure_data['post']['location']['location']['lng']

        # Animals alowance
        parsed_data['animals'] = pure_data['post']['animals']

        # Phone number
        parsed_data['phone'] = pure_data['post']['contacts'][0]['formattedPhone']

        # Price with its currency
        parsed_data['dailyPriceFull'] = f"{pure_data['post']['dailyPriceFull'][0]['price']} - {pure_data['post']['dailyPriceFull'][0]['currency']}"
        parsed_data['dailiPrice'] = pure_data['post']['daily_price']

        parsed_data['monthly_mortgage_amd'] = pure_data['post']['monthly_mortgage_amd']
        parsed_data[
            'priceFull'] = f"{pure_data['post']['priceFull'][0]['price']} - {pure_data['post']['priceFull'][0]['currency']}"

        parsed_data['propertyType'] = pure_data['post']['propertyType']

        parsed_data['building_floors'] = pure_data['post']['sections']['about_building']['building_floors']
        parsed_data['building_type'] = pure_data['post']['sections']['about_building']['building_type']
        parsed_data['area'] = pure_data['post']['sections']['apartment_info'][0]['area']
        parsed_data['bathrooms'] = pure_data['post']['sections']['apartment_info'][0]['bathrooms']
        parsed_data['bedrooms'] = pure_data['post']['sections']['apartment_info'][0]['bedrooms']
        parsed_data['area'] = pure_data['post']['sections']['apartment_info'][0]['area']
        parsed_data['ceiling_height'] = pure_data['post']['sections']['apartment_info'][0]['ceiling_height']
        parsed_data['cooling'] = pure_data['post']['sections']['apartment_info'][0]['cooling']
        parsed_data['description_en'] = pure_data['post']['sections']['apartment_info'][0]['description_en']

        try:
            parsed_data['floor'] = pure_data['post']['sections']['apartment_info'][0]['floor']
        except KeyError:
            parsed_data['floor'] = None
        parsed_data['renovation'] = pure_data['post']['sections']['apartment_info'][0]['renovation']
        parsed_data['rooms'] = pure_data['post']['sections']['apartment_info'][0]['rooms']
        parsed_data['sqm_price'] = pure_data['post']['sections']['apartment_info'][0]['sqm_price']

        parsed_data['email'] = pure_data['post']['user']['email']
        parsed_data['first_name'] = pure_data['post']['user']['first_name']
        parsed_data['last_name'] = pure_data['post']['user']['last_name']
        parsed_data['username'] = pure_data['post']['user']['username']

        self.data.append(parsed_data)


if __name__ == "__main__":
    parser = GettingData()
    parser._getting_url_data(
        "https://banali.am/hy/vachark/bnakaran/1-senyakanoc/Ararat/Artashat/Araratyan-poxoc-B25706")
    parser._getting_url_data("https://banali.am/hy/vachark/bnakaran/4-senyakanoc/Erevan/Avan/6-Almatii-poxoc-B20506")
    parser._getting_url_data(
        "https://banali.am/hy/vardzakalutyun/bnakaran/1-senyakanoc/Kotayq/Caxkadzor/Caxkadzor-B23574")
    parser._getting_url_data(
        "https://banali.am/hy/vardzakalutyun/bnakaran/3-senyakanoc/Erevan/Arabkir/Nikoxayos-Adonci-poxoc-B32579")
    parser._getting_url_data(
        "https://banali.am/hy/vachark/arandznatun/3-senyakanoc/Kotayq/Dzoraxbyur/Dzoraxbyur-H14879")
    print(parser.data)
