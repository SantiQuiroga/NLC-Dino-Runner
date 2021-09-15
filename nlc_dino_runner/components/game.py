import pygame

from nlc_dino_runner.components.dino import Dino
# from nlc_dino_runner.components.obstacles.cactus import Cactus
from nlc_dino_runner.components.obstacles.obstaclesManager import ObstaclesManager
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS
# SMALL_CACTUS, LARGE_CACTUS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.game_speed = 20
        self.player = Dino()
        self.obstacle_manager = ObstaclesManager()
        # self.cactus_small = Cactus(SMALL_CACTUS)
        # self.cactus_large = Cactus(LARGE_CACTUS)

    def run(self):
        self.playing = True

        while self.playing:
            self.event()
            self.update()
            self.draw()

        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_bg()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        pygame.display.update()
        pygame.display.flip()

    def draw_bg(self):
        img_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (self.x_pos_bg + img_width, self.y_pos_bg))

        if self.x_pos_bg <= -img_width:
            self.screen.blit(BG, (self.x_pos_bg + img_width, self.y_pos_bg))
            self.x_pos_bg = 0

        self.x_pos_bg -= self.game_speed
