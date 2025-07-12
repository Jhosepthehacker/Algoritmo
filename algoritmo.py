def algoritmo(): # Posible error en alguna parte del código
    productos = ["Azúcar", "Sal", "Limón", "Leche"]
    for i in productos:
        print(i)
    user = input("\n¿Qué desea comprar?: ").lower()
    if user == productos[0].lower() or productos[1].lower():
        print("Cuesta 2$")
    elif user == productos[2].lower():
        print("Cuesta 4$")
    elif user== productos[3].lower():
        print("Cuesta 6$")
# En desarrollo

if __name__ == '__main__':
    algoritmo()
