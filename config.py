import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "25619358"))
API_HASH = getenv("API_HASH", "3a178d74b056ba890432a2e1dd5bc3b6‎")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7469825671:AAE2Qr4VPF73_SNA146Z81e9wVCvfM66KyY")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Raghav23:Raghav23@cluster0.6nrx6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Vars For API End Pont.
YTPROXY_URL = getenv("YTPROXY_URL", 'https://yt.okflix.top/api') ## E.G https://yt.okflix.top/api/jADTdg-o8i0 Returns Download Info.
COOKIES_URL=getenv("COOKIES_URL" , "")

## Other vaes
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 120))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002430579671"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "2121966922"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/xbitcode/music.git",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/carxynetok")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/carxynetok")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
ASSISTANT_LEAVE_TIME = int(getenv("ASSISTANT_LEAVE_TIME",  5400))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 204857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

PRIVATE_BOT_MODE_MEM = int(getenv("PRIVATE_BOT_MODE_MEM", 1))


CACHE_DURATION = int(getenv("CACHE_DURATION" , "86400"))  #60*60*24
CACHE_SLEEP = int(getenv("CACHE_SLEEP" , "3600"))   #60*60


# Get your pyrogram v2 session from 
STRING1 = getenv("STRING_SESSION", "BQGG654AGMtLgmVy8EV-Hga0u5ieGSZDCGBAiYY-GiBlzMSf6ArHmUhdsEQi3KGw5hX3Ctk3HSBpNylORb1XgJdTb0lXPsKyc3jZZ0yCR7Lz1pHtVu7Hs9dg6ag5WcpzSLkCiaE0APQVnBxzunHbtKNqvOCBaoARMLZkz1FDWBU70Z5xNSgPQAyCUWV-pa1i0oMaoGH718ntjWSDfMyfvjipQmUrwbZcAMs45IH9W7ddnAIxm2MVbVMAU4axNl_2mo7Palj_1JDzfT6xYH0LAhcRebOKDZ_UsYW3DqxJ6NFFpfWINDAz6QAF7OaDopcfTGjkDC6qhiwc0SkKnpEagxFa5ap0aAAAAAHVliPiAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
file_cache: dict[str, float] = {}

START_IMG_URL = ["https://envs.sh/wzY.jpg"]
    
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/wzY.jpg"
)
PLAYLIST_IMG_URL = "https://envs.sh/wzY.jpg"
STATS_IMG_URL = "https://envs.sh/wzY.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/wzY.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/wzY.jpg"
STREAM_IMG_URL = "https://envs.sh/wzY.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/wzY.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/wzY.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/wzY.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/wzY.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/wzY.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:360"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
