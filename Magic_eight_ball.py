import random

RESPONSES = [
    "It is certain",
    "Without a doubt",
    "Most likely",
    "Ask again later",
    "Can not predict now",
    "Do not count on it",
    "My reply is NO",
    "Very Doubtful"
]

def get_eight_ball_responses():
    return random.choices(RESPONSES)
