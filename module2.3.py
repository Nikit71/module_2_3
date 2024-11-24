# Домашняя работа по уроку " Стиль кода. Цикл While. 1.2 "
# Задача " Нули ничто. отрицание недопустимо!"
my_list=[42,69,322,13,0,99,-5,9,8,7,-6,5]
print("\nИмеем список\n",my_list,"\n")
indx=0
while indx < len(my_list):
    if my_list[indx] < 0:
        break
    elif my_list[indx] != 0:
        print (my_list[indx])
    indx=indx+1
print("\nСписок проверен")
# Задание выполнено