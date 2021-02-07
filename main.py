import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PinPong - Good Luck!")

YELLOW = (255,255,0) #Screen Background
RED = (139,0,0)
GREEN = (0,100,0)

#BORDER = pygame.Rect()

FPS = 60



def draw_window():
    WIN.fill(YELLOW)
    
    RED_IMAGE = pygame.draw.rect(WIN, RED, (WIDTH/10 - 50, HEIGHT/2 - 50, WIDTH/90, HEIGHT/10))  #(x,y,width, height)
    GREEN_IMAGE = pygame.draw.rect(WIN, GREEN, (WIDTH - 40, HEIGHT/2 - 50, WIDTH/90, HEIGHT/10))
    
    pygame.display.update()


def main():
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(FPS) #control the speed of while loop
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
        
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
