import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koukaton = pg.image.load ("ex01/fig/3.png")#練習２こうかとん画像生成
    koukaton = pg.transform.flip(koukaton,True,False)#練習２こうかとん画像反転
    koukaton_list =[koukaton,pg.transform.rotate(koukaton,5),pg.transform.rotate(koukaton,15),pg.transform.rotate(koukaton,10)]#練習３リスト生成
    tmr = 0
 
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%3200
        print(x,tmr)
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img,True,False), [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        #screen.blit(koukaton,[100,100])#練習２こうかとん画像貼り付け
        screen.blit(koukaton_list[tmr%3],[300,200])
        pg.display.update()#
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()