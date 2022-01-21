from math import floor
from msilib.schema import SelfReg
from random import random
import random

class Snail :
    def __init__(self, name, number, motivation, miles) :
        self.__snailName = name
        self.__snailNumber = number
        self.__snailMotivation = motivation
        self.__snailMiles = miles

    def getName(self):
        return self.__snailName

    def getNumber(self):
        return self.__snailNumber

    def getLook(self) :
        return self.__snailMotivation

    def getMiles(self) :
        return self.__snailMiles

    def sleep(self) :
        up = random.randint(1, 6)
        while(self.__snailMotivation + up <= 6) :
            self.__snailMotivation += up
        else :
            self.__snailMotivation = 6
        return self.__snailMotivation

    def advance(self) :
        self.__snailMiles += self.__snailMotivation
        low = random.randint(1, 6)
        while (low <= self.__snailMotivation) :
            self.__snailMotivation -= low
        return self.__snailMiles

    def race(self) :
        for i in range(self.__snailMiles - 1) :
            print("_", end="")
        print(self.__snailNumber, end="")
        for i in range(19 - self.__snailMiles) :
            print("_", end="")
        print("")

playerList = []

players = int(input("Combien d'escargots vont faire la course ? : "))
for i in range(players) :
    player = input("Choisissez le nom de l'escargot : ")
    playerList.append(player)
for i in range(players) :
    playerList[i] = Snail(playerList[i],"@" + str(i), random.randint(1, 6), 0)
victoire = False
choix = 0
print("Voici les participants : ")
for i in range(players) :
    print(playerList[i].getName() + " = " + playerList[i].getNumber())
choixJ = input("Selon vous, quel escargot va gagner ? (tapez le chiffre) : ")

while (victoire == False) :
    for i in range(players) :
        playerList[i].race()
    for i in range(players) :
            choixList = [1, 2]
            if(playerList[i].getLook() == 6) :
                choix = random.choices(choixList, weights=(80, 20))
            elif(playerList[i].getLook() == 5) :
                choix = random.choices(choixList, weights=(70, 30))
            elif(playerList[i].getLook() == 4) :
                choix = random.choices(choixList, weights=(60, 40))
            elif(playerList[i].getLook() == 3) :
                choix = random.choices(choixList, weights=(50, 50))
            elif(playerList[i].getLook() == 2) :
                choix = random.choices(choixList, weights=(40, 60))
            elif(playerList[i].getLook() == 1) :
                choix = random.choices(choixList, weights=(30, 70))
            if(playerList[i].getLook() <= 0) :
                choix = 2
                print("L'escargot " + playerList[i].getName() + " n'a pas d'autre choix que de se reposer")
            else :
                print("L'escargot " + playerList[i].getName() + " fait un choix")
            if(choix == [1]) :
                playerList[i].advance()
                print("L'escargot " + playerList[i].getName() + " décide d'avancer")
            else :
                playerList[i].sleep()
                print("L'escargot " + playerList[i].getName() + " décide de se reposer")
            if(playerList[i].getMiles() >= 19) :
                victorieux = playerList[i]
                victoire = True

if(victoire == True) :
    print("Il semblerait que " + victorieux.getName() + " a remporté cette course d'escargot !")
    if("@" + str(choixJ) == victorieux.getNumber()) :
        print("Vous avez remportez votre pari bravo !")
    else :
        print("Vous avez pariez sur le mauvais escargot l'ami")
