import json
import concurrent.futures
import requests
from fake_useragent import UserAgent


class FindingParseItemLinks():
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

    def get_response(self, page):
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

    def __find_link_on_page(self, page):
        response = self.get_response(page).text
        response_data = json.loads(response)

        for post in response_data["data"]["posts"]["data"]:
            hy_value = post["slug"]["hy"]
            link = f"https://banali.am/hy/{hy_value}"
            self.links.append(link)

    def find_all_links(self):
        for i in range(677):
            self.__find_link_on_page(i)
            print(f'page - {i}')

    def links_to_json(self):
        parsed_data = {'links': list(set(self.links))}
        json_data = json.dumps(parsed_data, indent=4)
        with open("links.json", "w") as json_file:
            json_file.write(json_data)


if __name__ == '__main__':
    finder = FindingParseItemLinks()
    finder.find_all_links()
    finder.links_to_json()
