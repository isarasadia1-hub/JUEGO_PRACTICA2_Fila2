#Bienvenidos a la clase de programación orientada a objetos. En esta clase, vamos a crear un juego de rol simple utilizando clases y objetos en Python. El juego consistirá en personajes que pueden atacar, defenderse y subir de nivel. Cada personaje tendrá atributos como fuerza, vida, nivel, puntería, magia, resistencia, velocidad e inteligencia.

#-------------------CLASE PERSONAJE------------------#

#Tenemos que tener en cuenta que la clase personaje será la clase madre y que sus atributos serán los mismos para todas las demás clases que generemos.
#Dicho esto, comenzaremos con 4 atributos básicos para la clase personaje: nombre, fuerza, vida y nivel. Además, cada personaje tendrá atributos adicionales como puntería, magia, resistencia, velocidad e inteligencia, que se mejorarán al subir de nivel.
#Inicializaremos las variables de cada personaje con valores predeterminados cómo por ejemplom la vida será 100 puntos y todos los personajes comenzarán en un nivel 1
#Cada personaje tendrá métodos para atacar, defenderse y subir de nivel. El método de ataque calculará el daño causado al enemigo en función de la fuerza del personaje y su nivel, mientras que el método de defensa permitirá al personaje recuperar vida en función de su fuerza. El método de subir de nivel aumentará los atributos del personaje en un 5% adicional cada vez que suba de nivel.

class personaje:
    
    def __init__(self, nombre, fuerza, vida=100, nivel=1):    
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = vida
        self.nivel = nivel

#------------------MÉTODOS DE LA CLASE PERSONAJE------------------#
#Estos métodos serán heredados por las clases guerrero, arquero, mago y ladrón, pero cada clase tendrá un atributo adicional que mejora en un 10% al pertenecer a esa clase. Por ejemplo, el guerrero tendrá un atributo de resistencia que se mejora en un 10%, el arquero tendrá un atributo de puntería que se mejora en un 10%, el mago tendrá un atributo de magia que se mejora en un 10% y el ladrón tendrá un atributo de inteligencia que se mejora en un 10%.


#-------------------MÉTODOS DE LA CLASE PERSONAJE------------------#

#-------------------Funciones de ataque, defensa y subir de nivel------------------#
#Tenemos que tener en cuenta que un personaje sólo podrá atacar a otro si tiene al menos 1 punto de vida, y su contrincante tiene más de 0 puntos de vida.
#En ese caso, ccada vez que nuestro personaje ataque, infligirá una cantidad de daño proporcional a su fuerza y nivel, y el enemigo perderá esa cantidad de vida. Si la vida del enemigo llega a cero o menos, el enemigo será derrotado.

    def atacar(self, enemigo):
        if self.vida <= 0:
            print(f"{self.nombre} no puede atacar porque está derrotado.")
            return

        if enemigo.vida <= 0:
            print(f"{enemigo.nombre} ya está derrotado.")
            return

        daño = self.fuerza * self.nivel
        enemigo.vida -= daño
        print(f"{self.nombre} ataca a {enemigo.nombre} causando {daño} de daño.")

        if enemigo.vida <= 0:
            enemigo.vida = 0
            print(f"{enemigo.nombre} ha sido derrotado por {self.nombre}.")
        
    def defenderse (self):
        if self.vida <= 0:
            print(f"{self.nombre} no puede defenderse porque está derrotado.")
            return

        defensa = self.fuerza * 0.5
        self.vida += defensa
        print(f"{self.nombre} se defiende y recupera {defensa} de vida.")

#Cada vez que un personaje deje a 0 la vida de su enemigo, subirá de nivel y mejorará sus habilidades. Para esto, podemos agregar un método adicional en la clase personaje que permita al personaje subir de nivel y mejorar sus atributos en un 5% adicional cada vez que suba de nivel.
    def subir_nivel(self):
        self.nivel += 1
        self.fuerza += 5
        self.vida += 20
        self.punteria += self.punteria * 0.05
        self.magia += self.magia * 0.05
        self.resistencia += self.resistencia * 0.05
        self.velocidad += self.velocidad * 0.05
        self.inteligencia += self.inteligencia * 0.05
        print(f"{self.nombre} ha subido al nivel {self.nivel}. Fuerza: {self.fuerza}, Vida: {self.vida}, Puntería: {self.punteria}, Magia: {self.magia}, Resistencia: {self.resistencia}, Velocidad: {self.velocidad}, Inteligencia: {self.inteligencia}")

#Cada vez que un personaje ataca a otro, se deben mostrar las vidas de ambos personajes después del ataque. Para esto, podemos agregar un método adicional en la clase personaje que muestre la vida actual del personaje.

    def mostrar_vida(self):
        print(f"{self.nombre} tiene {self.vida} de vida.")


# Ejemplo de uso
#Si el guerrero derrota a un enemigo, sube de nivel y mejora sus habilidades.
#Si la vida del guerrero llega a cero, no puede atacar ni defenderse.
#cuando el guerrero ataca, el daño causado se calcula multiplicando su fuerza por su nivel, y se resta de la vida del enemigo.
#cuando el un guerrero ataca a otro, si el enemigo ya está derrotado, no se puede atacar.
#Cada vez que un guerrero ataca y el otro se defiende, el guerrero defensor recupera vida en función de su fuerza.
#cuando un guerrero ataca a otro, se deben mostrar las vidas de ambos guerreros después del ataque.
#Ambos guerreros comienzan con 100 de vida, pero pueden aumentar su vida al subir de nivel o al defenderse.
#Cada guerrero tiene un nombre único y una clase

guerrero1 = personaje("Thor", 20)
guerrero2 = personaje("Loki", 15) 

#Vamos a hacer un bucle de ataque entre dos guerreros para probar el funcionamiento de los métodos de ataque, defensa y subir de nivel.
while guerrero1.vida > 0 and guerrero2.vida > 0:
    guerrero1.atacar(guerrero2) 
    guerrero1.mostrar_vida() 
    guerrero2.mostrar_vida() 
    guerrero2.defenderse() 
    guerrero2.mostrar_vida() 
    if guerrero2.vida <= 0:
        break
   
if guerrero2.vida <= 0:
        guerrero1.subir_nivel() 
        guerrero2 = personaje("Loki", 15)  # Reiniciar enemigo

#En este caso, tenemos el ejemplo de que el guerrero1 ataca al guerrero2, y el guerrero2 se defiende. Si el guerrero2 es derrotado, el guerrero1 sube de nivel y mejora sus habilidades. Luego, el guerrero2 se reinicia para continuar la batalla.
#Intentemos hacer que ambos guerreros ataquen y defiendan en un bucle hasta que uno de ellos sea derrotado. De esta manera, podremos ver cómo funcionan los métodos de ataque, defensa y subir de nivel en acción.

while guerrero1.vida > 0 and guerrero2.vida > 0:
    guerrero1.atacar(guerrero2) 
    guerrero1.mostrar_vida() 
    guerrero2.mostrar_vida() 
    if guerrero2.vida <= 0: 
        break 
    guerrero2.atacar(guerrero1) 
    guerrero2.mostrar_vida() 
    guerrero1.mostrar_vida() 
    if guerrero1.vida <= 0: 
        break