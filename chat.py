from brain import *


class Chat:
    def __init__(self):
        self.user_message = ""  # make global variable for user msg
        self.translate_msg = ""  # make global variable for translate user msg

        self.lst_unknown_word = []
        self.length_list = len(self.lst_unknown_word)

    def chat_analyze(self, msg):
        self.user_message = msg  # msg from user insert to global variable
        print(self.user_message)

        self.zamiana_polskich_liter()  # convert to text without polish letter
        self.zamiana_polskich_liter_2()  # konwertowanie do postaci bez spacji i znaków specjalnych

        try_search = search_intents(self.translate_msg)  # najprostsze wyszukiwanie
        if try_search is not None:
            return try_search
        else:
            final_search = self.szukanie_zaawansowane()
            if final_search is not None:
                return final_search
            else:
                return "Nie rozumiem"

    def zamiana_polskich_liter(self):
        txt = self.user_message
        txt = txt.lower()

        y = {"ą": "a", "ć": "c", "ę": "e", "ł": "l",
             "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}
        z = {"!", "?", ".", ",", "<", ">", "/", ";", "(", ")",
             ":", '"'}

        my_table = txt.maketrans(y)
        self.translate_msg = txt.translate(my_table)

        self.translate_msg = self.translate_msg.translate(
            {ord(i): None for i in z})
        self.translate_msg = self.translate_msg.replace(" ", "")
        # print(self.translate_msg)

    def zamiana_polskich_liter_2(self):
        txt = self.user_message
        txt = txt.lower()

        y = {"ą": "a", "ć": "c", "ę": "e", "ł": "l",
             "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}
        z = {"!", "?", ".", ",", "<", ">", "/", ";", "(", ")", ":"}

        my_table = txt.maketrans(y)
        txt_translate_msg = txt.translate(my_table)
        txt_translate_msg = txt_translate_msg.translate(
            {ord(i): None for i in z})

        self.lst_unknown_word = []
        self.lst_unknown_word = self.txt_translate_msg.split()
        self.dlugosc_listy = len(self.lst_unknown_word)
        self.len_word = len(self.txt_translate_msg)

    def szukanie_zaawansowane(self):
        # szukanie słowa od prawej strony
        x = -1
        for i in range(0, self.len_word):
            n_2 = ""
            n_2 = n_2.join(self.lst_unknown_word)
            n_2 = n_2[:x]
            print("chat 1: " + n_2)
            self.wynik = search_intents(n_2)
            print("chat 2: " + str(self.wynik))
            x -= 1
            if self.wynik is not None:
                return self.wynik


if __name__ == "__main__":
    Chat()
