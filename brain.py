import json
import random


def search_intents(
        msg_from_user="None"):  # the definition looks for whether what the user has entered is in the database
    intents = json.loads(open('patterns.json', encoding="utf-8").read())
    print("tutaj: " + msg_from_user)
    for intent in intents['intents']:  # searching in a dictionary key intents
        for a, b in intent.items():  # making a dictionary
            for pattern in b['patterns']:  # searching in a dictionary key patterns
                if pattern == msg_from_user:  # checking if the word is in the database
                    lst = b['responses']  # looking for responses
                    lst_len = len(lst)  # len of the list
                    random_number = random.randint(0, lst_len - 1)  # random number from 0 to (len list - 1)
                    word = lst[random_number]  # selecting a word from a list
                    return word


if __name__ == '__main__':
    search_intents()
