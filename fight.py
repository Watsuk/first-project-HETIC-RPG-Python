import kivy
from kivy.app import App

kivy.require('2.0.0')

from kivy.lang import Builder
from kivy.logger import Logger, LOG_LEVELS
from kivy.properties import ObjectProperty, StringProperty, NumericProperty

from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from random import randint

Logger.setLevel(LOG_LEVELS["debug"])
# Logger.setLevel(LOG_LEVELS["info"])

monster_hp = 100
monster_attack = 10
monster_prio = randint(1,3)
character_hp = 100
character_prio = 2
character_attack = 30
monster_can_attack = 0

rapid = {'1':'fast', '2':'normal','3':'slow'}

def saveScore():
    Logger.debug("Read fightscore.txt")
    # écrit le résultat dans un fichier txt
    with open('fightscore.txt', 'w') as f:
        f.write("character_hp " + str(character_hp) + '\n')
        f.write("monster_hp " + str(monster_hp) + '\n')


class Manager(ScreenManager):
    pass

class MenuScreen(Screen):
    def open_fight(self):
        Logger.debug("fight")

class FightScreen(Screen):
    lifehp = NumericProperty(character_hp)
    monsterhp = NumericProperty(monster_hp)
    speed1 = StringProperty()
    speed2 = StringProperty()

    def on_pre_enter(self):
        self.fight()

    def fight(self):
        global monster_hp
        global character_hp
        global monster_prio
        global character_prio
        global character_attack
        global monster_can_attack

        Logger.debug("char_hp:"+str(character_hp))
        Logger.debug("monster_hp:"+str(monster_hp))

        self.lifehp = character_hp
        self.monsterhp = monster_hp
        self.speed1 = rapid[str(character_prio)]
        self.speed2 = rapid[str(monster_prio)]


    def go_fight(self):
        Logger.debug("Attack")

    def open_inventory(self):
        Logger.debug("inventory")

    def open_element(self):
        Logger.debug("Element")

    def back_menu(self):
        Logger.debug("back menu")

class AttackScreen(Screen):
    lifehp = NumericProperty(character_hp)
    monsterhp = NumericProperty(monster_hp)
    speed1 = StringProperty()
    speed2 = StringProperty()

    def on_pre_enter(self):
        self.attack(0)

    def attack(self, num):
        global monster_hp
        global character_hp
        global monster_prio
        global character_prio
        global character_attack
        global monster_can_attack

        if num == 0:
            Logger.debug("char_hp:"+str(character_hp))
            Logger.debug("monster_hp:"+str(monster_hp))

            self.lifehp = character_hp
            self.monsterhp = monster_hp
            self.speed1 = rapid[str(character_prio)]
            self.speed2 = rapid[str(monster_prio)]
            return

        if monster_prio < character_prio:
            if monster_can_attack == 0:
                character_hp -= (randint(1,3) * 10)
            else:
                monster_can_attack -= 1
            if character_hp > 0:
                if num == 1:
                    monster_hp -= character_attack
                    if monster_hp < 1:
                        Logger.debug("Gagné")
                        saveScore()
                        exit()
                elif num == 2:
                    monster_can_attack = 1
                else:
                    character_attack += 10
            else:
                Logger.debug("perdu")
                saveScore()
                exit()
        else:
            if character_hp > 0:
                if num == 1:
                    monster_hp -= character_attack
                    if monster_hp > 0:
                        if monster_can_attack == 0:
                            character_hp -= (randint(1,3) * 10)
                            if character_hp < 1:
                                Logger.debug("Perdu")
                                saveScore()
                                exit()
                        else:
                            monster_can_attack -= 1
                    else:
                        Logger.debug("Gagné")
                        saveScore()
                        exit()
                elif num == 2:
                    monster_can_attack = 1
                else:
                    character_attack += 10
                    character_hp -= (randint(1,3) * 10)
                    if character_hp < 1:
                        Logger.debug("Perdu")
                        saveScore()
                        exit()
            else:
                Logger.debug("Perdu")
                saveScore()
                exit()

        Logger.debug("char_hp:"+str(character_hp))
        Logger.debug("monster_hp:"+str(monster_hp))

        self.lifehp = character_hp
        self.monsterhp = monster_hp

class InventScreen(Screen):
    nb_watermelon = NumericProperty()
    nb_potato = NumericProperty()
    nb_apple = NumericProperty()
    nb_mystery = NumericProperty(0)

    def on_pre_enter(self):
        self.invent(0)

    def saveInvent(self):
        Logger.debug("Write inventory.txt")
        # écrit le résultat dans un fichier txt
        with open('inventory.txt', 'w') as f:
            f.write("watermelon " + str(self.nb_watermelon) + '\n')
            f.write("potato " + str(self.nb_potato) + '\n')
            f.write("apple " + str(self.nb_apple) + '\n')

    def readInvent(self):
        try:
            Logger.debug("Read inventory.txt")
            with open("inventory.txt") as f:
                contents = f.readlines()
            self.nb_watermelon = contents[0].split()[1]
            self.nb_potato = contents[1].split()[1]
            self.nb_apple = contents[2].split()[1]
        except:
            pass

    def inventSave(self):
        self.saveInvent()

    def invent(self, num):
        global character_hp
        global character_prio
        if num == 0:
            self.readInvent()
        elif num == 1:
            if self.nb_watermelon > 0:
                self.nb_watermelon -= 1
                character_hp += 100
                Logger.debug("hp: "+ str(character_hp))
            else:
                pass
        elif num == 2:
            if self.nb_potato > 0:
                self.nb_potato -= 1
                character_prio = 3
            else:
                pass
        elif num == 3:
            if self.nb_apple > 0:
                self.nb_apple -= 1
                character_prio -= 1
            else:
                pass
        else:
            pass

        Logger.debug("nb_watermelon:"+str(self.nb_watermelon))
        Logger.debug("nb_potato:"+str(self.nb_potato))
        Logger.debug("nb_apple:"+str(self.nb_apple))
        Logger.debug("nb_mystery:"+str(self.nb_mystery))

sm = Builder.load_file('fight.kv')

class FightApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    FightApp().run()
    saveScore()



"""
Balade dans les tableaux
Si contact
    Menu
        Fight
            Attack1
                VieMonstre - 10
                Vie - attaqueMonstre
            Attack2
                VieMonstre - 20
                Vie - attaqueMonstre
            Attack3        
                VieMonstre - 30
                Vie - attaqueMonstre
        Element
        Inventory
        Escape
            return balade respawn vie -x
Quitter
"""