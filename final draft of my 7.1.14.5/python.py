import pygame as py
import time
def display_score():
    ct = int(py.time.get_ticks()/1000) - st
    score_surf = font.render(f'Score :- {ct} :)',False,(64,64,64))
    sr = score_surf.get_rect(center = (400,30))
    window.blit(score_surf,sr)
    print(ct)
    return ct

py.init()
py.mixer.init()
i = 1
paro = py.mixer.Sound('paro.mp3')
omahi = py.mixer.Sound('omahi.mp3')
bsong = py.mixer.Sound('bsong.mp3')
tungi = py.mixer.Sound('tungi.mp3')
tullu = py.mixer.Sound('tullu.mp3')
bhu = py.mixer.Sound('bhu.mp3')
kya = py.mixer.Sound('kya.mp3')
clock = py.time.Clock()
window = py.display.set_mode((800,500))

py.display.set_caption(' Beauty Of Failure!')
font = py.font.Font(None, 32)
text = font.render('my first game', True,(0,255,0))
textgo = font.render('  RONALDO V/S KUTTA ', True,(0,255,0))
textRect = text.get_rect()
textRectgo = textgo.get_rect()
mess = font.render('Click Space To Continue   ',True,(255,0,0))
vs = font.render(' V / S ',True,(0,0,0))
textRect.center = (400,30)
textRectgo.topleft = (0,0)
vsrect = vs.get_rect()
vsrect.topleft = (350,220)
a = True
sky = py.image.load('sky.png').convert()
plr = py.image.load('ptm.png').convert_alpha()
grd = py.image.load('g.jpg').convert()
kty = py.image.load('kutta.png').convert_alpha()
ga = True
st = 0
src = 0
plr2 = plr.get_rect(topleft=(40,330))
kty2 = kty.get_rect(topleft=(400,355))
grv = 0
sunil = py.image.load('sunil.png').convert_alpha()
gg = py.image.load('gg.png')
sunilr = sunil.get_rect(topleft = (480,110))
ggr = gg.get_rect(topleft= (100,110))
messr = mess.get_rect(center = (390,90))
obst  = py.USEREVENT + 1
i = 1
py.time.set_timer(obst,900)



while a:
    for event in py.event.get():
        if event.type == py.KEYDOWN:
            if event.key == py.K_1:
                py.mixer.pause()
            if event.key == py.K_q:
                omahi.play()
            if event.key == py.K_w:
                bsong.play()
            if event.key == py.K_e:
                tungi.play()
            if event.key == py.K_r:
                bhu.play()
            if event.key == py.K_t:
                paro.play()
            if event.key == py.K_y:
                kya.play()          
        if event.type == py.QUIT:
               a = False
        
        if ga:             
            if event.type == py.MOUSEBUTTONDOWN:
                if plr2.collidepoint(event.pos) and plr2.bottom >= 430:
                    grv = -20
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE and plr2.bottom >= 430:
                    tullu.play()
                    grv =-23
        else:        
            
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    ga = True
                    kty2.left = 800
                    st = int(py.time.get_ticks()/1000)
            if event.type == obst:
                if ga:
                    print('test')
              
    if ga:               
        window.blit(sky,(0,0))
        window.blit(grd,(0,430))
        window.blit(plr,plr2)
        window.blit(kty,kty2)
        
        src = display_score()
        kty2.x -= 5
        if kty2.x < -100:
            kty2.x  = 800
        grv += 1
        plr2.y += grv
        if plr2.bottom > 430:
            plr2.bottom = 430
    

    
    if kty2.colliderect(plr2):
       
       ga = False
       window.fill((34, 105, 212))
       window.blit(sunil,sunilr)
       window.blit(textgo,(250,30))
        
       window.blit(gg,ggr)
       window.blit(vs,vsrect)
       window.blit(mess,messr)
       sm = font.render(f'YOUR  SCORE : "{src}" :-)',False,(0,0,0))
       smr = sm.get_rect(center = (370,450))
     
       if src == 0:
            window.blit(mess,messr)
       
       else:
            window.blit(sm,smr)


    
           
    clock.tick(60)
    py.display.update()
