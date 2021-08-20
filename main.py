#Перед началом работы надо установить доп. модуль
#Это делается командой в терминале:
#pip3 install colorama

#Импортируем нужные модули
from colorama import init
from colorama import Fore, Back

#Эта команда нужна для работы модуля
init()

#Выводим текст разных цветов
print(Fore.RED + 'Красный текст.')
print(Fore.GREEN + 'Зелёный текст.')
print(Fore.BLUE + 'Синий текст.')
print(Fore.YELLOW + 'Жёлтый текст.')



#Выводи пробел
print('        ')
print('        ')
print('        ')

#Выводим текст с разным фоном
print(Back.RED + 'Красный текст.')
print(Back.GREEN + 'Зелёный текст.')
print(Back.BLUE + 'Синий текст.')
print(Back.YELLOW + 'Жёлтый текст.')

#Спасибо
#Подпишись ;)