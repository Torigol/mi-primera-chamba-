opcion=1
#En un ciclo while realiza operaciones hasta que el usuario escriba 0
while opcion!=0:
    num1=int(input("ingresa el primer numero "))
    num2=int(input("ingresa el segundo numero "))
    print("Ingresa 1. sumar")
    print("Ingresa 2. resta")
    print("Ingresa 3. multiplicar")
    print("Ingresa 4. dividir")
    op=int(input("Que operacion quieres hacer con esos numeros? "))
    if(op==1):
        sum=num1+num2
        print("la suma de los numeros es: ", sum)
    elif(op==2):
        res=num1-num2
        print("la resta de los numeros es: ", res)
    elif(op==3):
        mult=num1*num2
        print("la multiplicacion de los numeros es: ", mult)
    elif(op==4):
        div=num1/num2
        print("la divicion de los numeros es: ", div)


    else:
        print("no valido")
    opcion=int(input("deseas continuar?, si no preciona 0. para salir"))    