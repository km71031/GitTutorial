# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import NumericProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random
import math
#import kivy.uix.layout
import sys
from kivy.core.window import Window
#from kivy.graphics import Color
#from Tkinter import *


Window.size = (1000,600)
rrr = 12
#w = Widget( size=(1300,400),
 #           size_hint=(None, None) )

#enemymove = False

class Mole(Widget):

    #Color = (1, 0, 0)
    #def boxattack(self, en):
     #  if self.collide_widget(en):

    def whack(self, hm):
        """if self.collide_widget(hm):
            self.mole.x = 900 * random.random()
            self.mole.y = 500 * random.random()
            self.score += 1"""
        pass

    """
            if self.x < enemy.x:
                enemy.x += 20
            else:
                enemy.x -= 20

            if self.y < enemy.y:
                enemy.y += 20
            else:
                enemy.y -= 20  #
    """
class Hammer(Mole):
    def test2(self):
        print "test2"

"""def func(**kwargs):

    for key, val in kwargs:
        print(key,val)

func(a=1,b=2)"""

class MoleGame(Widget):
    mole = ObjectProperty(Mole)
    hammer = ObjectProperty(Hammer)
    score = NumericProperty(0)
    time = NumericProperty(1000)
    #mole = Mole()
    #hammer = Hammer()
    def start(self):
        #self.mole = Mole()
        #self.hammer =Hammer()
        #wpx = int(math.ceil(500 * random.random()))
        #wpy = int(math.ceil(500 * random.random()))
        self.mole.center = [100, 300]
        self.hammer.center= [450, 250]
        print self.mole.center
        print self.hammer.center



        #self.__setattr__("player2", ObjectProperty(None))
        #self.player2 = ObjectProperty(None)
 #    enemy = []
 #   for i in range(20):
 #       enemy.append(ObjectProperty(None))
 #       enemy[i].center = (100 * random.random(), 100 * random.random())

    #def on_touch_move(self, touch):
     #   self.player1.center = touch

    def on_touch_move(self, touch):
        #moleX = self.mole.x
        hammerX = self.hammer.x
        hammerY = self.hammer.y
        if self.time:
            """
            if moleX < touch.x < moleX + self.mole.width:
                self.mole.x = 900 * random.random()
                self.mole.y = 500 * random.random()
                self.score += 1
            #"""
            if hammerX < touch.x < hammerX + self.hammer.width:
                if hammerY< touch.y < hammerY + self.hammer.width:
                    self.hammer.x = touch.x - self.hammer.width / 2
                    self.hammer.y = touch.y - self.hammer.height / 2

    #hammer = Hammer()
    def update(self, dt):
       # for en in self.enemy:
        #    self.p1.pcrush(en)
        #self.mole.on_touch_move
        #self.mole.whack(self)

        if self.mole.collide_widget(self.hammer):
           self.mole.x = 900 * random.random()
           self.mole.y = 500 * random.random()
           self.hammer.x = 900 * random.random()
           self.hammer.y = 500 * random.random()
           self.score += 1


        if self.time:
            self.time -= 1
        else:
            self.time = 0

        """if self.mole.LP:
            pass
        else:
            sys.exit()"""


class WhackmoleApp(App):
    def build(self):
         game = MoleGame()
         game.start()
         Clock.schedule_interval(game.update, 1.0 / 50.0)
         #print game.hammer.center
         return game



if __name__ == "__main__":
    WhackmoleApp().run()




