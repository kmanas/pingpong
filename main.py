import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PinPong Game")

YELLOW = (255,255,0)
RED = (139,0,0)
GREEN = (0,100,0)

BORDER = pygame.Rect()

FPS = 60

TIGER_IMAGE
FROG_IMAGE

def draw_window():
    WIN.fill(YELLOW)
    pagame.draw_rect(WIN, RED, BORDER)
    pagame.draw_rect(WIN, GREEN, BORDER)
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
