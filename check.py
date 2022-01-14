dic = dict()
while True : 
    print("---------------")
    inp = input().replace(" ","")
    for i in range(len(inp)):
        if inp[i] not in dic.keys():
            dic[inp[i]] = 0
        else:
            dic[inp[i]] += 1
    print(dic)
