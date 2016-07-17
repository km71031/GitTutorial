# -*- coding: utf-8 -*-
from kivy.config import Config
#Config.set('graphics', 'fullscreen', '1')
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '500')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import NumericProperty
from kivy.properties import OptionProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random
import math
#import kivy.uix.layout
import sys
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Ellipse
#from kivy.graphics import Color
#from Tkinter import *

#Window.size = (1000,600)


class Trash(Widget):
    avoidE = 0
    COR = 0.9
    velocityX = 0
    velocityY = 0
    g = 0.2
    def bounce(self, box, ):
        if self.collide_widget(box):
         #   if self.avoidE <= 2:
            self.velocityX *= - self.COR
         #self.avoidE += 1
         #elif self.avoidE:
            #self.avoidE -= 1



    def bounce3(self, box):
        if self.collide_widget(box)\
        and box.x + 5 < self.x < box.x + box.width - 5:
            if self.avoidE < 5:
                self.velocityY *= -self.COR
                self.avoidE += 1
            else:
                self.y = box.top
                self.avoidE -= 5
                if self.velocityY > 0:
                    self.velocityY = 2
        elif self.avoidE:
            self.avoidE -= 1
              #self.avoidE += 1
        #elif self.avoidE:
           # self.avoidE -= 1

    def fall(self):
        self.velocityY -= self.g
    """def avoidE(self, box):
        if self.collide_widget(box)\
        and (self.velocityX) = """

class TrashCan(Widget):
    hakoheight = 150
class TrashCan3(TrashCan):
    hakowidth = 150

class Throw(Widget):
    gomi = ObjectProperty(Trash)
    hako1 = ObjectProperty(TrashCan)
    hako2 = ObjectProperty(TrashCan)
    hako3 = ObjectProperty(TrashCan3)
    def start(self):
        self.success = 0
        self.finishshooting = 0
        self.ready = 0
        self.gomi.center = [50, 100]
        hakopos = [700, 60]
        self.hako1.pos = hakopos
        self.hako2.pos = hakopos
        self.hako2.x += self.hako3.hakowidth
        self.hako3.pos = hakopos

    def on_touch_down(self, touch):
        print touch.pos
        self.touchDx = touch.x
        self.touchDy = touch.y
        #print self.touchD[1]
    def on_touch_up(self, touch):
        print touch.pos
        self.touchUx = touch.x
        self.touchUy = touch.y
        self.ready = 2

    def update(self, dt):
        #print self.ready
        #while self.finishshooting < 1:
        if self.finishshooting < 1:
            if self.ready > 1:
                #print self.touchDx
                dx = self.touchDx - self.touchUx
                dy = self.touchDy - self.touchUy
                tan = dy / dx
                cos = math.sqrt(1 / (1 + tan ** 2))
                if dx < 0:
                    cos *= -1
                sin = tan * cos
                elongation_2 = (dx ** 2 + dy ** 2) / 500.0
                self.gomi.velocityX += math.sqrt(elongation_2) * cos
                self.gomi.velocityY += math.sqrt(elongation_2) * sin
                self.finishshooting = 2
            else:
                pass
        else:
            pass
        #if self.gomi.avoidE < 2:
        if self.success < 2:
            self.gomi.x += self.gomi.velocityX
            self.gomi.y += self.gomi.velocityY
        elif self.success == 3:
            print "Success!"
        if self.gomi.x + self.gomi.width > self.width:
            self.gomi.velocityX = - self.gomi.COR * abs(self.gomi.velocityX)
        if self.gomi.x < self.x:
            self.gomi.velocityX = self.gomi.COR * abs(self.gomi.velocityX)
        if self.gomi.top > self.height:
            self.gomi.velocityY = - self.gomi.COR * abs(self.gomi.velocityY)
        if self.gomi.y < self.y:
            self.gomi.velocityY = self.gomi.COR * abs(self.gomi.velocityY)
        self.gomi.bounce(self.hako1)
        self.gomi.bounce(self.hako2)
        self.gomi.bounce3(self.hako3)

        if self.finishshooting:
            if self.gomi.y > self.y:
                if abs(self.gomi.velocityY) > 1.5 \
                or self.gomi.y > 1:
                    self.gomi.fall()
                else:
                    self.gomi.velocityY = 0

        if self.hako1.x + self.hako1.width < self.gomi.x < self.hako2.x \
        and self.hako3.top < self.gomi.top < self.hako3.y + self.gomi.height + 80 \
        and self.gomi.velocityY ** 2 < 2 * self.gomi.g * (self.hako1.top - self.gomi.y):
            self.success += 1
        elif self.success:
            if self.success < 2:
              self.success -= 1
        #if self.gomi.collide_widget(self.hako):
         #   self.gomi.velocity *= -1
    #def on_touch_move(self, touch):


class Throw_trashApp(App):

    def build(self):
        game = Throw()
        """with game.canvas:
            Color(1, 1, 0, .5)
            Line(points=[100, 250, 100, 50, 350, 50, 350, 250], width=10)
                                                # , close)で閉じる
            Color(0, .5, 1)
            Ellipse(pos=(150, 150), size=(120, 120))"""
        game.start()
        #game.shoot()
        Clock.schedule_interval(game.update, 1.0 /90.0)
        print game.gomi.avoidE
        return game


if __name__ == '__main__':
    Throw_trashApp().run()