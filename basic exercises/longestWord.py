
def find_longest_word(list):
    longest=['']
    for word in list:
        if len(word)>len(longest[-1]):
            longest=[word]
        elif len(word)==len(longest[-1]):
            longest.append(word)
    return longest
   

words_list= ['apple','banana','orange','strawberry','pineapple','kiwi']
print(find_longest_word(words_list))
