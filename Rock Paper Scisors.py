import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)
YELLOW = (255, 255, 100)

title_font = pygame.font.Font(None, 70)
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 32)

def make_text_image(text, color):
    surf = pygame.Surface((150, 150))
    surf.fill(color)
    text_render = font.render(text, True, BLACK)
    rect = text_render.get_rect(center=(75, 75))
    surf.blit(text_render, rect)
    return surf

rock_img = make_text_image("Rock", RED)
paper_img = make_text_image("Paper", BLUE)
scissors_img = make_text_image("Scissors", GREEN)

choices = ["Rock", "Paper", "Scissors"]

img_positions = {
    "Rock": (120, 200),
    "Paper": (320, 200),
    "Scissors": (520, 200)
}

user_choice = None
computer_choice = None
result = ""
player_score = 0
computor_score = 0

def get_result(user, comp):
    if user == comp:
        return "its a tie"
    elif (user == "Rock" and comp == "Scissors") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Scissors" and comp == "Paper"):
        return "you win"
        
    else:
        return "you lose"
    
def draw_button(text, x, y, w, h, color):
        rect = pygame.Rect(x, y, w, h)
        pygame.draw.Rect(screen, color, rect, border_radius-15)
        label = small_font.render(text, True, BLACK)
        screen.blit(label, (x + (w - label.get_width()) // 2, y + (h - label.get_height()) // 2))
        return rect

clock = pygame.time.Clock()
running = True

while running:
 screen.fill(LIGHT_GRAY)

 title = title_font.render('Rock Paper Scissors', True, BLACK)
 screen.blit(title, (160, 50))
 
 rects = {}
 for name, pos in img_positions.items():
    if name == "Rock":
        screen.blit(rock_img, pos)
        rects[name] = pygame.Rect(pos[0], pos[1], 150, 150)
    elif name == "Paper":
        screen.blit(paper_img, pos)
        rects[name] = pygame.Rect(pos[0], pos[1], 150, 150)
    else:
        screen.blit(scissors_img, pos)
        rects[name] = pygame.Rect(pos[0], pos[1], 150, 150)

    if user_choice:
        result_text = font.render(result, True, BLACK)
        user_text = small_font.render(f"You: {user_choice}", True, BLACK)
        comp_text = small_font.render(f"Computer: {computer_choice}", True, BLACK)
