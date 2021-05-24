import json
import random


def search_intents(
        msg_from_user="None"):  # the definition looks for whether what the user has entered is in the database
    intents = json.loads(open('patterns.json', encoding="utf-8").read())
    # print("tutaj: " + msg_from_user)
    for intent in intents['intents']:  # searching in a dictionary key intents
        for a, b in intent.items():  # making a dictionary
            for pattern in b['patterns']:  # searching in a dictionary key patterns
                if pattern == msg_from_user:  # checking if the word is in the database
                    lst = b['responses']  # looking for responses
                    lst_len = len(lst)  # len of the list
                    random_number = random.randint(0, lst_len - 1)  # random number from 0 to (len list - 1)
                    word = lst[random_number]  # selecting a word from a list
                    return word


repeating_words = ["jeszczeraz", "jeszczejeden", "znaszjeszczejakis"]
lst_input_context = []  # zapis wszystkich wiadomości od użytkownika
# lst_msg_from_bot = []   # zapis wszystkich wiadomości od bota


# definicja zapisuje wiadomości wysłane do użytkownika od bota
# def context_remember_msg_from_bot(bot_msg):
#     lst_msg_from_bot.append(bot_msg)


def context_user_input_msg(user_msg=""):
    if user_msg != "":
        # dodawanie wiadomości od użytkownika do listy
        is_it_correct = bool
        lst_input_context.append(user_msg)

        # długość listy z wiadomości od użytkownika
        length_lst_input_context = len(lst_input_context)

        # wybieranie ostatniej wiadomości
        current_word = lst_input_context[length_lst_input_context - 1]

        # sprawdzanie czy wpisana wiadomość znajduje się w słowniku repeating
        for i in repeating_words:
            print(i)
            if i == current_word:
                is_it_correct = True
                break
            else:
                is_it_correct = None

        if is_it_correct is not None:   # jeżeli się znajduje wykonaj to
            n = 2
            while True:
                last_word = lst_input_context[length_lst_input_context - n]
                send_msg = search_intents(last_word)
                if send_msg is None:
                    n += 1
                else:
                    return send_msg
        else:   # jeżeli się nie znajduje to zwróć False
            return False
    else:
        return False


if __name__ == '__main__':
    search_intents()
    context_user_input_msg()
