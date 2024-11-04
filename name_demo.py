 # kittybot/name_demo.py

 # Хотели импортировать только эту функцию
def simple_add(a, b):
    return a + b

 # Но в момент импорта выполнился и этот код:
print(simple_add(2, 2))
print(__name__)