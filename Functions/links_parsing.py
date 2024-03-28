import json
import time

import requests
from fake_useragent import UserAgent


class FindingSellParseItemLinks():
    '''
    Class that represents sell house links parser
    '''
    cookies = {
        '_gcl_au': '1.1.1578380407.1708608289',
        '_ym_uid': '1708608289339730971',
        '_ym_d': '1708608289',
        '_fbp': 'fb.1.1708608290017.2116922163',
        '_gac_UA-215674752-1': '1.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE',
        '_gcl_aw': 'GCL.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE',
        '_ym_isad': '2',
        '_gid': 'GA1.2.1815942576.1711469028',
        '_ym_visorc': 'w',
        '_clck': '12tethq%7C2%7Cfke%7C0%7C1513',
        '_clsk': 'm0m0wq%7C1711473354034%7C39%7C1%7Cn.clarity.ms%2Fcollect',
        '_ga_5LHZPJK3WL': 'GS1.1.1711469028.3.1.1711473703.58.0.0',
        '_ga': 'GA1.2.710196867.1708608290',
        '_gat_UA-215674752-1': '1',
        'XSRF-TOKEN': 'eyJpdiI6IitoK2FuYWxwTUFzZUd2V0J2bWlrZHc9PSIsInZhbHVlIjoieHlrV09TMGZkY0hwZlE1dDBOUU5xMHU4Z24yVWNEM2ZvU1Z4NDBobHE4Unh3ekJUb2IxLzYyYlRreWN1dnRkZHVXTUpXbUlVQklabTV4OGFCSVkzeHpSdjhYZWQ3cDNTM1ZBbzBkeE95S3ZMVmp5UkNEcGFHUWZtTHB4VWZyN1giLCJtYWMiOiIwOWM4ZTUyZGZhZjM5NDMxYWIwNWRmNGRjOWI2MTAyNWZmZGVjZjU3MzE2N2I1MTA4YjdlN2NlNTE4Y2M1MzgxIiwidGFnIjoiIn0%3D',
        'banali_session': 'eyJpdiI6IkswUUhqdlhDYWU0K0d0aTJZdHBWL3c9PSIsInZhbHVlIjoiTkh3Z1ZjeXFBOVJOUWpDVUgwMGlKNU1aMjBRaFFjMExtM25XS2ZmcThSM1FiVW4rMlpDcTVWQWhJaHRCSEV1TDNRTEJsU1RmQkVjMk9RTzZKNUxsVGJCOHdlNXhXc3h5MFRCUHdPOXdlSURZU3RiVnJadFBDRFQ4dDNlTU95UzUiLCJtYWMiOiI1YmZmMjVlYjUxMTFkZjdhZTQwZjhlM2JjNDkzMTEwMmI3ZDViNTVmZDRlNjIwMWIyZTIyZGY2OTQ4OGNiNTY5IiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'hy',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://banali.am',
        'referer': 'https://banali.am/hy/vachark?page=3',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-csrf-token': 'lYNDRfk3HcQ8ur5lxD0gDOVOFUwgipnvfvxsDW35',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6IitoK2FuYWxwTUFzZUd2V0J2bWlrZHc9PSIsInZhbHVlIjoieHlrV09TMGZkY0hwZlE1dDBOUU5xMHU4Z24yVWNEM2ZvU1Z4NDBobHE4Unh3ekJUb2IxLzYyYlRreWN1dnRkZHVXTUpXbUlVQklabTV4OGFCSVkzeHpSdjhYZWQ3cDNTM1ZBbzBkeE95S3ZMVmp5UkNEcGFHUWZtTHB4VWZyN1giLCJtYWMiOiIwOWM4ZTUyZGZhZjM5NDMxYWIwNWRmNGRjOWI2MTAyNWZmZGVjZjU3MzE2N2I1MTA4YjdlN2NlNTE4Y2M1MzgxIiwidGFnIjoiIn0=',
    }

    json_data = {
        'params': {
            'filters': {
                'public_code': '',
                'renovation': [],
                'structure_type': '',
                'developer_name': '',
                'rooms': [],
                'rental_price_type': [],
                'property_type': [],
                'is_developer': [],
                'sqm_price': [],
                'price': [],
                'monthly_mortgage': [],
                'area': [],
                'heating': [],
                'furniture': [],
                'amenities': [],
                'bedrooms': [],
                'floor': [],
                'has_3D_tour': [],
                'building_name': '',
                'animals': [],
                'with_installment': [],
                'is_favorite': [],
                'deal': 'sell',
                'state_id': [],
                'district_id': [],
            },
            'sortBy': 'date_desc',
        },
    }

    def __init__(self):
        self.ua = UserAgent()
        self.links = []

    def _get_response(self, page: int) -> requests.Response:
        '''
        Send post method to Link and returns a response
        :param page (int): The page number to request.
        :return (requests.Response): The response object
        '''
        headers = {'User-Agent': self.ua.random}
        params = {
            'page': page,
        }
        response = requests.post(
            'https://banali.am/api/search/filter-posts',
            params=params,
            cookies=self.cookies,
            headers=self.headers,
            json=self.json_data,
        )
        return response

    def _find_link_on_page(self, page: int):
        '''
        Parses links on page
        :param page(int): the number of page
        :return: None if response.status_code != 200
        '''
        response = self._get_response(page)
        if response.status_code == 200:
            response_data = json.loads(response.text)
        else:
            print(f"Cannot get repsonse from page-{page}")
            return

        for post in response_data["data"]["posts"]["data"]:
            hy_value = post["slug"]["hy"]
            link = f"https://banali.am/hy/{hy_value}"
            self.links.append(link)
        print(f"Finished page - {page}")

    def _find_all_links(self, times_to_repeat: int = 1) -> None:
        '''
        Finds all links from multiple pages and stores them in the links list.
        :param times_to_repeat(int, optional): Number of times to repeat the process. Defaults to 1.
        '''
        for i in range(times_to_repeat * 1000):
            self._find_link_on_page(i)
            time.sleep(0.5)
            if i % 100 == 0:
                time.sleep(5)

    def _links_to_json(self, file_name: str):
        '''
        Func that creates .json file of self.links list
        :param file_name: Name of the file
        '''
        parsed_data = {'links': list(set(self.links))}
        json_data = json.dumps(parsed_data, indent=4)
        with open(f"../Data/{file_name}.json", "w") as json_file:
            json_file.write(json_data)

    def get_data_links(self, file_name: str, time_to_repeat: int = 1):
        self._find_all_links(time_to_repeat)
        self._links_to_json(file_name)


class FindingRentParseItemLinks(FindingSellParseItemLinks):
    '''
    Class that represents rent house links parser
    '''
    cookies = {
        '_gcl_au': '1.1.1578380407.1708608289',
        '_ym_uid': '1708608289339730971',
        '_ym_d': '1708608289',
        '_fbp': 'fb.1.1708608290017.2116922163',
        '_gac_UA-215674752-1': '1.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE',
        '_gcl_aw': 'GCL.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE',
        '_gid': 'GA1.2.1815942576.1711469028',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        '_clck': '12tethq%7C2%7Cfkg%7C0%7C1513',
        '_gat_UA-215674752-1': '1',
        '_ga_5LHZPJK3WL': 'GS1.1.1711600409.6.1.1711601416.40.0.0',
        '_ga': 'GA1.2.710196867.1708608290',
        '_clsk': 'wwkkm2%7C1711601417885%7C35%7C1%7Cn.clarity.ms%2Fcollect',
        'XSRF-TOKEN': 'eyJpdiI6IjczSXRDUDllRVBhYnNWTENIUERPUXc9PSIsInZhbHVlIjoiVWNsRGtXemVxd2RxQ1U3NXNCaVdtcXlxbmk1ZUcxWWlrWnZmT2hoazZ1WGJuT241SGh1RGVQOGFScElLbUhIaVU1ck9sUmEvSWt5N2FtLzQ2Nm5zZEJQRVZ0WDNrWHZOTUZKajFXTkNNTDViYWJQcTZlWGdhOGpIOXpOcUYvLzYiLCJtYWMiOiIzYTA4ZjU5MTI5YTU5ZjlmZGM2MGQyZDBiNmYzMzgzZGZlZGU2NWRhYmFkZGIzZTlmMTBmOTJkYjMwY2I1ZTc4IiwidGFnIjoiIn0%3D',
        'banali_session': 'eyJpdiI6InFENHBsNDB6anZMYXNoWjhZRXR0WGc9PSIsInZhbHVlIjoibnVqekRhTi9PYVpnSnNGSnFMOTV2N1VxWGFSRnJhS2U4R2Y2VUVqWWNYUXcvZmFoaWYyWms2MkJGOEVnaFFHWU05b1FuY0tqZXZqc1d6RWl5WWdETU1ndGMzUjJCSUlackhYR2tpczl5QTJDQ1RPV0lhT0pKOWNwanBBYjZ3NWEiLCJtYWMiOiIyNjA0MDNkNzkzZTk1NjQ3OGQ4ZjA4YTcyMDZmNGE1ZmEyYzA4MzVhYjIxODE5ZTNjMWE5ZWUwNTBlMDM5ZWQ3IiwidGFnIjoiIn0%3D',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'hy',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': '_gcl_au=1.1.1578380407.1708608289; _ym_uid=1708608289339730971; _ym_d=1708608289; _fbp=fb.1.1708608290017.2116922163; _gac_UA-215674752-1=1.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE; _gcl_aw=GCL.1710943579.CjwKCAjwkuqvBhAQEiwA65XxQIAhZKGYs34aMpt1TpVUoJR3Bd-9M1WhHwdIQFJU-j2Gh1Z9sBBaDBoCShEQAvD_BwE; _gid=GA1.2.1815942576.1711469028; _ym_isad=2; _ym_visorc=w; _clck=12tethq%7C2%7Cfkg%7C0%7C1513; _gat_UA-215674752-1=1; _ga_5LHZPJK3WL=GS1.1.1711600409.6.1.1711601416.40.0.0; _ga=GA1.2.710196867.1708608290; _clsk=wwkkm2%7C1711601417885%7C35%7C1%7Cn.clarity.ms%2Fcollect; XSRF-TOKEN=eyJpdiI6IjczSXRDUDllRVBhYnNWTENIUERPUXc9PSIsInZhbHVlIjoiVWNsRGtXemVxd2RxQ1U3NXNCaVdtcXlxbmk1ZUcxWWlrWnZmT2hoazZ1WGJuT241SGh1RGVQOGFScElLbUhIaVU1ck9sUmEvSWt5N2FtLzQ2Nm5zZEJQRVZ0WDNrWHZOTUZKajFXTkNNTDViYWJQcTZlWGdhOGpIOXpOcUYvLzYiLCJtYWMiOiIzYTA4ZjU5MTI5YTU5ZjlmZGM2MGQyZDBiNmYzMzgzZGZlZGU2NWRhYmFkZGIzZTlmMTBmOTJkYjMwY2I1ZTc4IiwidGFnIjoiIn0%3D; banali_session=eyJpdiI6InFENHBsNDB6anZMYXNoWjhZRXR0WGc9PSIsInZhbHVlIjoibnVqekRhTi9PYVpnSnNGSnFMOTV2N1VxWGFSRnJhS2U4R2Y2VUVqWWNYUXcvZmFoaWYyWms2MkJGOEVnaFFHWU05b1FuY0tqZXZqc1d6RWl5WWdETU1ndGMzUjJCSUlackhYR2tpczl5QTJDQ1RPV0lhT0pKOWNwanBBYjZ3NWEiLCJtYWMiOiIyNjA0MDNkNzkzZTk1NjQ3OGQ4ZjA4YTcyMDZmNGE1ZmEyYzA4MzVhYjIxODE5ZTNjMWE5ZWUwNTBlMDM5ZWQ3IiwidGFnIjoiIn0%3D',
        'origin': 'https://banali.am',
        'referer': 'https://banali.am/hy/vardzakalutyun?page=2',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-csrf-token': 'UDPWfx1O5VBedCw5F7J4MEnEOp7VraITDiZ1pNfQ',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'eyJpdiI6IjczSXRDUDllRVBhYnNWTENIUERPUXc9PSIsInZhbHVlIjoiVWNsRGtXemVxd2RxQ1U3NXNCaVdtcXlxbmk1ZUcxWWlrWnZmT2hoazZ1WGJuT241SGh1RGVQOGFScElLbUhIaVU1ck9sUmEvSWt5N2FtLzQ2Nm5zZEJQRVZ0WDNrWHZOTUZKajFXTkNNTDViYWJQcTZlWGdhOGpIOXpOcUYvLzYiLCJtYWMiOiIzYTA4ZjU5MTI5YTU5ZjlmZGM2MGQyZDBiNmYzMzgzZGZlZGU2NWRhYmFkZGIzZTlmMTBmOTJkYjMwY2I1ZTc4IiwidGFnIjoiIn0=',
    }

    json_data = {
        'params': {
            'filters': {
                'public_code': '',
                'renovation': [],
                'structure_type': '',
                'developer_name': '',
                'rooms': [],
                'rental_price_type': [],
                'property_type': [],
                'is_developer': [],
                'sqm_price': [],
                'price': [],
                'monthly_mortgage': [],
                'area': [],
                'heating': [],
                'furniture': [],
                'amenities': [],
                'bedrooms': [],
                'floor': [],
                'has_3D_tour': [],
                'building_name': '',
                'animals': [],
                'with_installment': [],
                'is_favorite': [],
                'deal': 'rent',
                'state_id': [],
                'district_id': [],
            },
            'sortBy': 'date_desc',
        },
    }

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    # Run code below to get sell data links!
    finder = FindingSellParseItemLinks()
    finder.get_data_links('SellLink1')

    # Run code below to get rent data links!
    finder = FindingRentParseItemLinks()
    finder.get_data_links('RentLinks2', 1)
