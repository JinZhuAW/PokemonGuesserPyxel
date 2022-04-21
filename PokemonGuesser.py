import pyxel
import os
import requests
from random import randint
import urllib.request

api_url = "https://pokeapi.co/api/v2/pokemon/"

def get_api_responds(index):
    search = api_url + str(index)
    response = requests.get(search)
    return response

def get_pokemon_name(response):
    name = response.json()["name"]
    return name

def get_pokemon_sprite_url(response,answer):
    if answer == True:
        url = response.json()["sprites"]["versions"]["generation-vii"]["ultra-sun-ultra-moon"]["front_default"]
    else:
        url = response.json()["sprites"]["versions"]["generation-vii"]["icons"]["front_default"]
    return url


def save_sprite(url):
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
    return filename

def show_image(response,answer):
    url = get_pokemon_sprite_url(response,answer)
    filename = save_sprite(url)
    return filename

def add_letter(text):
    if pyxel.btnr(pyxel.KEY_A):
        text += "a"
    elif pyxel.btnr(pyxel.KEY_B):
        text += "b"
    elif pyxel.btnr(pyxel.KEY_C):
        text += "c"
    elif pyxel.btnr(pyxel.KEY_D):
        text += "d"
    elif pyxel.btnr(pyxel.KEY_E):
        text += "e"
    elif pyxel.btnr(pyxel.KEY_F):
        text += "f"
    elif pyxel.btnr(pyxel.KEY_G):
        text += "g"
    elif pyxel.btnr(pyxel.KEY_H):
        text += "h"
    elif pyxel.btnr(pyxel.KEY_I):
        text += "i"
    elif pyxel.btnr(pyxel.KEY_J):
        text += "j"
    elif pyxel.btnr(pyxel.KEY_K):
        text += "k"
    elif pyxel.btnr(pyxel.KEY_L):
        text += "l"
    elif pyxel.btnr(pyxel.KEY_M):
        text += "m"
    elif pyxel.btnr(pyxel.KEY_N):
        text += "n"
    elif pyxel.btnr(pyxel.KEY_O):
        text += "o"
    elif pyxel.btnr(pyxel.KEY_P):
        text += "p"
    elif pyxel.btnr(pyxel.KEY_Q):
        text += "q"
    elif pyxel.btnr(pyxel.KEY_R):
        text += "r"
    elif pyxel.btnr(pyxel.KEY_S):
        text += "s"
    elif pyxel.btnr(pyxel.KEY_T):
        text += "t"
    elif pyxel.btnr(pyxel.KEY_U):
        text += "u"
    elif pyxel.btnr(pyxel.KEY_V):
        text += "v"
    elif pyxel.btnr(pyxel.KEY_W):
        text += "w"
    elif pyxel.btnr(pyxel.KEY_X):
        text += "x"
    elif pyxel.btnr(pyxel.KEY_Y):
        text += "y"
    elif pyxel.btnr(pyxel.KEY_Z):
        text += "z"
    return text

        
def remove_letter(text):
    if text.split(':\n\n')[-1] != "":
        return text[:-1]
    else:
        return text

class App:

    def __init__(self):
        pyxel.init(180, 180, title="Pokemon Guesser Game")
        self.game_init()
        
        pyxel.run(self.update, self.draw)
        
    def game_init(self):
        r_num = randint(1,151)
        self.restart = False
        self.imgw = 40
        self.imgh = 30
        self.imgx = 70
        self.imgy = 10
        self.txtx = 10
        self.txty = 80
        self.message = "Please enter the name of the pokemon:\n\n"
        self.response = get_api_responds(r_num)
        self.name = get_pokemon_name(self.response)
        self.filename = show_image(self.response,False)
        pyxel.image(0).load(0, 0, self.filename)

    def set_answer_image(self):
        self.filename = show_image(self.response,True)
        pyxel.image(0).load(0, 0, self.filename)
        self.imgw = 128
        self.imgh = 128
        self.imgx = 26
        self.imgy = 0
    
    def update(self):
        if pyxel.btnr(pyxel.KEY_0):
            os.remove(self.filename)
            quit()
            
    
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.imgx, self.imgy, 0, 0, 0, self.imgw, self.imgh)
        
        self.message = add_letter(self.message)
        pyxel.text(self.txtx, self.txty, self.message, pyxel.COLOR_WHITE)
        
        if pyxel.btnr(pyxel.KEY_RETURN):
            if self.restart == False:
                guessed_name = self.message.split(':\n\n')[-1]
                if guessed_name == self.name:
                    self.set_answer_image()
                    self.txty = 130
                    self.message = f"Well done! It's {self.name}!\nYou are a pokemon expert!!\n\nPress enter to Continue, 0 to quit: "
                    self.restart = True
                elif guessed_name == "a":
                    self.set_answer_image()
                    self.txty = 130
                    self.message = f"The answer is {self.name}!!\n\nPress enter to Continue, 0 to quit: "
                    self.restart = True
                else:    
                    self.message = f"Wrong Answer! Please try again\n\n(Type a get answer):\n\n"    
            else:
                os.remove(self.filename)
                self.game_init()

        if pyxel.btnr(pyxel.KEY_BACKSPACE):
            self.message = remove_letter(self.message)
App()
