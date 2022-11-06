n1 = int(input("Введите целое число: "))
n2 = 0
while n1 > 0:
   
    digit = n1 % 10
    
    n1 = n1 // 10
    
    n2 = n2 * 10
   
    n2 = n2 + digit
def pre():
    print(n2)
    a=int(input('ведите что вы хотете сделать? \n 1)* 2)/ 3)+ 4)- \n ответ:'))
    n3=int(input('ведите второе число:'))
    if a==1:
        n4=n2*n3
        print(f'вот что получилось {n4}')
    elif a==2:
        n4=n2/n3
        print(f'вот что получилось {n4}')
    elif a==3:
        n4=n2+n3
        print(f'вот что получилось {n4}')
    elif a==4:
        n4=n2-n3
        print(f'вот что получилось {n4}')
    else:
        print('нет такокой задачи')
pre()  


