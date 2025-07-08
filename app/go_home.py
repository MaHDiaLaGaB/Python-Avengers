import pygame
import random
import math

pygame.init()
WIDTH, HIGHT = 800, 600
screen = pygame.display.set_mode(WIDTH, HIGHT)
pygame.display.set_caption("Catch the following objects")

BACKGROUND = (10, 20, 30)
PLAYER_COLOR = (0, 200, 255)
OBJECT_COLORS = [(255,200,200), (100, 255, 100), (255,255,155)]
TEXT_COLOR = (230, 230, 230)
UI_BG = (30, 40 ,50 , 100)

player_width = 80
player_hight = 20
player_x = WIDTH // 2 - player_width // 2
player_y = HIGHT - 40
player_speed = 8

score = 0
lives = 3
game_over = False
game_pused = False
falling_objects = []
object_speed = 3
spawn_timer = 0
spawn_delay = 30

font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 30)

class FallingObject:

    def __init__(self):
        pass