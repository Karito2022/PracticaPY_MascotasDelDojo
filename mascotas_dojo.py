class Mascota:

    # implementa __init__( name , type , tricks ):
    def __init__(self, name , type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    # implementa los siguiente metodos
    # dormir() - aumenta la energía de las mascotas en 25
    def dormir(self):
        self.energy += 25
        return self

    # comer() - aumenta la energía de la mascota en 5 y la salud en 10
    def comer(self):
        self.energy += 5
        self.health += 10
        return self

    # jugar() - aumenta la salud de la mascota en 5
    def jugar(self):
        self.health += 5
        self.energy -= 15
        return self

    # ruido() - imprime el sonido de la mascota
    def ruido(self):
        print(self.ruido)



class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # implementar los siguientes metodos
    # caminar() - pasea a la mascota del ninja invocando el método pet play()
    def pasear(self):
        self.pet.jugar()
        return self

    # alimentar() - alimenta a la mascota del ninja invocando el método pet eat()
    def alimentar(self):

        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.comer()
        else:
            print("Oh no!!! necesitas más comida para mascotas!")
        return self

    # bañar() - limpia la mascota del ninja invocando el método pet noise()
    def bañar(self):
        self.pet.ruido()

mis_golosinas = ['Snausage','Bacon',"Trash Bag"]
mi_comida_para_mascota = ['Pizza','Hamburguesa']

nibbles = Mascota("Mr. Nibbles","Horse",['nibbles on things','is invisible'],"Hey Hey")

adrien = Ninja("Adrien","Dion",mis_golosinas,mi_comida_para_mascota, nibbles)

adrien.alimentar();
adrien.alimentar();
adrien.alimentar();
