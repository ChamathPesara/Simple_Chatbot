import random

eating  = "I don't eat anything because I'm a bot"
weather = "Ask from google weather about that"
bot_name = "My name is Simon and I'm a chatbot"


def unknown():
    response = ['Could you please re-phrase that ?',
                '...',
                'Sounds about right',
                'What does that mean ?',
                'Sorry ??'][random.randrange(5)]
    return response