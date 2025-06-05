def generator(sentence):
    
    word_list = sentence.title()
    word_list = word_list.split()

    short_form = ''
    for i in word_list:
        short_form = short_form + i[0]
    print(short_form)

text = str(input("enter senetnce: "))
generator(text)