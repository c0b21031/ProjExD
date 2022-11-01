import pygame as pg
import sys
from random import randint

class Screen:
    def __init__(self,title,wh,bgimage):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode((wh))
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimage)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Speed:
    key_s = {
        pg.K_1:  10,
        pg.K_2:  20,
    }
    def __init__(self,):
        self.spe=0

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, sp in Speed.key_s.items():
            if key_states[key]:
                self.spe += sp[0]
        return self.spe


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }


    def __init__(self, img, zoom, xy):
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

        self.facing = -1


    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0] + spd.spe
                self.rct.centery += delta[1] + spd.spe
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0] - self.spe
                    self.rct.centery -= delta[1] - self.spe
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)

class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)

def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    scr=Screen("逃げろ!こうかとん",(1600,900),"C:/Users/admin/Documents/ProjExD2022/ex04/pg_bg.jpg")
    
    kkt = Bird("C:/Users/admin/Documents/ProjExD2022/fig/5.png", 2.0, (900, 400))

    bkd = Bomb((255, 0, 0), 20, (-1, -1), scr)

    bkd1 = Bomb((255, 0, 0), 20, (+1, +1), scr)

    bkd2 = Bomb((255, 0, 0), 20, (+1, +1), scr)

    spd=Speed()


    clock = pg.time.Clock()
    
    while True:
        scr.blit() 

        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return
            
        kkt.update(scr)
        bkd.update(scr)
        bkd1.update(scr)
        bkd2.update(scr)

        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
