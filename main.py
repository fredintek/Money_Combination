alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caeser(text, shift, direction):
    new_list_shifted = alphabet_list[int(shift):]
    for i in alphabet_list[:int(shift)]:
        new_list_shifted.append(i)

    if direction.lower() == 'encode':
    #To encode!!
        encrypted_word = ''
        word = text.lower()
        for i in word:
            if i != ' ':
                num = alphabet_list.index(i)
                encrypted_word += new_list_shifted[num]
            else:
                encrypted_word += ' '
        print(f"The Encoded message is --> {encrypted_word}")

    elif direction.lower() == 'decode':
    #To Decode!!
        encrypted_word = ''
        word = text.lower()
        for i in word:
            if i != ' ':
                num = new_list_shifted.index(i)
                encrypted_word += alphabet_list[num]
            else:
                encrypted_word += ' '
        print(f"The Decoded message is --> {encrypted_word}")

caeser('qnuux fxaum', 9, 'decode')





    
