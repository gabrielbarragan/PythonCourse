#obtener solo los números impares de una lista de números

my_number_list= [1,4,5,6,9,12,20,34,19,21]

#solución con list comprehensions
odd=[i for i in my_number_list if i%2 != 0]
print(odd)

print('-------------')
#solución con filter
odd2= list(filter(lambda x: x % 2 != 0 , my_number_list))
print(odd2)
