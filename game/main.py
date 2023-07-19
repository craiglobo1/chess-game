import pygame as pg
import sys
import os
# from scripts import *

class Game:
    def __init__(self) -> None:
        pg.init()
        info = pg.display.Info()
        w = info.current_w
        h = info.current_h
        os.environ["SDL_VIDEO_CENTERED"] = '1'
        self.win = pg.display.set_mode((w, h-30), pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.fps = 60

        pg.display.set_caption("Game")

        self.playing = False

    def load(self):
        pass


    def update(self):
        pg.display.update()
        self.clock.tick(self.fps)
        mouse_pos = pg.mouse.get_pos()
        mouse_buttons = pg.mouse.get_pressed()

        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.quit()

            if event.type == pg.VIDEORESIZE:
                self.win = pg.display.set_mode(
                    (event.w, event.h), pg.RESIZABLE)


    def draw(self):
        # self.win.blit(self.bg_img, (0,0))
        self.win.fill((255,255,255))

    def run(self):
        self.load()
        self.running = True

        while self.running:
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(60)

    def quit(self):
        pg.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()