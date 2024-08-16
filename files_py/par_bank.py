
import csv
import requests
from bs4 import BeautifulSoup
import csv
import time
from tqdm import trange


idx = 1

cookies = {
    'BANKI_RU_USER_IDENTITY_UID': '1930769765026240969',
    'ga_client_id': '2026460267.1715352250',
    'tmr_lvid': 'cca824a1d9c020dc5cbe845d56b9e3a8',
    'tmr_lvidTS': '1715352249846',
    '_ym_uid': '1715352251109916049',
    '_ym_d': '1715352251',
    'ym_client_id': '1715352251109916049',
    'uxs_uid': 'c36f6960-0edb-11ef-9526-c7b6ed469e25',
    '_ga_PG15GEX7CK': 'GS1.1.1715352249.1.1.1715352345.0.0.0',
    'views_counter': '%7B%22folk_rating.response%22%3A%5B11144731%5D%7D',
    'PHPSESSID_NG_USER_RATING': 'vdt7u276rd6jamgd6dimv60cf6',
    'HO_SOURCE': 'seo_yandex',
    'aff_sub3': '%2Fservices%2Fresponses%2Fbank%2Fresponse%2F11144731%2F',
    '_ym_isad': '1',
    '_gcl_au': '1.1.1326007388.1723791919',
    'gtm-session-start': '1723791917809',
    '_ym_visorc': 'b',
    'domain_sid': '-LK3WmtWlgl2cv1Wl67hv%3A1723791919310',
    '_gid': 'GA1.2.509724177.1723791921',
    '_dc_gtm_UA-38591118-1': '1',
    'cid_time_cookie': '2026460267.1715352250 | 16.08.2024 | 10:05:49 | +03:00',
    'banki_prev_page': '/services/responses/list/',
    'aff_sub3': '/services/responses/bank/response/11144731/',
    'BANKI_RU_MYBANKI_ID': 'fe57687f-7876-4c52-bfe7-714fb141e5cf',
    '_banki_ru_mybanki_id_migration': '2024-08-14-updatedCookieDomain',
    'counter_session': '4',
    '_ga_MEEKHDWY53': 'GS1.1.1723791920.2.1.1723791965.15.0.0',
    '_ga': 'GA1.2.2026460267.1715352250',
    'tmr_detect': '0%7C1723791968038',
    'user_region_id': '4',
    '_ga_EFC0FSWXRL': 'GS1.1.1723791918.1.1.1723792003.0.0.0',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
    'referer': 'https://www.banki.ru/services/responses/list/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

all_data = []
# параметры для поиска по файлу
for x in trange(1, 15001): # Изменено для получения данных с 10 страниц
    # параметры для запроса
    params = {
        'page': x,
        'is_countable': 'on',
    }
    # отправка запроса
    response = requests.get('https://www.banki.ru/services/responses/list/ajax/', params=params, cookies=cookies, headers=headers)
    all_data.append(response.json())
    if x % 100 == 0:
        # Сохранение данных в CSV файл
        with open('bank_reviews_.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['idx', 'Score', 'Text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for data in all_data:
                for item in data['data']:
                    writer.writerow({'idx': idx, 'Score': item['grade'], 'Text': item['text']})
                    idx += 1