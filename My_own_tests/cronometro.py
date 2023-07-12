# Um cronometro em python

import os
import time


class Cronometro:

    def __init__(self, hora, minutos, segundos):
        self.hora = hora
        self.minutos = minutos
        self.segundos = segundos

    def __repr__(self):
        return f"{self.hora:02d}:{self.minutos:02d}:{self.segundos:02d}"

    def increase(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.hora += 1

    def execute(self):
        while True:
            os.system('cls')
            print(self)
            self.increase()
            time.sleep(1)


cronometro = Cronometro(0, 0, 0)
cronometro.execute()
