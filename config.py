from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "12787577"))
API_HASH = getenv("API_HASH", "d30cef43991a144be80615919bfcfc6c")
BOT_TOKEN = getenv("BOT_TOKEN","5240547448:AAEllXLVqBvRimDhZcfC7LbnCSpuz7Fly4E")
BOT_NAME = getenv("BOT_NAME","kannadigara_dwani_boT")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
SESSION_NAME = getenv("SESSION_NAME","AQC2vvz59KLQHX2dJDQZebClTomyOhhB4QF5MqTSHgumCc4KtraSRIa5A9TaxBfPH4RPtC0SmYOn9-XYHUG0Laf2TK_CmEIuTQ96cMcqIj9sSQtVNACn9vFcOyUK3fQp6Fpjtiy-FPS-e42LJO7f2Vj1d9y88itjkTCQwk5ZVoOfHeMAVj2UrRaUOVs1sJT3Ep-oNm6IpTRuWQXCs80R_e8QRzaiwWNDWrlfy5d1lsUTU-H10FP6XbgAH1gfBkZHa6-qdEdv3Fzg4Q1yxzavddCMGLH-wMUEoB9X6nwjNZjXgveNwesYAoGc0XVsmKMm6es0cGTkgsc0k0Wh-nC_ZCokAAAAATe3gk0A")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5272015055").split()))
