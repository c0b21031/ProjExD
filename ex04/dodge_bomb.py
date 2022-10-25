import pygame as pg
import sys
from random import randint

def check_bound(obj_rct,scr_rct):
    #obj_rctはこうかトンrctまたは爆弾rct
    #scr_rctはスクリーンrct
    yoko,tate= +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko=-1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate=-1
    return yoko,tate

#bomb2を次第に大きくする関数()
#def change_large(change_y):
#    if change_y <0.40:
#        change_y += 0.01
#    else:
#        change_y=0.01
#    return change_y 

def main():
    #ウィンドウ生成
    pg.display.set_caption("逃げろ!こうかとん")
    scrn_sfc=pg.display.set_mode((1600,900))
    scrn_rct=scrn_sfc.get_rect()

    #背景のsurfaceの生成
    bg_sfc=pg.image.load("C:/Users/admin/Documents/ProjExD2022/ex04/pg_bg.jpg")
    bg_rct=bg_sfc.get_rect()

    #鳥のsurfaceの生成
    tori_sfc=pg.image.load("C:/Users/admin/Documents/ProjExD2022/fig/5.png")
    tori_sfc=pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct=tori_sfc.get_rect()
    tori_rct.center=900,400


    #爆弾のSurfaceの生成
    bomb_sfc = pg.Surface((20, 20)) # 空のSurface
    bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn_rct.width)
    bomb_rct.centery = randint(0, scrn_rct.height)    

    
    
    #爆弾2のSurfaceの生成
    change_y=0.01
    bomb2_sfc=pg.image.load("C:/Users/admin/Documents/ProjExD2022/ex04/enemy.png")
    bomb2_sfc=pg.transform.rotozoom(bomb2_sfc,0,0.20)
    bomb2_rct=tori_sfc.get_rect()
    bomb2_rct.centerx = randint(0, scrn_rct.width)
    bomb2_rct.centery = randint(0, scrn_rct.height)

    vx,vy=+1,+1
    #背景画像のbilt
    clock=pg.time.Clock()
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)

        for event in pg.event.get():
            if event.type==pg.QUIT:
                return

        key_states=pg.key.get_pressed()
        if key_states[pg.K_UP]:   tori_rct.centery -= 1
        if key_states[pg.K_DOWN]:  tori_rct.centery += 1
        if key_states[pg.K_LEFT]:  tori_rct.centerx -= 1
        if key_states[pg.K_RIGHT]: tori_rct.centerx += 1
        yoko,tate =check_bound(tori_rct,scrn_rct)
        if yoko==-1:
            if key_states[pg.K_LEFT]: 
                tori_rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        if tate == -1:
            if key_states[pg.K_UP]: 
                tori_rct.centery += 1
            if key_states[pg.K_DOWN]:
                tori_rct.centery -= 1   

        scrn_sfc.blit(tori_sfc, tori_rct)

        yoko,tate=check_bound(bomb_rct, scrn_rct)
        yoko,tate=check_bound(bomb2_rct,scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx,vy)
        bomb2_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        scrn_sfc.blit(bomb2_sfc,bomb2_rct)

        

        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb2_rct): # こうかとんrctが爆弾1rctか爆弾2rctと重なったら
            return

        pg.display.update()
        clock.tick(1000)



if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()