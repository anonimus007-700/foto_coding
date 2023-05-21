from random import randint

class Coder:
    def text_to_cod(text):
        coding_text = []
        out_list = []
        for i in text:
            coding_text.append(str(ord(i)))
        for i in coding_text:
            out_list.append(bin(int(i))[2:])
        return out_list


class Decoder:
    def int_to_text(number):
        coding_text = []
        int_text = []
        for i in number:
            int_text.append(int(i, 2))
        for i in int_text:
            coding_text.append(chr(int(i)))
        
        coding_text = [item for item in coding_text if item != '\x00']
        return coding_text
