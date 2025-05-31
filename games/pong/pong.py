import arcade
import os
import sys
import random

def resource_path(relative_path):
    """ Возвращает абсолютный путь к ресурсу. Работает как в .exe, так и в обычном режиме """
    if hasattr(sys, '_MEIPASS'):
        # Если запущено из .exe
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        # Если запущено обычным образом
        return os.path.join(os.path.dirname(__file__), relative_path)

WIDTH = 800
HEIDHT = 600
TITLE = "PONG"
R, G, B = 100, 180, 200
BALL = "resources\images\Ball.png"
# PADLE = "Python_lessons\padle.png"
SPEED_X = 9
SPEED_Y = 9
DELTA = 2
SPEED_PAD = 10
WIN = 25
SOUND_BALL = "resources\sound\sound_ball.mp3"
# SOUND_WIN = "Python_lessons\short_applause_normal.mp3"
SOUND_GAME_OVER = "resources\sound\game_over.mp3"
BG = "resources\images\Bag_round.jpg"
# BG_SOUND = "Python_lessons/bg_sound.mp3"
PADLE = "resources\images/boat.png"
BG_SOUND = "resources\sound\sound_lake.mp3"
SOUND_WIN = "resources\sound\sound_bell.mp3"
BALL2 = "resources/images/ball2.png"

class GameWindow(arcade.Window): # тут всё создаём
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture(resource_path(BG))
        self.ball = Ball(resource_path(BALL), 0.05)
        # self.padle = Padle(PADLE, 0.1)
        self.padle = Padle(resource_path(PADLE), 1)
        self.score = 0
        self.attempts = 3
        self.lose = False
        self.win = False
        self.level3 = False
        self.ball_sound = arcade.load_sound(resource_path(SOUND_BALL))
        self.sound_win = arcade.load_sound(resource_path(SOUND_WIN))
        self.sound_game_over = arcade.load_sound(resource_path(SOUND_GAME_OVER))
        self.bg_sound = arcade.load_sound(resource_path(BG_SOUND))
        self.player = arcade.play_sound(self.bg_sound) # создаём плеер для этой музыки
        self.level = 1
        
    def setup(self, speed_x, speed_y): # тут мы задаём все координаты и их изменения
        if self.level3:
            self.ball2 = Ball(resource_path(BALL2), 0.15)
            self.ball2.center_x = random.randint(10, WIDTH-10)
            self.ball2.center_y = 3*HEIDHT/4
            self.ball2.change_x = speed_x
            self.ball2.change_y = speed_y
        self.ball.center_x = random.randint(10, WIDTH-10)
        self.ball.center_y = 3*HEIDHT/4
        self.ball.change_x = speed_x
        self.ball.change_y = speed_y
        
        self.padle.center_x = WIDTH/2
        self.padle.center_y = HEIDHT/4

    def on_draw(self): # мы тут всё рисуем
        arcade.start_render()
        # arcade.set_background_color((R, G, B))
        arcade.draw_texture_rectangle(WIDTH/2, HEIDHT/2, WIDTH, HEIDHT, self.bg)
        self.ball.draw()
        self.padle.draw()
        arcade.draw_text(f"SCORE: {self.score}", 20, HEIDHT - 50, (90, 167, 229), 20) # 1 - что напишем, 2?, 3 - на сколько подвинем в отношении высоты, 4 - цвет, 5 - шрифт
        arcade.draw_text(f"ATTEMPTS: {self.attempts}", WIDTH - 200, HEIDHT - 50, (90, 167, 229), 20)
        arcade.draw_text(f"LEVEL: {self.level}", WIDTH/2-100, HEIDHT-50, (255, 0, 0), 20)
        if self.win:
            arcade.draw_text("WIN!!!", WIDTH - 500, HEIDHT - 250, (0, 255, 0), 50)
        if self.lose:
            arcade.draw_text("GAME OVER", WIDTH - 620, HEIDHT - 250, (255, 0, 0), 50)
        if self.level3:
            self.ball2.draw()
        
    def on_update(self, delta_time): # из-за этого у нас работает игра
        if not self.lose:
            if not self.win:
                self.ball.update()
                if self.level3:
                    self.ball2.update()
                self.padle.update()
                if arcade.check_for_collision(self.ball, self.padle):
                    arcade.play_sound(self.ball_sound)
                    self.ball.bottom = self.padle.top # но это не очень top - верх, bottom - низ
                    self.ball.change_y *= -1
                    if self.level3:
                        self.ball2.bottom = self.padle.top
                        self.ball2.change_y *= -1
                    self.score += 1
                if self.score == WIN:
                    arcade.stop_sound(self.player) # общая музыка тут должна выключаться 
                    arcade.play_sound(self.sound_win) # музыку выигрыша проигрываем
                    self.win = True
                if self.score == 10:
                    self.setup(SPEED_X+DELTA, SPEED_Y+DELTA)
                    self.level = 2
                    self.score += 1
                if self.score == 20:
                    self.level3 = True
                    self.setup(SPEED_X, SPEED_Y)
                    self.level = 3
                    self.score += 1
                    
                if self.ball.bottom < 0:
                    self.attempts -= 1
                    self.setup(SPEED_X, SPEED_Y)
                if self.level3 and self.ball2.bottom < 0:
                    self.attempts -= 1
                    self.setup(SPEED_X, SPEED_Y)
                if self.attempts == 0:
                    arcade.stop_sound(self.player) # общая музыка тут должна выключаться 
                    arcade.play_sound(self.sound_game_over) # музыку проигрыша проигрываем
                    self.lose = True
            
    def on_key_press(self, key, modifiers): # тут мы задали, что если мы нажимаем на клавиши, то ракетка двигается
        if key == arcade.key.RIGHT:
            self.padle.change_x = SPEED_PAD
        if key == arcade.key.LEFT:
            self.padle.change_x = -SPEED_PAD
    
    def on_key_release(self, key, modifiers): # тут мы задали, что если мы отпускаем клавиши, то ракетка перестаёт двигаться
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.padle.change_x = 0

class Ball(arcade.Sprite): # тут всё, что есть только у мяча, и где он, и всё о мяче
    def update(self):
        self.center_x += self.change_x
        if self.right > WIDTH or self.left < 0:
            self.change_x *= -1
        
        self.center_y += self.change_y
        if self.top > HEIDHT or self.bottom < 0:
            self.change_y *= -1

class Padle(arcade.Sprite): # тут всё о ракетке, что у неё есть, и где она и всё такое
    def update(self):
        self.center_x += self.change_x
        # if self.right > WIDTH or self.left < 0:
        #     self.change_x *= -1
        if self.right > WIDTH:
            self.right = WIDTH
        if self.left < 0:
            self.left = 0

window = GameWindow(WIDTH, HEIDHT, TITLE)
window.setup(SPEED_X, SPEED_Y)

arcade.run()
