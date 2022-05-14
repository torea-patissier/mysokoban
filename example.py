import pygame
import sys 
pygame.init()

screen = pygame.display.set_mode((400,500)) # Défini la taille de l'écran DISPLAY SURFACE
timer = pygame.time.Clock() # Défini le nombre de FPS

my_surface = pygame.Surface((100,100)) # Surface (option 1)
my_rect = pygame.Rect(75,100,150,150) # Rect (option 2)

game_on= True # Initialise la boucle de jeux à true, on la passe à false pour stopper le jeux

while game_on: #Boucle de jeux

    for event in pygame.event.get(): #Ferme la fenêtre si je décide de quitter l'application
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    screen.fill(pygame.Color('green'))#Colorer le background

    my_surface.fill((35,0,219)) # Colorer la surface (option1)
    screen.blit(my_surface,(150,200)) # Ajouter une surface à la DS (!) 150 = x 200 = y (option1)

    pygame.draw.rect(screen,pygame.Color('purple'),my_rect) #Ajouter un rect à la DS (option2)

    pygame.display.update() #Pour afficher les MAJ
    timer.tick(60) # La boucle de jeux est executé 60 fois par seconde


