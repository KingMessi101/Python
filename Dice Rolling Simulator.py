import pygame, random, sys
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Dice Roller")
font = pygame.font.Font(None, 80)
small = pygame.font.Font(None, 40)

def roll():
    return random.randint(1, 6)

dice = None
run = True
while run:
    screen.fill((255, 255, 255))
    btn = pygame.draw.rect(screen, (0, 150, 0), (140, 200, 120, 50), border_radius=10)
    screen.blit(small.render("Roll", True, (255, 255, 255)), (180, 210))
    
    if dice:
        screen.blit(font.render(str(dice), True, (200, 0, 0)), (180, 100))
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN and btn.collidepoint(e.pos):
            dice = roll()

    pygame.display.flip()

pygame.quit()
sys.exit()
