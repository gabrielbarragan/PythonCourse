from functools import reduce 

#obtener la suma de todos los números de una lista

my_number_list= [2,2,2,2,2]

#solución con bucle for
multiplied_elements= 1
for i in my_number_list:
    multiplied_elements=multiplied_elements*i
print(multiplied_elements)

print('-------------')
# #solución con reduce
multiplied_elements= reduce(lambda a,b: a*b , my_number_list)
print(square2)
