from xml.etree.ElementTree import tostring

goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'}, {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
def field(items, *args):
    # print(args[1])
    answer = ""
    if len(args) == 1:
        for i in range(0,len(goods)):
         if args[0] in goods[i]:
             answer += goods[i][args[0]] + ","
        print(answer[:len(answer)-1])
    else:
        answer = ""
        for i in range(0, len(goods)):
            for j in range(0,len(args)):
                if args[j] in goods[i]:
                    answer += ", " + "'" + args[j] + "'" + ":" + " '" + str(goods[i][args[j]]) + "'"
        print("{" + answer[2:] + "}")
    assert len(args) > 0

field(goods, "title", "price")