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





user = json.loads(open('user.json').read())
bot = json.loads(open('bot.json').read())



def get_message(message):
    for intent in user:
        for i in user[intent]:
            if fuzz.ratio(message, i) > 80:
                return random.choice(tuple(bot[intent]))


# def get_message(message):
#     for i in hello:
#         if fuzz.ratio(message, i) > 80:
#             return random.choice(tuple(hello_resp))

