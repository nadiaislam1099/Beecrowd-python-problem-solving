a,b,c = input().split()
greatest = (int(a) + int(b) + abs(int(a)-int(b)) )//2
greatest = (greatest + int(c) + abs(greatest - int(c))) //2
print(greatest , "eh o maior")