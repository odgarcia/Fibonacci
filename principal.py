def fibonacci(n):

   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
# Cambiar el numero de cantidad por un numero entero positivo
cantidad = 10
for i in range(cantidad):
   print(fibonacci(i))