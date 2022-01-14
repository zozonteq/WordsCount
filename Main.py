words_list = dict()

inp = input()
for i in inp.split(' '):
    i=i.replace('.','').lower()
    if i not in words_list.keys():
        words_list[i] =1
    else:
        words_list[i] +=1
    
print(words_list)
    

