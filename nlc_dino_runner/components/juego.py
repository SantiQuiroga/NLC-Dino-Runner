import pygame

from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS


class Juego:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.reloj = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.jugando = False
        self.x_pos_bg = 0
        self.y_pos_bg = 360
        self.velocidad_del_juego = 20

    def correr(self):
        self.jugando = True
        while self.jugando:
            self.evento()
            self.actualizar()
            self.dibujar()
        pygame.quit()

    def evento(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.jugando = False

    def actualizar(self):
        pass

    def dibujar(self):
        self.reloj.tick(FPS)
        self.pantalla.fill((255, 255, 255))
        self.dibujar_fondo()
        pygame.display.update()
        pygame.display.flip()

    def dibujar_fondo(self):
        ancho_de_imagen = BG.get_width()
        self.pantalla.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.pantalla.blit(BG, (self.x_pos_bg + ancho_de_imagen, self.y_pos_bg))
        if self.x_pos_bg <= -ancho_de_imagen:
            self.pantalla.blit(BG, (self.x_pos_bg + ancho_de_imagen, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.velocidad_del_juego
