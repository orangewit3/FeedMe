from firebase import firebase

from next_generation import NextGen

fb = None

data = None

def main():

    global fb

    global data

    fb = firebase.FirebaseApplication("https://alexa-feed-me.firebaseio.com/", None)

    data = fb.get('users', None)

    users = list(data.keys())

    for user in users:

        article_text = process_user(user)

        user_path = 'users/' + user

        fb.put(user_path, 'articles', article_text)


def process_user(user_id):

    global data

    similarity_processor = NextGen(data[user_id]['articles'], data[user_id]['query'])

    information_to_update = similarity_processor.convert_relevant_words_article()

    return information_to_update


main()
