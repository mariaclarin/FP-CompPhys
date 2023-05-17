import pygame

# Pygame initialization
pygame.init()
pygame.font.init()

# Define the background colour using RGB color coding
background_colour = (255, 255, 255)
header_colour = (192, 192, 192)  # Gray color for the header

# Define the dimensions of the screen object (width, height)
screen_width = 1440
screen_height = 950
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption of the screen
pygame.display.set_caption('Optimochrone')

# Fill the background colour to the screen
screen.fill(background_colour)

# Set up the font
font = pygame.font.Font(None, 28)

# Render the header text
header_text = font.render('Optimochrone', True, pygame.Color('black'))

# Calculate the position to align the header text at the top
header_x = 0
header_y = 0

# Calculate the dimensions of the header based on the text size
header_width = screen_width
header_height = 40

# Draw the header rectangle with the gray color
header_rect = pygame.Rect(header_x, header_y, header_width, header_height)
pygame.draw.rect(screen, header_colour, header_rect)

# Blit the header text onto the screen
screen.blit(header_text, (header_x + 5, header_y + 5))

# Load the image of the cycloid curve
curve_image = pygame.image.load('flp_linear.webp')

# Get the dimensions of the curve image
curve_image_width = curve_image.get_width()
curve_image_height = curve_image.get_height()

# Calculate the position to align the image on the right side
image_x = screen_width - curve_image_width - 25
image_y = header_y + header_height + 25

# Blit the curve image onto the screen
screen.blit(curve_image, (image_x, image_y))

# Cycloid curve information
curve_info = [
     "Linear Curve",
    "-----------------",
    "  The brachistochrone curve is the curve that allows a mass point, starting from rest and ",
    "subject to gravity without friction, to slide between two fixed points in the shortest ",
    "possible time compared to all other curve options (Theilmann, 2016). In curve fitting,",
    "a linear curve refers to a curve where the relationship between ",
    "the curve's parameters and the curve itself is linear. This includes ",
    " curves such as lines, polynomials, Chebyshev series, and any curve that can be ",
    "expressed as a linear combination of a set of curves. The linearity of these curves makes ",
    "calculations simpler because the solution can be expressed using basic linear algebra.",
    "     ",
    "  In two-variable linear regression, we utilize a linear equation involving  ",
    "a single independent variable. The equation takes the form:",
    "     y = a + bx",
    "     ",
    "     Here, 'a' and 'b' are constant values.",
    "     ",
    "  The independent variable is denoted as 'x,' while 'y' represents the dependent variable.",
    " Generally, a specific value is selected for the independent variable,",
    " allowing us to determine the corresponding value of the dependent variable through solving.",
    "      ",
    "The plotted line in the given graph highlights the issue of employing a linear relationship to fit a curved relationship. ",
    " Despite a high R-squared value, it is evident that the model is insufficient.",
    " It is necessary to utilize curve fitting methods instead.",

]

# Calculate the position to align the text on the left side
text_x = header_x
text_y = image_y

# Render the text on separate surfaces
text_surfaces = []
for line in curve_info:
    text_surface = font.render(line, True, pygame.Color('black'))
    text_surfaces.append(text_surface)

# Blit the text surfaces onto the screen
for text_surface in text_surfaces:
    screen.blit(text_surface, (text_x, text_y))
    text_y += text_surface.get_height() + 10

# Update the display using flip
pygame.display.flip()

# Variable to keep our game loop running
running = True

# Game loop
while running:
    # For loop through the event queue
    for event in pygame.event.get():
        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False

# Exit Pygame
pygame.quit()