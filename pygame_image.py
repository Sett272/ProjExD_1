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
    bg_flip = pg.transform.flip(bg_img, True, False)
    kk_rct = koukaton.get_rect() #10 動き
    kk_rct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: #上矢印
            kk_rct.move_ip(0, -1)
        elif key_lst[pg.K_DOWN]: #下矢印
            kk_rct.move_ip(0, 1)
        elif key_lst[pg.K_LEFT]: #左矢印
            kk_rct.move_ip(-1, 0)
        elif key_lst[pg.K_RIGHT]: #右矢印
            kk_rct.move_ip(1, 0)
        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #5 右に移動
        screen.blit(bg_flip, [-x+1600, 0]) #7 画像延長#8 画像反転
        screen.blit(bg_img, [-x+3200, 0]) #9 ループ
        screen.blit(kk, kk_rct) #4こうかとんsurfaceに貼り付け

        pg.display.update()
        tmr += 1        
        clock.tick(200) #6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()