import pygame
import random #Librairie poura voir la nourriture de façon alétatoire
import sys
from config import *

pygame.init()

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

    def draw_snake(self):

        for block in self.body:

            x_coord = block.x * CELL_SIZE # 2 * 40 soit x = 40px
            y_coord = block.y * CELL_SIZE# 6 * 40 soit y = 240px 

            #Donc le coin supérieur gauche du 1er block = intersection entre 40px x et 240px y

            block_rect = pygame.Rect(x_coord,y_coord,CELL_SIZE,CELL_SIZE) #Definie x, y, w, h
            pygame.draw.rect(screen,pygame.Color('blue'),block_rect) #Dessine sur le DS


        
screen = pygame.display.set_mode(size=(NB_COL * CELL_SIZE, NB_ROW * CELL_SIZE)) #Display Surface
timer = pygame.time.Clock() #FPS
game_on = True

food = Food()
snake = Snake()

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

    
    screen.fill(pygame.Color('white'))
    show_grid() # Appel du RECT de la grille

    food.draw_food() 
    snake.draw_snake()
    
    pygame.display.update() #Maj de la boucle
    timer.tick(FPS) #Boucle de jeux défini à 60 FPS