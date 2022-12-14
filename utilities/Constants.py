import datetime as dt

# DISCORD
COLOR = 0x46a063
COOLDOWN_COLOR = 0xff7700
ERROR_COLOR = 0xff0f16
DISCORD_LIMIT = 2 ** 11 # 2048
MAX_SIZE_FIELD_VALUE = 2 ** 10 # 1024
MAX_MAX_SIZE_FIELD_VALUE = 5000 # max embed size
ME_AVATAR = "https://cdn.discordapp.com/icons/927754329035780137/a_634e8eae8c4f15d8a988b2bf17f41ce7.gif"
# APIS
USER_AGENT = {'User-Agent': 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/73.0'}
MAX_RETRIES = 10


def discord_timestamp():
    return dt.datetime.now()


def percentage(total, x):
    return "{:.2f}%".format(x * 100 / total) if total > 0 else 0