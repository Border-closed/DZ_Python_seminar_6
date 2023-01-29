# Задача 4
# Пользователь вводит число N. 
# Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.

N=int(input('Введите количество друзей '))
friends=[]
names=[]
for i in range(0,N):
    fr={}
    name=input(f'Введите имя {i+1} друга ')
    age=input(f'Введите возраст {name} ')
    names.append(name)
    fr[name]=age
    friends.append(fr)
print(f'Список друзей и их возрастов: {friends}')
sum_age=0
for i in range(len(friends)):
    sum_age=sum_age+int(friends[i].get(names[i]))
print(f'Средний возраст друзей {sum_age/N}')
key=[]
for i in range(len(friends)):
    for k in friends[i].keys():
        key.append(k)
key.append('')
print(max(key, key=len))