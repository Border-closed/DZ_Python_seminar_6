#Задача 3
# Пользователь вводит число N - количество друзей. 
# Затем он вводит личные данные (имя и возраст) для N друзей.  
# Создайте список Friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего и выведите его имя

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
age=[]
for i in range(len(friends)):
    age.append(int(friends[i].get(names[i])))
age_num=list(enumerate(age,0))
age_min_v=min(age_num, key=lambda i: i[1])
print(f'Минимальный возраст {min(age)} у друга {names[age_min_v[0]]} ')