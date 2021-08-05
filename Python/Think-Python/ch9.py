# kapitell 9

fin=open('words.txt')

def read_word(document):
    line=document.readline()
    word=line.strip()
    print(word)

# hvor mange ord i det engelske språk har mer enn 20 bokstaver?
# for word in fin:
#     if len(word)>20:
#         print(word)
#     else:
#         pass




# l_in_word: string -> *string
# prints letters in a word

def l_in_word(w):
    num_l=len(w)
    for l in range(0,num_l):
        print(w[l])

# has_no_e: string -> boolean
# takes a string en determines if the string has a letter "e" in it
# denne gir feil resultat!!

# def has_no_e(word):
#     num_letters=len(word)
#     for index in range(0,num_letters):
#         if word[index]=="e":
#             return False
#         else:
#             return True

def has_no_e(w):
    for l in w:
        if l=='e':
            return False
    return True

# assert has_no_e('abc')==True
# assert has_no_e('dedf')==False


# lines_in_doc: document -> integer
# counts the number of lines (words in this case) in a document
# fin har 113783

def lines_in_doc(document):
    counter=0
    for lines in document:
        counter+=1
    return counter

# words_wo_e: document -> integer
# counts words withough the letter 'e'
# call to function has_no_e in process
# antall ord uten 'e': 109419
# 0.0383537083747133
def words_wo_e(document):
    counter=0
    for word in document:
        if has_no_e(word)==True:
            counter+=1
        else:
            pass
    return counter

