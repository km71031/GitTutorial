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
#from kivy.graphics import Color
#from Tkinter import *
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Ellipse


#Window.size = (1000,600)


class Trash(Widget):
    velocityX = 0
    velocityY = 0
    def bounce(self, box):
        if self.collide_widget(box):
            self.velocityX *= -1

    def bounce3(self, box):
        if self.collide_widget(box):
            self.velocityY *= -1
    def fall(self):
        self.velocityY -= 0.1

class TrashCan(Widget):
    hakoheight = 100
class TrashCan3(TrashCan):
    hakowidth = 150

class Throw(Widget):
    gomi = ObjectProperty(Trash)
    hako1 = ObjectProperty(TrashCan)
    hako2 = ObjectProperty(TrashCan)
    hako3 = ObjectProperty(TrashCan3)
    def start(self):
        self.finishshooting = 0
        self.ready = 0
        self.gomi.center = [150, 100]
        hakopos = [500, 200]
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
        #while self.finishshooting < 1:
        if self.ready > 1:
            print self.touchDx
            dx = self.touchDx - self.touchUx
            dy = self.touchDy - self.touchUy
            tan = dy / dx
            cos = math.sqrt(1 / (1 + tan ** 2))
            if dx < 0:
                cos *= -1
            sin = tan * cos
            elongation_2 = dx ** 2 + dy **2
            self.gomi.velocityX += math.sqrt(elongation_2) * cos
            self.gomi.velocityY += math.sqrt(elongation_2) * sin
            self.finishshooting = 2
        else:
            pass
        self.gomi.x += self.gomi.velocityX
        self.gomi.y += self.gomi.velocityY
        if self.gomi.x + self.gomi.width > self.width\
        or self.gomi.x < self.x:
            self.gomi.velocityX *= -1
        if self.gomi.top > self.height\
        or self.gomi.y < self.y:
            self.gomi.velocityY *= -1
        self.gomi.bounce(self.hako1)
        self.gomi.bounce(self.hako2)
        self.gomi.bounce3(self.hako3)

        if self.finishshooting:
            self.gomi.fall()
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
        game.shoot()
        Clock.schedule_interval(game.update, 1.0 /30.0)
        return game


if __name__ == '__main__':
    Throw_trashApp().run()