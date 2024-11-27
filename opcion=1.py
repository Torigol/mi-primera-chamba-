opcion=1
print("bienvenido al programa")
while opcion!=0:

    print("Ingresa 1. area de triangulo")
    print("Ingresa 2. area del rectangulo")
    print("Ingresa 3. area del circulo")
    print("Ingresa 4. convertir temperatura F a C")
    print("ingresa 5. convertir temperatura C a F")
    op=int(input("Que operacion quieres hacer con esos numeros? "))
    if(op==1):
        base=int(input("Ingresa la base: "))
        altura=int(input("ingresa la altura: "))
        areat=base*altura/2
        print("el area es: ", areat)
    elif(op==2):
        base=int(input("Ingresa la base: "))
        altura=int(input("ingresa la altura: "))
        arear=base*altura
        print("el area es: ", arear)
    elif(op==3):
        radio=int(input("ingresa el radio: "))
        areac=3.14*radio*radio
        print("el area es: ", areac)
    elif(op==4):
        fahrenheit=int(input("ingresa los grados fahrenheit: "))
        cel=(fahrenheit-32)*5/9
        print("la convercion de F a C ES: ", cel)
    elif(op==5):
        celsius=int(input("ingresa los grados celsius: "))
        fare=(celsius*9/5)+32
        


    else:
        print("no valido")
    opcion=int(input("deseas continuar?, si no preciona 0. para salir"))    
    



