import sys
import pygame
import math

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
playing = True

rect = pygame.Rect(0, 0, 50, 50)
rect.centerx = width // 2
rect.centery = height // 2
rect_center = pygame.Vector2(*rect.center)

dist = pygame.Vector2(0, -100)
offset = 40
angle = 0
down = True
slashing = False
speed = 1

while playing:
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            slashing = True
            # if down:
            #     dist = pygame.Vector2(0, -100).rotate(220)
            # else:
            #     dist = pygame.Vector2(0, -100).rotate(-40)
            # down = not down

    vec_angle = angle - offset + 180
    # vec_angle = vec_angle + rect_center.angle_to(pygame.mouse.get_pos())
    vec_angle += math.degrees(math.atan2(rect.centery - my, rect.centerx - mx)) + 180

    pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.draw.circle(
        screen,
        (255, 255, 255),
        (rect_center - dist.rotate(vec_angle)).xy,
        10,
    )
    # print(vec_angle)

    if slashing:
        if down:
            if angle < 260:
                # dist.rotate_ip(speed)
                angle += speed
            else:
                slashing = False
                down = False
        else:
            if angle > 0:
                # dist.rotate_ip(-speed)
                angle -= speed
            else:
                slashing = False
                down = True

    pygame.display.update()
    clock.tick()

pygame.quit()
sys.exit()
