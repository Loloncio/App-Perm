import os

class Ayuda():

    def __init__(self):
        self.tutorial = []
        ruta_ayuda = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./Ayuda.txt")
        with open(ruta_ayuda, encoding="utf8") as file:
            for line in file:
                c1 = line[0]
                elemento = []
                if c1 == ">":
                    elemento.append(line[1:])
                    elemento.append(3)
                elif c1 == "<":
                    elemento.append(line[1:])
                    elemento.append(2)
                else:
                    elemento.append(line)
                    elemento.append(1)
                self.tutorial.append(elemento)
    def getTutorial(self):
        return self.tutorial