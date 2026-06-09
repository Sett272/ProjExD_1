import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    koukaton = pg.image.load("fig/3.png") # 3こうかとん読み込み
    kk = pg.transform.flip(koukaton, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr
        screen.blit(bg_img, [-x, 0]) #5
        screen.blit(kk, [300,200]) #4こうかとんsurfaceに貼り付け
        pg.display.update()
        tmr += 1        
        clock.tick(200) #6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()