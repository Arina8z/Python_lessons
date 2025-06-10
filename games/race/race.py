import arcade
import random
import time

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Гонки"
ROAD = "race\images/road.png"
# CAR = "race\images\car.png"
CAR = "race\images/new_car.png"
SPEED_CAR = 10
DELTA_ANGLE = 15
WALL = "race\images\car_down.png"
SOUND_CRASH = "race\sound\crash.mp3"
SOUND_CAR = "race\sound\car_sound.mp3"
MAX_SCORE = 10
SOUND_WIN = "race\sound\sound_bell.mp3"
SOUND_GAME_OVER = "race\sound\game_over.mp3"

class GameWindow(arcade.Window): # конструктор, тут мы всё создаём 
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture(ROAD)
        self.car = Car(CAR, 0.2)
        self.car2 = Wall(WALL, 0.25)
        self.sound_crash = arcade.load_sound(SOUND_CRASH)
        self.sound_car = arcade.load_sound(SOUND_CAR)
        self.attempts = 3
        self.score = 0
        self.lose = False
        self.win = False
        self.sound_win = arcade.load_sound(SOUND_WIN)
        self.sound_game_over = arcade.load_sound(SOUND_GAME_OVER)
    
    def setup(self): # тут мы задаём все координаты и их изменения 
        self.player = arcade.play_sound(self.sound_car)
        self.car.center_x = SCREEN_WIDTH-SCREEN_WIDTH/3
        self.car.center_y = SCREEN_HEIGHT/6.1
        self.car2.center_x = random.randint(0, SCREEN_WIDTH)
        self.car2.change_y = random.randint(5, 8)
        self.car2.center_y = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT*2)
        self.score = 0
    
    def on_draw(self): # мы тут всё рисуем 
        arcade.start_render() 
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.car.draw()
        self.car2.draw()
        arcade.draw_text(f"Счёт: {self.score}", SCREEN_WIDTH/10, 8*SCREEN_HEIGHT/9, (0, 255, 0), 20)
        arcade.draw_text(f"Попытки: {self.attempts}", 3*SCREEN_WIDTH/4, 8*SCREEN_HEIGHT/9, (0, 255, 0), 20)
        if self.win:
            arcade.draw_text("ПОБЕДА!", SCREEN_WIDTH/4, SCREEN_HEIGHT/2, (0, 255, 0), 60)
        if self.lose:
            arcade.draw_text("ПОРАЖЕНИЕ!", SCREEN_WIDTH/4, SCREEN_HEIGHT/2, (255, 0, 0), 40)
    
    def on_update(self, delta_time): # из-за этого у нас работает игра
        if not self.lose:
            if not self.win:
                self.car.update()
                self.car2.update()
                if arcade.check_for_collision(self.car, self.car2):
                    arcade.stop_sound(self.player)
                    arcade.play_sound(self.sound_crash)
                    self.attempts -= 1
                    time.sleep(2)
                    self.setup()
                if self.attempts == 0:
                    arcade.stop_sound(self.player)
                    arcade.play_sound(self.sound_game_over)
                    self.lose = True
                    self.car2.change_y = 0
                if self.car2.top < self.car.bottom+(self.car.center_y-self.car.bottom)/20:
                    self.score += 1
                if self.score == MAX_SCORE:
                    arcade.stop_sound(self.player)
                    arcade.play_sound(self.sound_win)
                    self.win = True
                    self.car2.change_y = 0
    
    def on_key_press(self, key, modifiers): # тут мы задали, что если мы нажимаем на клавиши, то машинка двигается, но пока это так не работает
        if key == arcade.key.RIGHT:
            self.car.change_x = SPEED_CAR
            self.car.angle -= DELTA_ANGLE
        if key == arcade.key.LEFT:
            self.car.change_x = -SPEED_CAR
            self.car.angle += DELTA_ANGLE
    
    def on_key_release(self, key, modifiers): # тут мы задали, что если мы отпускаем клавиши, то машинка перестаёт двигаться, но пока и это тоже не работает
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.car.change_x = 0
            self.car.angle = 0

class Car(arcade.Sprite): # тут всё о главной машинке, где она и что с ней
    def update(self): # тут мы задаём, чтобы машинка двигалась
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH: # тут мы задаём, чтобы машинка не выезжала за края окна
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0

class Wall(arcade.Sprite):
    def update(self):
        self.center_y -= self.change_y
        if self.top < 0:
            self.bottom = random.randint(SCREEN_HEIGHT, SCREEN_HEIGHT*3)
            self.center_x = random.randint(0, SCREEN_WIDTH)
    
window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
