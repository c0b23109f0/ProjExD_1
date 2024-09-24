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
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = -(tmr % 3200) #練習6
        screen.blit(bg_img, [x, 0])
        screen.blit(haikei_img, [x+1600, 0]) #練習7-1
        screen.blit(bg_img, [x+3200, 0]) #練習7-2
        screen.blit(haikei_img, [x+4800, 0]) #練習7-2
        screen.blit(kk_img, [300, 200]) #練習4
        pg.display.update()
        tmr += 1        
        clock.tick(20000) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()