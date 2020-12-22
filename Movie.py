from colorama import Fore, Back, Style

banner = Fore.RED + Style.BRIGHT + """

███╗░░░███╗░█████╗░██╗░░░██╗██╗███████╗
████╗░████║██╔══██╗██║░░░██║██║██╔════╝
██╔████╔██║██║░░██║╚██╗░██╔╝██║█████╗░░
██║╚██╔╝██║██║░░██║░╚████╔╝░██║██╔══╝░░
██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░██║███████╗
╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚══════╝
—·– t.me/ohtllinest | Поиск фильмов –·—
""" + Style.RESET_ALL

line = Fore.RED + """
————————————————————————————————————————————————
"""

js_banner = """
[1] Начать поиск
[2] Инструкция
"""
js_inst = """
— 1. Зайдите на сайт КиноПоиска и выберите фильм который хотите посмотреть
— 2. В адресной строке браузера появится номер фильма (film/номер)
— 3. Введите номер фильма и вы получите ссылку на данный фильм
"""

print (banner)
print (' ')
print (js_banner)

js_name = input ("— Введите номер функции : ")
if js_name == "1":
	js_fore = input ("— Введите идентификатор фильма : ")
	print (' ')
	print (line)
	print ('— Ссылки на фильм:')
	print ("https://sskinopoisk.ru/film/" + js_fore)
	print ("https://ww1.flink.su/film/" + js_fore)
	print (line)

if js_name == "2":
	print (line)
	print (js_inst)
	print (line)
