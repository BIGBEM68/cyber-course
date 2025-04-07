def palyndrome(sentence):
    sentence=sentence.strip()
    if sentence[::]==sentence[::-1]:
        return True
    return False

def find_palyndromes(list):
    paly_list=[]
    for item in list:
        if palyndrome(item):
            paly_list.append(item)
    return paly_list

words_list=['radar' , 'apple', 'level','banana','stats','noon']
print(find_palyndromes(words_list))

    

