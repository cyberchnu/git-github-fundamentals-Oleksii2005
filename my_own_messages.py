

sec = 60
hours = 60
hours_per_day = 24

seconds_per_hour = (sec * hours)
seconds_per_day = (seconds_per_hour * hours_per_day)

print( str(seconds_per_hour) + ' - seconds per hour ' '\n' + str(seconds_per_day) + ' - seconds per day' )
print( str(seconds_per_day // seconds_per_hour) )

print(3 + 9)
print(17 - 5)
print(4 * 3)
print(24 // 2)

my_favorite_num = 30
name = 'Oleksii'

print(my_favorite_num)
print(name)

poem = '''Yes, I'll smile, indeed, through tears and weeping
Sing my songs where evil holds its sway,
Hopeless, a steadfast hope forever keeping,
I shall live! You thoughts of grief, away!'''

print(poem[0:15])

print(len(poem))



print(poem.startswith('Yes'))

print(poem.endswith('I shall live!'))

print(poem.find(','))

print(poem.rfind(','))

print(poem.count(','))

print(poem.isalnum())

# Задачі

name = 'Sasha'
programming_language = 'Python'

print('Hello, '+ name + ', would you like to learn some ' + programming_language+ ' today?')

famous_person = 'Steve Jobs'
message = "\"Your time is limited, so don't waste it living someone else's life. \nDon't be trapped by dogma – which is living with the results of other people's thinking.\""

print(famous_person +', once said, ' + message)

name = '****Oleksii****'

print(name.strip('*'), '\n'+ name.lstrip('*'), '\t'+ name.rstrip('*'))

print('Oleksii Kaba' '\n' 'Ukraine' '\n' 'Chernivtsi' '\n' '58004' '\n' 'Center' '\n' 'st. Holovna' '\n' '81')

print('{meters} {inches} {ft} {miles} {yards}'.format(meters='1m = ',inches='39.37 inch,', ft = '3.28 ft,', yards='0.91 yards', miles ='1609.34 metres in on mile,'))

# days = 7
# hours = 168
# minutes = 10.080
# seconds = 604.800

# print(float(minutes))

# print(rjust(40)(days, float(hours), float(minutes), seconds))

C = 10
F = 32 + 9/5 * C
K = C + 273,15

print(f'{K}')
print(F'{F}')

name = input("What's your name?: ")
print("Hello " + name)


# This is my homework 02.02.23 - 16.02.23