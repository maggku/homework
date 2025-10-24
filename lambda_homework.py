#Zamień te f-ncje na lambdy:
#
#print(square(4)) # 16
#print(absolute(-7)) # 7
#print(even_or_odd(5)) # nieparzysta
#print(even_or_odd(10)) # parzysta

#Przykład:
#print(lambda x: x **2)

#print((lambda x: x ** 2)(4))
#print((lambda x: )(-7))
#print((lambda x: "parzysta/even" if x % 2 == 0  else "nieparzysta/odd" (5))
#print((lambda x: x ** x)(10))

square = lambda x: x ** 2
print(square(4))

absolute = lambda x: abs(x)
print(absolute(-7))

even_or_odd = lambda x: "parzysta/even" if x % 2 == 0 else "nieparzysta/odd"
print(even_or_odd(5))
print(even_or_odd(10))
