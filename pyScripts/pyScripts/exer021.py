import pygame as pg
pg.init()
pg.mixer.music.load('FundoDaGrotaRemix.mp3')
pg.mixer.music.play()
pg.mixer.music.set_volume(0.05)
pg.event.wait()
input()
