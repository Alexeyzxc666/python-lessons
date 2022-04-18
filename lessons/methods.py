#upper() lower() count(cчетчик) find(найти символ) rfind() index(найти номер индекса)  rjust() and ljust(10, ?) join(имя списка)
#split(знак разделения - пробел (по умолчанию))
#len(object.split('text'))
#strip(удаляет пробелы и переносы \n)
#метод можно применять к инпуту s=input().upper()

#метод не меняет строку

#1.
#replace(old, new)
address = '1.1.1.1'
print(address.replace('.', '[.]'))

#2.
#split()
x = 'Hello world'
s = len(x.split())
print(s)

#3
name = input()
nam = name.replace('!','')
print(nam)

#4
x = list(input()) # можно без лист
s = '*'.join(x)
print(s)

#5
name = input()
x = name[0].upper()
m = name.replace(name[0], x)
print(m)

#6
enter = input().lower()
x = enter.replace('o', '').replace('a', '').replace('u', '').replace('e', ''). replace('i', '').replace('y', '')
s = '.'.join(x)
print('.'+s)


