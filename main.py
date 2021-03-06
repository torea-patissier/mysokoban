import pygame
import random #Librairie poura voir la nourriture de façon alétatoire
import sys
from config import *

pygame.init()

#Permet d'update le snake et la nourriture
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.generate_food()

    def update(self):
        self.snake.move_snake()
        self.check_head_on_food()
        self.game_over()  

    def draw_game_element(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_head_on_food(self):
        snake_length = len(self.snake.body)
        snake_head_block = self.snake.body[snake_length - 1]
        food_block = self.food.block
        #Si collision avec nourriture alors +1, sinon rien ne se passe 
        if snake_head_block.x == food_block.x and snake_head_block.y == food_block.y:
            self.generate_food()
        else:
            self.snake.body.pop(0)

    def generate_food(self): #Gère si la nourriture pop sur la pos du snake
        should_generate_food = True
        while should_generate_food:
            count = 0
            for block in self.snake.body:
                if block.x == self.food.block.x and block.y == self.food.block.y:
                    count += 1
            if count == 0:
                should_generate_food = False  
            else:
                self.food = Food()  

    def game_over(self):
        snake_length = len(self.snake.body)
        snake_head = self.snake.body[snake_length - 1]
        #Si je sors de la surface GAME OVER
        if ((snake_head.x not in range(0, NB_COL)) or (snake_head.y not in range(0, NB_ROW))):
            self.snake.reset_snake()
            print('GAME OVER')
             
        # Si collision du snake sur lui même également GAME OVER
        for block in self.snake.body[0:snake_length - 1]:
            if block.x == snake_head.x and block.y == snake_head.y:
                print('GAME OVER AUSSI')
                self.snake.reset_snake()

#Classe pour détecter la position d'un élément sur le screen
class Block:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos

#Créer la nourriture
class Food:
    def __init__(self):
        x = random.randint(0,NB_COL - 1) #On met -1 pour éviter de tomber sur 10 (limite de NB_ROW qui est en dehors du screen)
        y = random.randint(0,NB_ROW - 1)

        self.block = Block(x,y)
    
    #Dessine et positionne la nourriture à la coordonnées demandé
    def draw_food(self):
        rect = pygame.Rect(self.block.x * CELL_SIZE , self.block.y * CELL_SIZE , CELL_SIZE, CELL_SIZE) #Definie x, y, w, h
        pygame.draw.rect(screen,pygame.Color(FOOD_COLOR),rect) #Dessine sur le DS

#Créer le snake
class Snake:
    def __init__(self):
        #1er block en x2,y6
        self.body= [Block(2,6),Block(3,6),Block(4,6)]
        self.direction = 'RIGHT' # Au début du jeux le snake se déplace vers la droite 

    def draw_snake(self):

        for block in self.body:

            x_coord = block.x * CELL_SIZE # 2 * 40 soit x = 40px
            y_coord = block.y * CELL_SIZE# 6 * 40 soit y = 240px 

            #Donc le coin supérieur gauche du 1er block = intersection entre 40px x et 240px y

            block_rect = pygame.Rect(x_coord,y_coord,CELL_SIZE,CELL_SIZE) #Definie x, y, w, h
            pygame.draw.rect(screen,pygame.Color('blue'),block_rect) #Dessine sur le DS
    

    def move_snake(self):
        snake_block_count = len(self.body)
        old_head = self.body[snake_block_count - 1]

        if self.direction == 'RIGHT':
            new_head = Block(old_head.x + 1, old_head.y)

        elif self.direction == 'LEFT':
            new_head = Block(old_head.x - 1, old_head.y)

        elif self.direction == 'TOP':
            new_head = Block(old_head.x, old_head.y - 1)

        else:
            new_head = Block(old_head.x, old_head.y + 1)

        self.body.append(new_head)

    def reset_snake(self):
        self.body= [Block(2,6),Block(3,6),Block(4,6)]
        self.direction = 'RIGHT' # Au début du jeux le snake se déplace vers la droite 
#Config
screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE, NB_ROW * CELL_SIZE)) #Display Surface
timer = pygame.time.Clock() #FPS
game_on = True
game = Game()

#Gère la vitesse du Snake
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 400)#millisec

#Afficher la grille
def show_grid():
    for i in range(0, NB_COL):
        for j in range(0, NB_ROW):
            rect = pygame.Rect( i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE) #x,y,w,h RECT
            pygame.draw.rect(screen,pygame.Color('black'),rect,width=1) # Définition du RECT
            #(width=1) permet de faire la grille et non rendre un écran noir car les rect se touchent
 

#Boucle de jeux
while game_on:

    #Fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

        #Maj du snake à la vitesse de 200milisec au lieu de 60 FPS
        if event.type == SCREEN_UPDATE:
            game.update()

        #Capte les touches pressés
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP:
                if game.snake.direction != 'DOWN':
                    game.snake.direction = 'TOP'

            if event.key == pygame.K_DOWN:
                if game.snake.direction != 'TOP':
                    game.snake.direction = 'DOWN'

            if event.key == pygame.K_LEFT:
                if game.snake.direction != 'RIGHT':
                    game.snake.direction = 'LEFT'

            if event.key == pygame.K_RIGHT:
                if game.snake.direction != 'LEFT':
                    game.snake.direction = 'RIGHT'

    
    screen.fill(pygame.Color('white'))
    show_grid() # Appel du RECT de la grille 
    game.draw_game_element()
    pygame.display.update() #Maj de la boucle
    timer.tick(FPS) #Boucle de jeux défini à 60 FPS