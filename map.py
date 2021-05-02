#obtener el cuadrado de los números de una lista

my_number_list= [1,4,5,6,9,12,20,34,19,21]

#solución con list comprehensions
square=[i**2 for i in my_number_list ]
print(square)

print('-------------')
#solución con filter
square2= list(map(lambda x: x**2 , my_number_list))
print(square2)
