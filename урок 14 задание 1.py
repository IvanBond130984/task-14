def f(ls, i):
    if i==len(ls):
        print('Конец списка')
        return
    else:
        print(ls[i], end=' ')
        r=i+1
        return f(ls, r)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
n=0
f(my_list, n)