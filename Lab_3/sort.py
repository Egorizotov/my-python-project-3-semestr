def sort1(data):
    sortedd = sorted(data, key=None, reverse=True)
    return sortedd

def  sort2(data2):
    answer = str(input("По какому параметру вы хотите сортировать?"))
    sortedd = sorted(data2, key= lambda data2: data2[str(answer)], reverse=True)
    return sortedd