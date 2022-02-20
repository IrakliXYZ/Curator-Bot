import random, json, os, time
from fuzzywuzzy import fuzz










def get_message(message):
    if fuzz.ratio(message, 'How soon') > 80:
        # time.sleep(0.2)
        return "soooon"
    # return random.choice(tuple(howsoon))