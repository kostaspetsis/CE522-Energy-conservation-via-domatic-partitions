import pygame


screen = None#pygame.display.set_mode((720, 480))
clock = None#pygame.time.Clock()
FPS = 60  # Frames per second.

BLACK = None#(0, 0, 0)
WHITE = None#(25, 255, 255)
RED = None#(255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SAND = (252,233,138)
w=32
h=32

rect = None#pygame.Rect((0, 0), (32, 32))
image = None#pygame.Surface((32, 32))
#image .fill(WHITE)  
#display()
external_funcs = []

def display():
    global BLACK,WHITE,RED,GREEN,BLUE,rect,image,external_funcs,screen,clock,FPS
    quit = False
    while quit == False:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    rect.move_ip(0, -2)
                elif event.key == pygame.K_s:
                    rect.move_ip(0, 2)
                elif event.key == pygame.K_a:
                    rect.move_ip(-2, 0)
                elif event.key == pygame.K_d:
                    rect.move_ip(2, 0)
                elif event.key == pygame.K_ESCAPE:
                    quit=True
                    break
        screen.fill(BLACK)
        screen.blit(image, rect)
        for func in external_funcs:
            func()
        pygame.display.update()  # Or pygame.display.flip()
def text_to_screen(screen, text, x, y, size = 50,
            color = (200, 000, 000), font_type = 'data/fonts/orecrusherexpand.ttf'):
    try:

        text = str(text)
        font = pygame.font.Font(pygame.font.get_default_font(), size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception as e:
        print ('Font Error, saw it coming')
        raise e
def init_graphics(_w=500,_h=500):
    global BLACK,WHITE,RED,GREEN,BLUE,rect,image,external_funcs,screen,clock,FPS
    global w,h
    w=_w
    h=_h
    print("Initializing graphics")
    successes, failures = pygame.init()
    print("{0} successes and {1} failures".format(successes, failures))


    screen = pygame.display.set_mode((w,h))
    clock = pygame.time.Clock()
    FPS = 60  # Frames per second.

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    rect = pygame.Rect((0, 0), (32, 32))
    image = pygame.Surface((w, h))
    image.fill(SAND)  
def add_loop_function(func):
    global external_funcs
    external_funcs.append(func)
