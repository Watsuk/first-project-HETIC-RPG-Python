
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
import subprocess
from fonction import collides, movey, movex, movey_no_mob, movex_no_mob, pop_up_collides, paterny1, paternx1, paterny2, paternx2, paterny3, paternx3, paterny4, paternx4, comparescore, saveInvent, readInvent, saveXP, readXP
    


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        
        with self.canvas:
            self.map = 4
            self.background = Rectangle(source="Earthmap.png", pos=(0,0), size=(800, 600))
            self.player = Rectangle(source= "sprites/front2.png", pos=(0,0), size=(60,60))
            self.enemy1 = Rectangle(source="transparent.png", pos=(200,400), size=(75,75))
            self.enemy2 = Rectangle(source="transparent.png", pos=(600,400), size=(75,75))
            self.enemy3 = Rectangle(source="transparent.png", pos=(200,200), size=(75,75))
            self.enemy4 = Rectangle(source="transparent.png", pos=(600,200), size=(75,75))
            self.apple = Rectangle(source="transparent.png", pos=(200,100), size=(50,60))
            self.watermelon = Rectangle(source="transparent.png", pos=(200,100), size=(50,50))
            self.potato = Rectangle(source="transparent.png", pos=(200,100), size=(50,50))

            self.pop_up = Rectangle(source="transparent.png", pos=(50,50), size=(700, 100))
            self.object1 = Rectangle(source="transparent.png", pos =(240,108), size=(150,30))
            self.object2 = Rectangle(source="transparent.png", pos =(500,108), size=(150,30))
            self.object3 = Rectangle(source="transparent.png", pos =(240,59), size=(150,30))
            self.gameover_screen = Rectangle(source="transparent.png", pos=(0,0), size=(800,600))

            self.direction = 0
            self.front = 0
            self.XP = 0
            self.Level = 1
            self.fight = False
            self.fight1 = False
            self.fight2 = False
            self.fight3 = False
            self.fight4 = False
            self.text = False
            self.text_page = 0
            self.drop1 = False
            self.drop2 = False
            self.drop3 = False
            self.gameover = False
            self.nb_watermelon = 0
            self.nb_apple = 0
            self.nb_potato = 0

        self.keysPressed = set()        
        
        Clock.schedule_interval(self.move_step,0)
        Clock.schedule_interval(self.direction1,0.25)

        
    def _on_keyboard_closed(self):
        self._keyboard.unbind(self.on_key_up)
        self._keyboard.unbind(self.on_key_down)
        self._on_key_down = None
    
    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(text)
        
        

    
    def _on_key_up(self,keyboard,keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)
            
    def move_step(self,dt):
        if self.gameover == False:
            step_size = 150 * dt
            currentx = self.player.pos[0]
            currenty = self.player.pos[1]
            if self.map == 0:
                enemyx = self.enemy1.pos[0]
                enemyy = self.enemy1.pos[1]
            elif self.map == 1:
                enemyx = self.apple.pos[0]
                enemyy = self.apple.pos[1]
            elif self.map == 2:
                enemyx = self.enemy2.pos[0]
                enemyy = self.enemy2.pos[1]
            elif self.map == 4:
                enemyx = self.watermelon.pos[0]
                enemyy = self.watermelon.pos[1]
            elif self.map == 6:
                enemyx = self.enemy3.pos[0]
                enemyy = self.enemy3.pos[1]
            elif self.map == 7:
                enemyx = self.potato.pos[0]
                enemyy = self.potato.pos[1]
            elif self.map == 8:
                enemyx = self.enemy4.pos[0]
                enemyy = self.enemy4.pos[1]
                    
            if self.map == 0:
                enemyx = paternx1(enemyx, enemyy, self.player.pos, self.player.size, self.enemy1.pos, self.enemy1.size)
                enemyy = paterny1(enemyx, enemyy, self.player.pos, self.player.size, self.enemy1.pos, self.enemy1.size)
            elif self.map == 2:
                enemyx = paternx2(enemyx, enemyy, self.player.pos, self.player.size, self.enemy2.pos, self.enemy2.size)
                enemyy = paterny2(enemyx, enemyy, self.player.pos, self.player.size, self.enemy2.pos, self.enemy2.size)
            elif self.map == 6:
                enemyx = paternx3(enemyx, enemyy, self.player.pos, self.player.size, self.enemy3.pos, self.enemy3.size)
                enemyy = paterny3(enemyx, enemyy, self.player.pos, self.player.size, self.enemy3.pos, self.enemy3.size)
            elif self.map == 8:
                enemyx = paternx4(enemyx, enemyy, self.player.pos, self.player.size, self.enemy4.pos, self.enemy4.size)
                enemyy = paterny4(enemyx, enemyy, self.player.pos, self.player.size, self.enemy4.pos, self.enemy4.size)
            if "i" in self.keysPressed:
                pass
            else:
                if self.map == 0 and self.fight1 == False:
                    currenty = movey(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy)
                    currentx = movex(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy)
                    if pop_up_collides(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy, self.map) == True:
                        subprocess.call("python fight.py", shell=True)
                        print(comparescore())
                        if comparescore() == "perdu":
                            self.gameover = True
                        elif comparescore() == "gagné":       
                            self.XP += 10
                            if self.XP >= 10:
                                while self.XP >= 10:
                                    if self.XP >= 10:
                                        self.Level += 1
                                        self.XP -= 10
                            saveXP(self)
                            self.fight1 = True
                        else:                                    
                            currentx = 400
                            currenty = 300
                elif self.map == 0 and self.fight1 == True:
                    currenty = movey_no_mob(self.keysPressed, currentx, currenty, step_size)
                    currentx = movex_no_mob(self.keysPressed, currentx, currenty, step_size)    
                elif self.map == 2 and self.fight2 == False:
                    currenty = movey(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy)
                    currentx = movex(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy)
                    if pop_up_collides(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy, self.map) == True:
                        subprocess.call("python fight.py", shell=True)
                        if comparescore() == "perdu":
                            self.gameover = True
                        elif comparescore() == "gagné":
                            self.XP += 10
                            if self.XP >= 10:
                                while self.XP >= 10:
                                    if self.XP >= 10:
                                        self.Level += 1
                                        self.XP -= 10
                                saveXP(self)
                                self.fight2 = True
                        else:                                    
                            currentx = 400
                            currenty = 300
                elif self.map == 2 and self.fight1 == True:
                    currenty = movey_no_mob(self.keysPressed, currentx, currenty, step_size)
                    currentx = movex_no_mob(self.keysPressed, currentx, currenty, step_size) 
                elif self.map == 6 and self.fight3 == False:
                    currenty = movey(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy)
                    currentx = movex(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy)
                    if pop_up_collides(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy, self.map) == True:
                        subprocess.call("python fight.py", shell=True)
                        if comparescore() == "perdu":
                            self.gameover = True
                        elif comparescore() == "gagné":
                            self.XP += 10
                            while self.XP >= 10:
                                if self.XP >= 10:
                                    self.Level += 1
                                    self.XP -= 10
                            saveXP(self)       
                            self.fight3 = True
                        else:                                    
                            currentx = 400
                            currenty = 300
                elif self.map == 6 and self.fight3 == True:
                    currenty = movey_no_mob(self.keysPressed, currentx, currenty, step_size)
                    currentx = movex_no_mob(self.keysPressed, currentx, currenty, step_size) 
                elif self.map == 8 and self.fight4 == False:
                    currenty = movey(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy)
                    currentx = movex(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy)
                    if pop_up_collides(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy, self.map) == True:
                        subprocess.call("python fight.py", shell=True)
                        if comparescore() == "perdu":
                            self.gameover = True
                        elif comparescore() == "gagné":
                            self.XP += 10
                            while self.XP >= 10:
                                if self.XP >= 10:
                                    self.Level += 1
                                    self.XP -= 10
                            saveXP(self)       
                            self.fight4 = True
                        else:                                    
                            currentx = 400
                            currenty = 300
                elif self.map == 8 and self.fight4 == True:
                    currenty = movey_no_mob(self.keysPressed, currentx, currenty, step_size)
                    currentx = movex_no_mob(self.keysPressed, currentx, currenty, step_size) 
                elif self.map == 1:
                    currenty = movey_no_mob(self.keysPressed, currentx, currenty, step_size)
                    currentx = movex_no_mob(self.keysPressed, currentx, currenty, step_size)
                    if self.drop1 == False:
                        self.drop1 = pop_up_collides(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy, self.map)
                        self.nb_watermelon = 1
                        saveInvent(self)
                        
                        
                elif self.map == 4:
                    currenty = movey_no_mob(self.keysPressed, currentx, currenty, step_size)
                    currentx = movex_no_mob(self.keysPressed, currentx, currenty, step_size)
                    if self.drop2 == False:
                        self.drop2 = pop_up_collides(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy, self.map)
                        self.nb_apple = 1
                        saveInvent(self)
                        

                elif self.map == 7:
                    currenty = movey_no_mob(self.keysPressed, currentx, currenty, step_size)
                    currentx = movex_no_mob(self.keysPressed, currentx, currenty, step_size)
                    if self.drop3 == False:
                        self.drop3 = pop_up_collides(self.keysPressed, currentx, currenty, step_size, self.player.size, enemyx, enemyy, self.map)            
                        self.nb_potato = 1
                        saveInvent(self)
                        

                elif "t" in self.keysPressed:
                    pass
                else:
                        currenty = movey_no_mob(self.keysPressed, currentx, currenty, step_size)
                        currentx = movex_no_mob(self.keysPressed, currentx, currenty, step_size)
        
            if currentx >= 750 and self.map != 2 and self.map != 5 and self.map != 8:
                self.map += 1
                currentx = 0
                if self.map == 0:
                    enemyx = self.enemy1.pos[0]
                    enemyy = self.enemy1.pos[1]
                if self.map == 2:
                    enemyx = self.enemy2.pos[0]
                    enemyy = self.enemy2.pos[1]
                if self.map == 6:
                    enemyx = self.enemy3.pos[0]
                    enemyy = self.enemy3.pos[1]
                if self.map == 8:
                    enemyx = self.enemy4.pos[0]
                    enemyy = self.enemy4.pos[1]
            elif currentx >= 750:
                currentx = 750
            if currentx < 0 and self.map != 0 and self.map != 3 and self.map != 6:
                currentx = 750
                self.map -= 1
                if self.map == 0:
                    enemyx = self.enemy1.pos[0]
                    enemyy = self.enemy1.pos[1]
                if self.map == 2:
                    enemyx = self.enemy2.pos[0]
                    enemyy = self.enemy2.pos[1]
                if self.map == 6:
                    enemyx = self.enemy3.pos[0]
                    enemyy = self.enemy3.pos[1]
                if self.map == 8:
                    enemyx = self.enemy4.pos[0]
                    enemyy = self.enemy4.pos[1]
            elif currentx < 0:
                currentx = 0
            if currenty >= 550 and self.map != 0 and self.map != 1 and self.map != 2:
                currenty = 0
                self.map -= 3
                if self.map == 0:
                    enemyx = self.enemy1.pos[0]
                    enemyy = self.enemy1.pos[1]
                if self.map == 2:
                    enemyx = self.enemy2.pos[0]
                    enemyy = self.enemy2.pos[1]
                if self.map == 6:
                    enemyx = self.enemy3.pos[0]
                    enemyy = self.enemy3.pos[1]
                if self.map == 8:
                    enemyx = self.enemy4.pos[0]
                    enemyy = self.enemy4.pos[1]
            elif currenty >= 550:
                currenty = 550
            if currenty < 0 and self.map != 6 and self.map != 7 and self.map != 8:
                currenty = 550
                self.map += 3
                if self.map == 0:
                    enemyx = self.enemy1.pos[0]
                    enemyy = self.enemy1.pos[1]
                if self.map == 2:
                    enemyx = self.enemy2.pos[0]
                    enemyy = self.enemy2.pos[1]
                if self.map == 6:
                    enemyx = self.enemy3.pos[0]
                    enemyy = self.enemy3.pos[1]
                if self.map == 8:
                    enemyx = self.enemy4.pos[0]
                    enemyy = self.enemy4.pos[1]
            elif currenty < 0:
                currenty = 0

            self.player.pos= (currentx, currenty) 
            if self.map == 0:
                self.enemy1.pos = (enemyx, enemyy)
            elif self.map == 2:
                self.enemy2.pos = (enemyx, enemyy) 
            elif self.map == 6:
                self.enemy3.pos = (enemyx, enemyy) 
            elif self.map == 8:
                self.enemy4.pos = (enemyx, enemyy) 
                
    def direction1(self, dt):
        if self.gameover == True:
            self.gameover_screen.source="gameover.png"
            if " " in self.keysPressed:
                exit()
        elif self.fight1 == True and self.fight2 == True and self.fight3 == True and self.fight4 == True:
            self.gameover_screen.source="win.png"
            if " " in self.keysPressed:
                exit()
        elif self.text == False:
            if self.map != 0 or self.fight1 == True:
                self.enemy1.source="transparent.png"
            if self.map != 1 or self.drop1 == True:
                self.watermelon.source="transparent.png"
            if self.map != 2 or self.fight2 == True:
                self.enemy2.source="transparent.png"
            if self.map != 4 or self.drop2 == True:
                self.apple.source="transparent.png"
            if self.map != 6 or self.fight3 == True:
                self.enemy3.source="transparent.png"
            if self.map != 7 or self.drop3 == True:
                self.potato.source="transparent.png"
            if self.map != 8 or self.fight4 == True:
                self.enemy4.source="transparent.png"
            if self.map == 0 and self.fight1 == False:
                if self.direction%2 == 0:
                    self.enemy1.source="enemy1/front1.png"
                else:
                    self.enemy1.source="enemy1/front2.png"
                self.direction +=1
            elif self.map == 1 and self.drop1 == False:
                self.watermelon.source="sprites/watermelon.png"
                self.direction +=1
            elif self.map == 2 and self.fight2 == False:
                if self.direction%2 == 0:
                    self.enemy2.source="enemy1/front1.png"
                else:
                    self.enemy2.source="enemy1/front2.png"
                self.direction +=1
            elif self.map == 4 and self.drop2 == False:
                self.apple.source="sprites/apple.png"
                self.direction +=1
            elif self.map == 6 and self.fight3 == False:
                if self.direction%2 == 0:
                    self.enemy3.source="enemy1/front1.png"
                else:
                    self.enemy3.source="enemy1/front2.png"
                self.direction +=1
            elif self.map == 7 and self.drop3 == False:
                self.potato.source="sprites/potato.png"
                self.direction +=1
            elif self.map == 8 and self.fight4 == False:
                if self.direction%2 == 0:
                    self.enemy4.source="enemy1/front1.png"
                else:
                    self.enemy4.source="enemy1/front2.png"
                self.direction +=1
            else:
                self.direction += 1
            if "z"in self.keysPressed and "q" in self.keysPressed and "s" in self.keysPressed and "d" in self.keysPressed:
                self.player.source="sprites/santa.png"
                self.front = 5
                if "t" in self.keysPressed:
                    if self.direction%2 == 0:
                        self.player.source="sprites/santa1.png"
                    else:
                        self.player.source="sprites/santa2.png"
            elif "t" in self.keysPressed:
                if self.direction%2 == 0:
                    self.player.source="sprites/left2.png"
                else:
                    self.player.source="sprites/right2.png"
                self.front = 4
            elif "s" in self.keysPressed:
                if self.direction%2 == 0:
                    self.player.source="sprites/front1.png"
                else:
                    self.player.source="sprites/front3.png"
                self.front = 0
            elif "z" in self.keysPressed:
                if self.direction%2 == 0:
                    self.player.source="sprites/up1.png"
                else:
                    self.player.source="sprites/up3.png"
                self.front = 1
            elif "q" in self.keysPressed:
                if self.direction%2 == 0:
                    self.player.source="sprites/left1.png"
                else:
                    self.player.source="sprites/left3.png"
                self.front = 2
            elif "d" in self.keysPressed:
                if self.direction%2 == 0:
                    self.player.source="sprites/right1.png"
                else:
                    self.player.source="sprites/right3.png"
                self.front = 3
            elif "i" in self.keysPressed:
                self.pop_up.source = "pop_up/inventaire_vide.png"
                readInvent(self)
                print("pasteque", self.nb_watermelon)
                print("pomme", self.nb_apple)
                print("patate", self.nb_potato)
                if float(self.nb_watermelon) == 1:
                    self.object1.source = "pop_up/watermelon.png"
                if float(self.nb_apple) == 1:
                    self.object2.source = "pop_up/apple.png"
                if float(self.nb_potato) == 1:
                    self.object3.source = "pop_up/potato.png"

            else:
                if self.front == 0:
                    self.player.source="sprites./front2.png"
                if self.front == 1:
                    self.player.source="sprites./up2.png"
                if self.front == 2:
                    self.player.source="sprites./left2.png"
                if self.front == 3:
                    self.player.source="sprites./right2.png"
                if self.front == 5:
                    self.player.source="sprites/santa.png"
                self.object1.source = "transparent.png"
                self.object2.source = "transparent.png"
                self.object3.source = "transparent.png"
                self.pop_up.source = "transparent.png"
        else:
            if self.text_page == 0:
                self.pop_up.source = "pop_up/text1"
                self.text_page = 1
            if self.text_page == 1:
                if " " in self.keysPressed:
                    self.pop_up.source = "pop_up/text2"
                    self.text_page = 2
            if self.text_page == 1:
                if " " in self.keysPressed:
                    self.pop_up.source = "pop_up/text3"
                    self.text_page = 3
            if self.text_page == 1:
                if " " in self.keysPressed:
                    self.pop_up.source = "pop_up/text4"
                    self.text_page = 4
            if self.text_page == 4:
                if " " in self.keysPressed:
                    self.pop_up.source = "transparent.png"
                    self.text_page = 0

        
        

class MyApp(App):
    def build(self):
        return GameWidget()
    
if __name__ == "__main__":
    MyApp().run()
game.py
