import pygame
import sys
import random


def main():
    pygame.init()
    pygame.display.set_caption("Winning Smile")
    screen = pygame.display.set_mode((640, 480))
    eye_x = 0
    eye_y = 0
    clock = pygame.time.Clock()
    while True:
        # TODO 4: Set the clock speed to 60 fps
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 3: Make the eye pupils move with Up, Down, Left, and Right keys
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                eye_x = eye_x - random.randint(0, 10)
            if pressed[pygame.K_RIGHT]:
                eye_x = eye_x + random.randint(0, 10)
            if pressed[pygame.K_UP]:
                eye_y = eye_y - random.randint(0, 10)
            if pressed[pygame.K_DOWN]:
                eye_y = eye_y + random.randint(0, 10)
        screen.fill((255, 255, 255))  # white

        # API --> pygame.draw.circle(screen, color, (x, y), radius, thickness)

        pygame.draw.circle(screen, (0, 255, 0), (320, 240), 210)  # yellow circle
        pygame.draw.circle(screen, (0, 0, 0), (320, 240), 210, 4)  # black outline

        pygame.draw.circle(screen, (225, 0, 225), (240, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (240, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (242+eye_x, 162+eye_y), 7)  # black pupil

        pygame.draw.circle(screen, (225, 0, 225), (400, 160), 25)  # white eye
        pygame.draw.circle(screen, (0, 0, 0), (400, 160), 25, 3)  # black outline
        pygame.draw.circle(screen, (0, 0, 0), (398+eye_x, 162+eye_y), 7)  # black pupil

        # TODO 1: Draw a nose

        pygame.draw.circle(screen, pygame.Color(100, 100, 255), (320, 240), 80)

        # TODO 2: Draw a mouth
        # Suggestion: color (0,0,0), x 230, y 320, width 180, height 30
        pygame.draw.rect(screen, pygame.Color(0, 0, 0), (200, 300, 100, 10))

        pygame.display.update()


main()
