import requests
from datetime import datetime


token = '67aa46cedcddc0d1a411ea5c7e2f0d842c2e6dbbd113130aa04f6cd5bc75261d51afa1'
group_id = '36studio'
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 2, 13)


def get_posts(token, group_id, start_date, end_date):
    posts = []
    offset = 0
    while True:
        url = f'https://api.vk.com/method/wall.get?domain={group_id}&count=100&offset={offset}&access_token={token}&v=5.131'
        response = requests.get(url).json()
        if 'response' not in response:
            break
        items = response['response']['items']
        if not items:
            break
        for post in items:
            post_date = datetime.utcfromtimestamp(post['date'])
            if post_date < start_date:
                return posts
            if post_date <= end_date:
                posts.append({
                    'date': post_date,
                    'text': post['text'],
                    'likes': post['likes']['count'],
                    'views': post['views']['count'],
                    'reposts': post['reposts']['count']
                })
        offset += 100
    return posts


posts = get_posts(token, group_id, start_date, end_date)

print(posts)
