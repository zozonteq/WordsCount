words_list = dict()
banW = "1234567890!<>().,:;-!?'"

while True:
        print("---------------------")
        inp = input()
        for i in inp.split(' '):
                i=i.lower()
                for j in range(len(banW)):
                    i = i.replace(banW[j],"")
                if i == "": continue
                if i.isascii() is True:
                    if i not in words_list.keys():
                        words_list[i] =1
                    else:
                        words_list[i] +=1
        sorted_words = sorted(words_list.items(), key=lambda x:x[1])
        print(sorted_words)
