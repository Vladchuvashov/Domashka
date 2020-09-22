print("Введите альфа:")
alfa=float(input())
chas=alfa//30
minute=alfa % 30 * 2
sec=alfa% 0.5 * 120
print ("C начала суток прошло "+str(int(chas))+" полных часов "+str(int(minute))+" полных минут и "+str(int(sec))+" полных секунд :3")