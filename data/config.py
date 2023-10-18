from environs import Env

env = Env()
env.read_env()

ADMINS = env.list("ADMINS")
BOT_TOKEN = env.str("BOT_TOKEN")

IP = env.str("IP")
DB_NAME = env.str("DB_NAME")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")

POSTGRES_URL = f"postgresql://{DB_USER}:{DB_PASS}@{IP}/{DB_NAME}"
