  #EXEMPLOS Expressões Lógicas/Booleanas
#------------------------------
#1
#------------------------------
print("--- TESTE OPERADOR 1 ---")
x = 10
y = 1
res = not x > y
print(res)

#------------------------------
#2
#------------------------------
print("--- TESTE OPERADOR 2 ---")
x = 10
y = 1
z = 5.5
res = (x > y) and (z == y) # True and False
print(res)

#------------------------------
#3
#------------------------------
print("--- TESTE OPERADOR 3 ---")
x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != z / x  #1.55
# res = True or not False and True
# res = True or True and True
# res = True or True
print(res)