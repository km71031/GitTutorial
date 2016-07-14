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

Window.size = (1000,600)
rrr = 10
#w = Widget( size=(1300,400),
 #           size_hint=(None, None) )

#enemymove = False

class Player1(Widget):
    LP = NumericProperty(50)
    time = NumericProperty(200)
    #Color = (1, 0, 0)
    def pcrush(self, wp):

        if self.collide_widget(wp):
            print "collide!"
            self.LP -= 1

            """ print "-" * 20
            print  enemy.center
            print "=" * 20  #"""

            dx = wp.x - self.x
            dy = wp.y - self.y
            tan = dy / dx
            cos = math.sqrt(1 / (1 + (tan) ** 2))
            if self.x > wp.x:
                cos *= -1
            sin = tan * cos
            wp.x += rrr * cos
            wp.y += rrr * sin

        """
            if self.x < enemy.x:
                enemy.x += 20
            else:
                enemy.x -= 20

            if self.y < enemy.y:
                enemy.y += 20
            else:
                enemy.y -= 20  #"""

"""def func(**kwargs):

    for key, val in kwargs:
        print(key,val)

func(a=1,b=2)"""
           # enemy.center -= [100, 10] # Todo 敵の位置を更新
            #senemymove = True

#class Weapon(Player1):
 #   def test1(self):
  #      print "test1"



class Escape(Widget):
    player1 = ObjectProperty(None)
    weapon = ObjectProperty(None)

    def start(self):
        enx = int(math.ceil(500 * random.random()))
        eny = int(math.ceil(500 * random.random()))
        print enx, eny
        self.player1.center = [100, 300]
        self.weapon.center = [enx, eny]
        print self.weapon.center
        print self.player1.center

        #self.__setattr__("player2", ObjectProperty(None))
        #self.player2 = ObjectProperty(None)



 #    enemy = []
 #   for i in range(20):
 #       enemy.append(ObjectProperty(None))
 #       enemy[i].center = (100 * random.random(), 100 * random.random())

    #def on_touch_move(self, touch):
     #   self.player1.center = touch

    def on_touch_move(self, touch):
        self.player1.center_y = touch.y
        self.player1.center_x = touch.x


    def update(self, dt):
       # for en in self.enemy:
        #    self.p1.pcrush(en)

        self.player1.pcrush(self.weapon)
        if self.player1.time:
            self.player1.time -= 1
        else:
            self.player1.time = 0
            sys.exit()
        if self.player1.LP:
            pass
        else:
            sys.exit()


class EscapeApp(App):
    def build(self):
         game = Escape()

         game.start()
         Clock.schedule_interval(game.update, 1.0/10.0)
         return game



if __name__ == "__main__":
    EscapeApp().run()








