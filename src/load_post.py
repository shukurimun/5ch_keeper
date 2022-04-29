import datetime

import requests
from bs4 import BeautifulSoup
import pandas as pd
from plyer import notification


def load_thread_post(url: str):
    """与えられたurl内のスレッドの書き込みをDataFrameで返す

    Args:
        url (str): 5chのURL

    Returns:
        pandas.DataFrame: number,id,name,date,message のカラム
    """
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    message = soup.find_all(class_='post')

    thread_data = {
        'number': [int(i.find(class_='number').get_text()) for i in message],
        'id': [i.find(class_='uid').get_text() for i in message],
        'name': [i.find(class_='name').get_text() for i in message],
        'date': [i.find(class_='date').get_text() for i in message],
        'message': [i.find(class_='escaped').get_text() for i in message]
    }
    df = pd.DataFrame(thread_data)

    # dateカラムから不要な曜日文字列を削除し、datetime型に変える.
    day_of_week = ['(日)', '(月)', '(火)', '(水)', '(木)', '(金)', '(土)']
    for day in day_of_week:
        df['date'] = df['date'].str.replace(day, '', regex=False)
    df['date'] = pd.to_datetime(df['date'])

    return df


def filter_new_post(thread_post, time=1800):
    """新しい書き込みに絞り込む

    Args:
        thread_post (pd.DataFrame): load_thread_postの返り値.
        time (int, optional): [description]. Defaults to 1800.
    Returns:
        pandas.DataFrame: 絞り込まれたDataFrame.経過時間についてのカラムが追加される.
    """
    now = datetime.datetime.now()
    thread_post['elapsed_time'] = (now - thread_post['date']) / datetime.timedelta(seconds=1)
    return thread_post[thread_post['elapsed_time'] <= time]


def notify_desktop(title, message):
    """windowsデスクトップに通知を出す。

    Args:
        title (str): タイトル.一番でかい文字のやつ.
        message (str): 詳細.小さい文字.あんま読めない.
    """
    notification.notify(
        title=title,
        message=message,
        timeout=15
    )


if __name__ == "__main__":
    
    url = 'http://hebi.5ch.net/test/read.cgi/news4vip/1625935376/'
    df = load_thread_post(url)
    print(filter_new_post(df))
