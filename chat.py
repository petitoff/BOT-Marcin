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
        self.zamiana_polskich_liter_2()

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

        self.lst_unknown_word = txt_translate_msg.split()


if __name__ == "__main__":
    Chat()
