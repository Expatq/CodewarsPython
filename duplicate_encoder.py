def duplicate_encode(word):
    return "".join(["(" if word.lower().count(x) == 1 else ")" for x in word.lower()])
    
print(duplicate_encode("UJMKcDdsnkfLViMqKMBFQ)cr(!xi"))


'''new_word = word
    for i in word:
        checked_letter = i
        for j in word[word.find(i)+ 1:len(word)]:
            if (checked_letter == j):
                new_word = new_word.replace(j, ')')
            else: 
                new_word = new_word.replace(j, '(')
    return new_word
    
    def duplicate_encode(word):
    temp_lst = list(word.lower())
    for i in range(temp_lst.len()):
        map_dict = 
    
    '''
