import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, CAM_OFFSET_X, CAM_OFFSET_Y

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
playing = True

from scripts import Player, ground, wall, tilemap, attack_particles

camera = pygame.Surface(wall.full_size)

with open(f"./assets/background/map_player.csv", "r") as file:
    input = file.read().splitlines()
    px = py = 0
    for y, row in enumerate(input):
        for x, val in enumerate(row.split(",")):
            if val != "-1":
                px = x * tilemap.tilemap.width
                py = y * tilemap.tilemap.height
                break

clock = pygame.time.Clock()
player = Player((px, py))

while playing:
    screen.fill((0, 0, 0))
    camera.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.dict["size"]
            screen = pygame.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE
            )

    camera.blit(ground.surface, (0, 0))
    camera.blit(wall.surface, (0, 0))

    # pygame.draw.rect(camera, (0, 0, 255), player.collider_rect())
    # pygame.draw.rect(camera, (0, 0, 255), player.rect())
    player.render(camera)
    player.update()

    CAM_OFFSET_X, CAM_OFFSET_Y = (
        -player.pos.x + SCREEN_WIDTH / 2,
        -player.pos.y + SCREEN_HEIGHT / 2,
    )

    attack_particles.update()
    attack_particles.draw(camera)

    screen.blit(camera, (CAM_OFFSET_X, CAM_OFFSET_Y))
    for sprite in attack_particles.sprites():
        sprite.render(screen)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
