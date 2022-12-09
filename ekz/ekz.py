f = open("text.txt", "rt")
enterNum = int(input("Введіть число AAA: "))


for i in f:
    x = i.find(" ")
    x += 1
    y = ''
    for i2 in range(x, len(i)-1):
        y += i[i2]
    y = int(y)
    if y > enterNum and y != enterNum:
        print(i[0:x])
    else:
        print("Це значення більше або дорівнює значенню в файлі")

    
          
            
            
            
            
            
            
            



