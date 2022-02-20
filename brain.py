import random, json, os, time
from fuzzywuzzy import fuzz

# Use this later for text vs attachment
# if message["message"].get("text"):
#                         response_sent_text = brain.get_message(message["message"].get("text"))
#                         send_message(recipient_id, response_sent_text)
#                     # if user sends us a GIF, photo,video, or any other non-text item
#                     if message["message"].get("attachments"):
#                         response_sent_nontext = brain.get_message()
#                         send_message(recipient_id, response_sent_nontext)







def get_message(message):
    if fuzz.ratio(message, 'How soon') > 80:
        # time.sleep(0.2)
        return "soooon"
    # return random.choice(tuple(howsoon))