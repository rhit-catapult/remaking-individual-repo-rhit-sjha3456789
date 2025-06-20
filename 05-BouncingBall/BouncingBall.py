import pygame
import sys
import random
import time

ball_radius = 25
# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        self.x = x
        self.y = y
        self.speed_x = random.randint(1, 5)
        self.speed_y = random.randint(1,5)
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    def draw(self):
        pygame.draw.circle(self.screen,self.color, (self.x, self.y), ball_radius)
    def collide(self, ):
        if self.x < 0 + ball_radius or self.x > self.screen.get_width() - ball_radius:
            self.speed_x *= -1
        if self.y < 0 + ball_radius or self.y > self.screen.get_height() - ball_radius:
            self.speed_y *= -1


def main():
    pygame.init()
    screen = pygame.display.set_mode((200, 600))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()
    ball1 = Ball(screen, random.randint(ball_radius, screen.get_width() - ball_radius),
                 random.randint(ball_radius, screen.get_width() - ball_radius))
    ball2 = Ball(screen, random.randint(ball_radius, screen.get_width() - ball_radius),
                 random.randint(ball_radius, screen.get_width() - ball_radius))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))


        ball1.move()
        ball1.collide()
        ball1.draw()
        ball2.move()
        ball2.collide()
        ball2.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
