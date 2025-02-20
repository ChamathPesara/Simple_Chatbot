import re
import long_response as long

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Count how many recognized words are present in the user message
    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    # Prevent division by zero
    if len(recognized_words) == 0:
        percentage = 0
    else:
        percentage = float(message_certainty) / float(len(recognized_words))

    # Check if all required words are present
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Return probability score
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Response Definitions
    response('Hello!', ['hello', 'hi', 'sup', 'howdy', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!', ['i', 'love', 'this', 'program'], required_words=['this', 'program'])
    response(long.eating, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.weather, ['how', 'is', 'the', 'weather', 'today'], required_words=['weather'])
    response(long.bot_name, ['what', 'is', 'your', 'name'], required_words=['your', 'name'])

    # Get best response
    best_match = max(highest_prob_list, key=highest_prob_list.get, default=None)

    return long.unknown() if best_match is None or highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing responses
while True:
    print('Bot:', get_response(input('You: ')))
