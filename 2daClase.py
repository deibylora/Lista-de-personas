invitados = [
["Deiby", "Mirian", "Josue"],
["Carmen", "Clarissa", "Angel"],
["Nata", "Noel", "Jeni"]
]

i=0

while i < 5:
    fila = int(input("Inserta la linea: "))
    columna = int(input("Inserta la columna: "))



    if fila <= 2 and columna <= 2:
        print (str(invitados[fila] [columna]))
    else:
        print ("Por favor inserte un numero menor al 2")

i+=1
