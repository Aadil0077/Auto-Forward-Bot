from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", 7931283896:AAFXf5Cv6pBYAisqQ8D41Ph0OUySVlCx7hE)
      API_ID = int(getenv("API_ID", 10110297))
      AS_COPY = True if getenv("AS_COPY", True) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "7931283896:AAFXf5Cv6pBYAisqQ8D41Ph0OUySVlCx7hE")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002131762945").replace("\n", "-1002100858444").split(' '))
