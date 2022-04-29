import json
import time
import random

from src import load_post, utils, write_thread


def main():
    url, times, message, keywords, name = load_setting()
    post_df = load_post.load_thread_post(url)
    new_post = load_post.filter_new_post(post_df, times)

    if (new_post['elapsed_time'].min() >= 100) or (len(new_post) == 0):
        write_thread.write_to_5ch(url, message, name)
    else:
        print('最近書き込みがあったからスルーするー')

    for keyword in keywords:
        if len(new_post[new_post['message'].str.contains(keyword)]) > 0:
            utils.notify_desktop('新規来たかも', list(new_post[new_post['message'].str.contains(keyword)]['message'])[0])


def load_setting():
    with open('setting.json', encoding='utf-8') as f:
        settings = json.load(f)
    if type(settings['message']) is str:
        return settings['url'], settings['time'], settings['message'], settings['keyword'], settings['name']
    else:
        return settings['url'], settings['time'], random.choice(settings['message']), settings['keyword'], settings['name']


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1800)
