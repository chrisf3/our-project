'''
Öffnet ein Fenster, das wieder geschlossen werden kann. (überaschend schwer hinzukriegen)
'''
import pygame
pygame.init()

#%%
pygame.display.set_mode((640,480),pygame.RESIZABLE)

clock = pygame.time.Clock()
while True:
    if pygame.event.peek(pygame.QUIT) or pygame.event.peek(pygame.KEYDOWN):
        break
    #pygame.event.pump()
    clock.tick(30)
pygame.display.quit()
