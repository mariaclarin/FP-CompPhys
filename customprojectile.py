import pygame as pg
import math
import sys

pg.init()
FPS = 60
WIDTH = 1440
HEIGHT = 950
window = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
BLACK = pg.Color( 0 ,  0 ,  0 )
RED = pg.Color(255,0,0)
pg.display.set_caption('Optimochrone')
GRAVITY = 9.8
BALL_SIZE =7 
BALL_POSITION_START = (WIDTH/3, 120)
ACCELERATION_MULTIPLIER =1.5
TIME_MULTIPLIER= 8

class Ball:
    def __init__(self, win, current_ball_position):
        self.win = win
        self.pos = current_ball_position

    def update_ball_position(self, current_ball_position, draw_ball=True):
        self.pos = current_ball_position
        if draw_ball:
            self.draw_ball()

    def draw_ball(self):
        pg.draw.circle(surface=self.win, color=BLACK, center=self.pos, radius=BALL_SIZE)
        print(self.pos)

    def draw_line(self, mouse_pos):
        pg.draw.circle(surface=self.win, color=RED, center=mouse_pos, radius=2)
        pg.draw.line(surface=self.win, color =RED, start_pos=self.pos, end_pos=mouse_pos)

    def draw_ball_path(self, path_list):
        if path_list:
            for position in path_list:
                pg.draw.circle(surface=self.win, color=RED, center=position, radius=2)



    def calculate_angle(self, current_mouse_position):
        x1, y1, x2, y2 = [*self.pos, *current_mouse_position]
        angle= 90 if x1-x2 ==0 else math.atan(abs(y1-y2)/-(x1-x2))*180/math.pi
        return angle
    
    def launch(self, time, current_mouse_position, acceleration_time=ACCELERATION_MULTIPLIER):
        angle = self.calculate_angle(current_mouse_position)
        angle = 180 + angle if angle < 0 else angle
        print(angle)
        #calculate how much time has been passed after the launch function
        start_time = pg.time.get_ticks() 
        acceleration = time * 100 
        x_velocity_start = acceleration_time * acceleration *math.cos(math.radians(-angle))
        y_velocity_start = abs(acceleration_time * acceleration *math.sin(math.radians(-angle)))
        return start_time, x_velocity_start, y_velocity_start
def main():
    path_list=[]
    current_mouse_position =None
    global BALL_POSITION_START
    current_ball_position= BALL_POSITION_START
    #Calling the Ball class object
    ball = Ball(window, BALL_POSITION_START)
    launch = False

    def exit():
        pg.display.quit()
        pg.quit()
        sys.exit()

    bg = pg.image.load("images/background.png")
    header = pg.image.load("images/header.png")

    while True:
        window.blit(bg, (0, 0))

        if launch:
            time_passed_launch= (pg.time.get_ticks() - start_time)/1000 *TIME_MULTIPLIER
            #[1] means y value
            if current_ball_position[1]<= BALL_POSITION_START[1]:
                x, y=BALL_POSITION_START
                x_change = x_velocity_start * time_passed_launch
                y_change = y_velocity_start * time_passed_launch - 0.5 * GRAVITY *pow(time_passed_launch, 2)
                
                #final ball position (freefall motion formula)= starting velocity * time passed + 1/2 * -gravity * time passed**2
                current_ball_position = (x-x_change, y-y_change)
                path_list.append(current_ball_position)
            else:
                launch = False
                current_ball_position = (current_ball_position[0], BALL_POSITION_START)

        ball.update_ball_position(current_ball_position)
        if current_mouse_position is not None:
            ball.draw_line(current_mouse_position)
        ball.draw_ball_path(path_list)
        window.blit(header, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type ==pg.KEYDOWN:
                if event.key ==pg.K_r:
                    launch = False
                    current_ball_position=BALL_POSITION_START
            elif event.type ==pg.MOUSEMOTION:
                current_mouse_position = event.pos
            elif event.type ==pg.MOUSEBUTTONDOWN:
                start_count_time =pg.time.get_ticks()
            elif event.type ==pg.MOUSEBUTTONUP:
                end_count_time = (pg.time.get_ticks() - start_count_time)/1000
                print(str(end_count_time) + " s")
                start_time, x_velocity_start, y_velocity_start = ball.launch(end_count_time, current_mouse_position)
                BALL_POSITION_START = current_ball_position
                path_list = []
                launch=True

        clock.tick(FPS)
        pg.display.update()

if __name__ == "__main__":
    main()