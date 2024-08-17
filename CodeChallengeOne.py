numbers = []

while True:
    array = input("Introduce un número o presiona 'q' para salir: ")    
    if array.lower() == 'q':                # Q or q, it's ok
        print("Saliendo del bucle.")
        break 
    if array.isdigit():                     # Is the number valid?
        numbers.append(int(array)) 
    else:
        print("Entrada no válida. Por favor, introduce un número o 'q' para salir.")

print("Números ingresados:", numbers)

allowedNumbers = '0123'
selectedNumbers = []

for i in numbers:
    toString = str(i)
    newNumber = ''
    for j in toString:
        if j in allowedNumbers:
            newNumber += j

    if newNumber:
        selectedNumbers.append(int(newNumber))

print(selectedNumbers[::-1])
