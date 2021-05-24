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
        self.lst_unknown_word = txt_translate_msg.split()
        self.len_word = len(self.lst_unknown_word)
        self.len_word = len(txt_translate_msg)

    def szukanie_zaawansowane(self):
        # szukanie od prawa do lewa
        n_1 = 1
        while n_1 <= self.len_word:
            n_2 = ""
            n_2 = n_2.join(self.lst_unknown_word)
            n_2 = n_2[0:self.len_word - n_1]
            if n_2 == "":
                break
            wynik = search_intents(n_2)
            n_1 += 1
            if wynik is not None:
                return wynik

        # szukanie słowa od lewej do prawej
        x = 1
        for i in range(0, self.len_word):
            n_2 = ""
            n_2 = n_2.join(self.lst_unknown_word)
            n_2 = n_2[x:]
            if n_2 == "":
                break
            wynik = search_intents(n_2)
            x += 1
            if x > self.len_word:
                break
            if wynik is not None:
                return wynik

        # odcinanie lewa i prawa ku środku
        odcinanie_od_lewa = 0
        odcinanie_od_prawa = -1

        while True:
            lst_1 = ""
            lst_1 = lst_1.join(self.lst_unknown_word)
            lst_1 = lst_1[odcinanie_od_lewa:odcinanie_od_prawa]
            if lst_1 == "":
                break
            else:
                wynik = search_intents(lst_1)
                if wynik is not None:
                    return wynik
            odcinanie_od_lewa += 1
            lst_1 = lst_1.join(self.lst_unknown_word)
            lst_1 = lst_1[odcinanie_od_lewa:odcinanie_od_prawa]
            if lst_1 == "":
                break
            else:
                wynik = search_intents(lst_1)
                if wynik is not None:
                    return wynik


if __name__ == "__main__":
    Chat()
