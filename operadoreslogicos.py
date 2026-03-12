# Tablas de verdad de compuertas logicas ADN, OR Y NOT 
def AND(a,b):
  return int(a and b)
def OR(a,b):
  return int(a or b)
def NOT(a):
  return int(not a)
print("Tabla de verdad AND")
print("A B | A AND B")
for A in [0,1]:
  for B in[0,1]:
    print (A,B, "|" , AND (A,B))
print("Tabla de verdad OR")
print("A B | A OR B")
for A in [0,1]:
  for B in[0,1]:
    print (A,B, "|", OR (A,B))
print("Tabla de verdad NOT")
print("A B|A NOT B")
for A in [0,1]:
  print (A, "|" ,NOT (A))
