'''1. Пусть пользователь вводит логин и пароль для регистрации. Напишите функцию 
которая принимает логин и пароль в качестве аргументов и записывает в json файл.
2. Добавьте к вашей функции проверку на то, существует ли данный 
пользователь в системе.
3. Напишите функцию для входа пользователей в систему. Функция должна
проверять на правильность логин и пароль, которые записаны в json файл.'''

import json


data={'Dmitrii':'qwerty','Nikolai':'zsxdc','Vika':'aqwexa34'}
with open ('m3l4.json','r') as file:
	data=json.load(file)
def regist(login,password):
	data[login]=password
	
while True:
	moving_forvard=input('Moving forvard?: (y or n).(look dictionary enter d) ')
	if moving_forvard=='y':
		login=input("Login: ")
		password=input("Password: ")
		if (login,password) not in data.items():               # Проверка на наличие ключ:значение в словаре
			regist0=input("Login does not exist. Register? y or n?")  # Предложение зарегистрироваться в системе в случае отсутствия пользователя в словаре
			if regist0 == 'y':
				login=input('Your login: ')              # Регистрация
				password=input('Your password: ')
				if login in data.keys():                 # Проверка на наличия данного ключа в словаре чтобы не перезаписать значение
					print ('Login exist')
					continue
				regist(login,password)                   # Запись в словарь ключа и значения при успешной проверке
				print('Welcome',login)
				with open ('m3l4.json','w') as file:     # Запись нашего словаря в json файл
					json.dump(data,file)
			else:
				print ('good buy')	
		else:
			print ("Welcome ",login)
	elif moving_forvard=='d':                            # Просмотр словаря в системе
		print (data)
	else:
		print ('Good buy')
		break
