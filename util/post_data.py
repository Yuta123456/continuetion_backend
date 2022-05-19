from util.firebase import exist_today_data


def post_pixela(userId, today):
    if exist_today_data(userId, today):
        return
    # TODO: pixelaへの投稿