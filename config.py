from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 27353035))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "6257927828"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "STORM_CHATZ")
UPDATE_CHNL = getenv("UPDATE_CHNL", "STORM_TECHH")
OWNER_USERNAME = getenv("OWNER_USERNAME", "kexx_Xd")

IMG = [
    "https://graph.org/file/628e6352435e08129f882.jpg",
    "https://graph.org/file/20e44fa20dc9d58c44093.jpg",
    "https://graph.org/file/69dba4600258a67837f9d.jpg",
    "https://graph.org/file/9b9ea9cbdc19bcfb71006.jpg",
    "https://graph.org/file/338fc85de21fb02c73933.jpg",
    "https://graph.org/file/50a4605cfc9ce5b108fde.jpg",
    "https://graph.org/file/59e9305a5c6d8dad4c70c.jpg",
    "https://graph.org/file/43226ca38aecdb9dd1a4c.jpg",
]

STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]
