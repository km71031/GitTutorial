from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import ReferenceListProperty
from kivy.properties import NumericProperty
from kivy.vector import Vector
from kivy.clock import Clock
import random
import  math

class Player1(Widget):
    LP = NumericProperty(5)
    time = NumericProperty(200)

    def pcrush(self, enemy):

        if self.collide_widget(enemy):
            print "collide!"
            self.LP -= 1
            enemy.center = (200, 70)



class Escape(Widget):
    player1 = ObjectProperty(None)
    enemy = ObjectProperty(None)

    def start(self):
        enx = int(math.ceil(500 * random.random()))
        eny = int(math.ceil(500 * random.random()))
        print enx, eny
        self.player1.center = (50, 300)
        self.enemy.center = (enx, eny)
        print self.enemy.center
        print self.player1.center
 #    enemy = []
 #   for i in range(20):
 #       enemy.append(ObjectProperty(None))
 #       enemy[i].center = (100 * random.random(), 100 * random.random())


    def update(self, dt):
       # for en in self.enemy:
        #    self.p1.pcrush(en)
        self.player1.pcrush(self.enemy)
        self.player1.time -= 1
        if self.player1.time == 0:
            pass

class EscapeApp(App):
    def build(self):
         game = Escape()
         game.start()
         Clock.schedule_interval(game.update, 1.0/10.0)
         return game

if __name__ == "__main__":
    EscapeApp().run()








