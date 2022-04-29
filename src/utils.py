from plyer import notification


def notify_desktop(title: str, message: str):
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


if __name__ == '__main__':
    notify_desktop('test', 'test_test')
