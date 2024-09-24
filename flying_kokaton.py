import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png") #練習2
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    haikei_img = pg.transform.flip(bg_img, True, False) #練習7-1
    kk_rct = kk_img.get_rect() #練習8-1
    kk_rct.center = 300, 200 #練習8-1

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        dx, dy = 0, 0
        if key_lst[pg.K_UP]:
            dy = -1
        elif key_lst[pg.K_DOWN]:
            dy = +1
        elif key_lst[pg.K_RIGHT]:
            dx = +2
        elif key_lst[pg.K_LEFT]:
            dx = -1
        else:
            dx = -1

        kk_rct.move_ip(dx, dy)

        x = -(tmr % 3200) #練習6
        screen.blit(bg_img, [x, 0])
        screen.blit(haikei_img, [x+1600, 0]) #練習7-1
        screen.blit(bg_img, [x+3200, 0]) #練習7-2
        screen.blit(haikei_img, [x+4800, 0]) #練習7-2
        screen.blit(kk_img, kk_rct) #練習4 ->　練習8-5
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()