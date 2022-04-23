bases_atacadas = []

bases_totales =  [1,2,3,4,5,6,7,8,9,10]

def attack_base(base):
    print(f"Usted ha conquistado la base: {base} ")
    return base



def menu():

    while True:

        print('''
        \nSeleccione una opcion:
        1.- Atacar una base
        2.- Checar  el progreso
        3.- Salir
        '''
            )
        opcion = int(input())

        if opcion == 1:
            num_base = int(input("Ingrese el numero de base que desea atacar: "))
            while num_base <= 10:
                attack_base(num_base)
                if num_base in bases_atacadas:
                    print("La base ya ha sido atacada")
                else:
                    bases_atacadas.append(num_base)
        if opcion == 2:
            print(f"Su progreso es del {len(bases_atacadas) *100 / len(bases_totales)} % ")
            for i in bases_atacadas:
                print(f"Usted ya ataco la base: {i}")
        elif opcion == 3:
            break
        else:
            print("Ingrese una opcion valida")

menu()