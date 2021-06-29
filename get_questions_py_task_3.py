import requests
from datetime import datetime, timedelta
from pprint import pprint


def get_questions_py(tag='python'):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = \
        {
            'fromdate': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'),
            'todate': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
            'tagged': tag.lower(), 'site': 'stackoverflow'
        }
    response = requests.get(url, params).json()
    questions_dict = {items['title']: items['link'] for items in response['items']}
    return questions_dict


if __name__ == '__main__':
    pprint(get_questions_py())
