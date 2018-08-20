#!/usr/bin/python
# -*- coding: utf-8 -*-

class Kanin:
    def __init__(self, name):
        self.name = name

    def set_carrot(self,carrot):
        self.carrot = carrot

    def __str__(self):
        return "🐰: Hej, Jag är " + self.name + ' tokki🍀 Oj! du gav mig '+ '🥕'*int(self.carrot)+"! Tack💕)"

    def set_name(self, name):
        self.name = name

namn = input("Vad heter din kanin?")
carrot = input("Hur många carrot vill du ge till?")
tokki = Kanin(namn)
tokki.set_carrot(carrot)
print(tokki)

tokki.set_name(namn+'\'s Mamma')
print(tokki)
tokki.set_name(namn+'\'s Pappa')
print(tokki)
