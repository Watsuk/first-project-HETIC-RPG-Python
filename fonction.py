
import kivy
from kivy.logger import Logger, LOG_LEVELS

def collides(rect1,rect2):
    r1x = rect1[0][0]
    r1y = rect1[0][1]
    r2x = rect2[0][0]
    r2y = rect2[0][1]
    r1w = rect1[1][0]
    r1h = rect1[1][1]
    r2w = rect2[1][0]
    r2h = rect2[1][1]
    
    if(r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
        return False
    else:
        return True

    
def movey(keysPressed, currentx, currenty, step_size, playersize, enemyx, enemyy):
    if "z" in keysPressed:
        if collides(((currentx, currenty + step_size), playersize), ((enemyx, enemyy), (75,75))):
            currenty += step_size 
    if "z" in keysPressed and "c" in keysPressed:
        if collides(((currentx, currenty + step_size), playersize), ((enemyx, enemyy), (75,75))):
            currenty += step_size/2            
    if "s" in keysPressed:
        if collides(((currentx, currenty - step_size), playersize), ((enemyx, enemyy), (75,75))):
            currenty -= step_size
    if "s" in keysPressed and "c" in keysPressed:
        if collides(((currentx, currenty - step_size), playersize), ((enemyx, enemyy), (75,75))):
            currenty -= step_size/2  
    return currenty 

def movex(keysPressed, currentx, currenty, step_size, playersize, enemyx, enemyy):
    if "q" in keysPressed:
        if collides(((currentx - step_size, currenty), playersize), ((enemyx, enemyy), (75,75))):
            currentx -= step_size
    if "q" in keysPressed and "c" in keysPressed:
        if collides(((currentx - step_size, currenty), playersize), ((enemyx, enemyy), (75,75))):
            currentx -= step_size/2      
    if "d" in keysPressed:
        if collides(((currentx + step_size, currenty), playersize), ((enemyx, enemyy), (75,75))):
            currentx += step_size
    if "d" in keysPressed and "c" in keysPressed:
        if collides(((currentx + step_size, currenty), playersize), ((enemyx, enemyy), (75,75))):
            currentx += step_size/2
    return currentx

def movey_no_mob(keysPressed, currentx, currenty, step_size):
    if "z" in keysPressed:
            currenty += step_size 
    if "z" in keysPressed and "c" in keysPressed:
            currenty += step_size/2            
    if "s" in keysPressed:
            currenty -= step_size
    if "s" in keysPressed and "c" in keysPressed:
            currenty -= step_size/2  
    return currenty 

def movex_no_mob(keysPressed, currentx, currenty, step_size):
    if "q" in keysPressed:
            currentx -= step_size
    if "q" in keysPressed and "c" in keysPressed:
            currentx -= step_size/2      
    if "d" in keysPressed:
            currentx += step_size
    if "d" in keysPressed and "c" in keysPressed:
            currentx += step_size/2
    return currentx


def paternx1(enemyx, enemyy, playerpos, playersize, enemy1pos, enemy1size):
    if collides((playerpos, playersize), (enemy1pos, enemy1size)):
        if enemyy == 400 and enemyx < 300:
            enemyx += 1
        elif enemyy == 500 and enemyx > 200:
            enemyx -= 1
    return enemyx
def paterny1(enemyx, enemyy, playerpos, playersize, enemy1pos, enemy1size):
    if collides((playerpos, playersize), (enemy1pos, enemy1size)):
        if enemyx == 300 and enemyy < 500:
            enemyy += 1
        elif enemyx == 200 and enemyy > 400:
            enemyy -= 1
    return enemyy



def paternx2(enemyx, enemyy, playerpos, playersize, enemy1pos, enemy1size):
    if collides((playerpos, playersize), (enemy1pos, enemy1size)):
        if enemyy == 400 and enemyx < 700:
            enemyx += 1
        elif enemyy == 500 and enemyx > 600:
            enemyx -= 1
    return enemyx
def paterny2(enemyx, enemyy, playerpos, playersize, enemy1pos, enemy1size):
    if collides((playerpos, playersize), (enemy1pos, enemy1size)):
        if enemyx == 700 and enemyy < 500:
            enemyy += 1
        elif enemyx == 600 and enemyy > 400:
            enemyy -= 1
    return enemyy



def paternx3(enemyx, enemyy, playerpos, playersize, enemy1pos, enemy1size):
    if collides((playerpos, playersize), (enemy1pos, enemy1size)):
        if enemyy == 200 and enemyx < 300:
            enemyx += 1
        elif enemyy == 300 and enemyx > 200:
            enemyx -= 1
    return enemyx
def paterny3(enemyx, enemyy, playerpos, playersize, enemy1pos, enemy1size):
    if collides((playerpos, playersize), (enemy1pos, enemy1size)):
        if enemyx == 300 and enemyy < 300:
            enemyy += 1
        elif enemyx == 200 and enemyy > 200:
            enemyy -= 1
    return enemyy



def paternx4(enemyx, enemyy, playerpos, playersize, enemy1pos, enemy1size):
    if collides((playerpos, playersize), (enemy1pos, enemy1size)):
        if enemyy == 200 and enemyx < 700:
            enemyx += 1
        elif enemyy == 300 and enemyx > 600:
            enemyx -= 1
    return enemyx
def paterny4(enemyx, enemyy, playerpos, playersize, enemy1pos, enemy1size):
    if collides((playerpos, playersize), (enemy1pos, enemy1size)):
        if enemyx == 700 and enemyy < 300:
            enemyy += 1
        elif enemyx == 600 and enemyy > 200:
            enemyy -= 1
    return enemyy

def pop_up_collides(keysPressed, currentx, currenty, step_size, playersize, enemyx, enemyy, map):
    if collides(((currentx + step_size, currenty), playersize), ((enemyx, enemyy), (75,75))) == False:
        return True
    elif collides(((currentx - step_size, currenty), playersize), ((enemyx, enemyy), (75,75))) == False:
        return True
    elif collides(((currentx, currenty + step_size), playersize), ((enemyx, enemyy), (75,75))) == False:
        return True
    elif collides(((currentx, currenty - step_size), playersize), ((enemyx, enemyy), (75,75))) == False:
        return True
    else:
        return False
def fight_test(keysPressed, currentx, currenty, step_size, playersize, enemyx, enemyy, fight):
    if collides(((currentx + step_size, currenty), playersize), ((enemyx, enemyy), (75,75))) == False:
        return True
    if fight == True:
        return True

def comparescore():
    with open("fightscore.txt") as f:
        contents = f.readlines()
    chp = contents[0].split()[1]
    mhp = contents[1].split()[1]
 
    if int(chp) > 0 and int(mhp) > 0:
        return "fuite"
    elif int(chp) <= 0:
        return "perdu"
    else:
        return "gagné"
    
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

def saveXP(self):
        Logger.debug("Write XP.txt")
        # écrit le résultat dans un fichier txt
        with open('XP.txt', 'w') as f:
            f.write("Level " + str(self.Level) + '\n')
            f.write("XP" + str(self.XP) + '\n')

def readXP(self):
    try:
        Logger.debug("Read XP.txt")
        with open("XP.txt") as f:
            contents = f.readlines()
        self.Level = contents[0].split()[1]
        self.XP = contents[1].split()[1]
    except:
        pass