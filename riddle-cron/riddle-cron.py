import redis
import random as rd
import json

r = redis.StrictRedis(host="redis-service", port=6379, decode_responses=True, db=1)

riddles = [
    {
        'statement': "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
        'choices': {
            'a': 'Echo',
            'b': 'Whisper',
            'c': 'Shadow',
            'd': 'Music'
        },
        'correct_answer': 'a'
    },
    {
        'statement': "I'm tall when I'm young, and short when I'm old. What am I?",
        'choices': {
            'a': 'Tree',
            'b': 'Candle',
            'c': 'Book',
            'd': 'Pencil'
        },
        'correct_answer': 'b'
    },
    {
        'statement': "I fly without wings. I cry without eyes. Wherever I go, darkness follows me. What am I?",
        'choices': {
            'a': 'Wind',
            'b': 'Cloud',
            'c': 'Bat',
            'd': 'Time'
        },
        'correct_answer': 'b'
    },
    {
        'statement': "The more you take, the more you leave behind. What am I?",
        'choices': {
            'a': 'Footsteps',
            'b': 'Breath',
            'c': 'Memories',
            'd': 'Silence'
        },
        'correct_answer': 'a'
    },
    {
        'statement': "I have keys but open no locks. I have space but no room. You can enter, but you can't go inside. What am I?",
        'choices': {
            'a': 'Piano',
            'b': 'Keyboard',
            'c': 'Computer',
            'd': 'Typewriter'
        },
        'correct_answer': 'b'
    }
]


if __name__ == "__main__":
    rn = rd.randrange(len(riddles))
    r.set("riddle", json.dumps(riddles[rn]))
    r.set("answer", riddles[rn]["correct_answer"])
