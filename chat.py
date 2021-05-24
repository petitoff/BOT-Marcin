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
        self.zamiana_polskich_liter_2()  # converting to characters without spaces or special characters

        # tworzenie funkcji kontekstu
        context_checking = context_user_input_msg(self.translate_msg)
        if context_checking is not False:
            return context_checking

        try_search = search_intents(self.translate_msg)  # the simplest search
        if try_search is not None:  # jeżeli coś znalazł wypisz to
            return try_search
        else:   # przeciwnym wypadku użyj wyszukiwania zaawansowanego
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
             ":", '"', ":"}

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
        index_str_1 = 1
        while index_str_1 <= self.len_word:
            word_to_find = ""
            word_to_find = word_to_find.join(self.lst_unknown_word)
            word_to_find = word_to_find[0:self.len_word - index_str_1]
            if word_to_find == "":
                break
            result = search_intents(word_to_find)
            index_str_1 += 1
            if result is not None:
                return result

        # szukanie słowa od lewej do prawej
        index_str_2 = 1
        for i in range(0, self.len_word):
            word_to_find = ""
            word_to_find = word_to_find.join(self.lst_unknown_word)
            word_to_find = word_to_find[index_str_2:]
            if word_to_find == "":
                break
            result = search_intents(word_to_find)
            index_str_2 += 1
            if index_str_2 > self.len_word:
                break
            if result is not None:
                return result

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
                result = search_intents(lst_1)
                if result is not None:
                    return result
            odcinanie_od_lewa += 1
            lst_1 = lst_1.join(self.lst_unknown_word)
            lst_1 = lst_1[odcinanie_od_lewa:odcinanie_od_prawa]
            if lst_1 == "":
                break
            else:
                result = search_intents(lst_1)
                if result is not None:
                    return result


if __name__ == "__main__":
    Chat()
