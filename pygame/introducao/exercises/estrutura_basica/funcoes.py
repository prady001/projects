# Import the Pygame library
import pygame

# Function to initialize the Pygame library and create a window
def inicializa():
    pygame.init()
    window = pygame.display.set_mode((320, 240))  # Create a window with dimensions (320, 240)
    pygame.display.set_caption('Jogo do Prady')    # Set the window title
    return window

# Function to handle game events
def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # If the user closes the window, return False to exit the game loop
            return False
    return True   

# Function to draw on the window
def desenha(window):
    window.fill((255, 0, 0))           # Fill the window with red
    color = (0, 0, 255)
    pygame.draw.rect(window, color, pygame.Rect(160, 0, 160, 240))      # Draw a blue rectangle
    pygame.display.update()             # Update the window to show changes
    '''vertices = [(250, 0), (500, 200), (250, 400), (0, 200)]
    pygame.draw.polygon(window, (0, 255, 0), vertices)
    pygame.display.update()'''
    return window

game = True

# Main game loop
def game_loop(window):
    while True:
        if not recebe_eventos():    # Check for events and exit the loop if the user closes the window
            return False
        desenha(window)             # Update the window by calling the draw function

# Entry point of the program
if __name__ == "__main__":
    window = inicializa()   # Initialize the Pygame library and create a window
    while game:             # Run the game loop as long as 'game' is True
        game = game_loop(window)
    pygame.quit()           # Quit Pygame when the game loop exits
