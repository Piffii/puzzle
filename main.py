import pygame
import sys
import os


pygame.init()
FPS = 60
start = False
size = WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Мистер Банеееейн, Mr. Bannaaaame')
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# группы спрайтов
all_sprites = pygame.sprite.Group()
start_screen_sprites = pygame.sprite.Group()
main_view_sprites = pygame.sprite.Group()
left_view_sprites = pygame.sprite.Group()
right_view_sprites = pygame.sprite.Group()
rules_screen_sprites = pygame.sprite.Group()
select_level_sprites = pygame.sprite.Group()
arrows_sprites = pygame.sprite.Group()  # левая стрелка
arrow_sprites = pygame.sprite.Group()  # правая стрелка
arro_sprites = pygame.sprite.Group()  # стрелка вниз
theatre_front_sprites = pygame.sprite.Group()
theatre_left_sprites = pygame.sprite.Group()
theatre_right_sprites = pygame.sprite.Group()
theatre_back_sprites = pygame.sprite.Group()
seat_sprites = pygame.sprite.Group()
board_sprites = pygame.sprite.Group()


start_button = pygame.sprite.Sprite(start_screen_sprites)
start_button.image = load_image("start_button.png")
start_button.image = pygame.transform.scale(start_button.image, (WIDTH / 4, HEIGHT / 9))
start_button.rect = start_button.image.get_rect()
start_button.rect.x = WIDTH / 2 - WIDTH / 8
start_button.rect.y = HEIGHT / 2 - HEIGHT / 18

scores_button = pygame.sprite.Sprite(start_screen_sprites)
scores_button.image = load_image("scores_button.png")
scores_button.image = pygame.transform.scale(scores_button.image, (WIDTH / 4, HEIGHT / 9))
scores_button.rect = scores_button.image.get_rect()
scores_button.rect.x = WIDTH / 2 - WIDTH / 8
scores_button.rect.y = (HEIGHT / 2 + HEIGHT / 3) - HEIGHT / 18

rules_button = pygame.sprite.Sprite(start_screen_sprites)
rules_button.image = load_image("rules_button.png")
rules_button.image = pygame.transform.scale(rules_button.image, (WIDTH / 4, HEIGHT / 9))
rules_button.rect = rules_button.image.get_rect()
rules_button.rect.x = WIDTH / 2 - WIDTH / 8
rules_button.rect.y = (HEIGHT / 2 + HEIGHT / 6) - HEIGHT / 18

# левая стрелка
left_arrow = pygame.sprite.Sprite(arrows_sprites)
left_arrow.image = load_image("left_arrow.png")
left_arrow.rect = left_arrow.image.get_rect()
left_arrow.rect.x = WIDTH / 35
left_arrow.rect.y = HEIGHT - HEIGHT / 10

# правая стрелка
right_arrow = pygame.sprite.Sprite(arrow_sprites)
right_arrow.image = load_image("right_arrow.png")
right_arrow.rect = right_arrow.image.get_rect()
right_arrow.rect.x = WIDTH / 1.08
right_arrow.rect.y = HEIGHT - HEIGHT / 10

# стрелка вниз
down_arrow = pygame.sprite.Sprite(arro_sprites)
down_arrow.image = load_image("down_arrow.png")
down_arrow.rect = down_arrow.image.get_rect()
down_arrow.rect.x = WIDTH / 2
down_arrow.rect.y = HEIGHT - HEIGHT / 15

# запуск театра
theatre_button = pygame.sprite.Sprite(select_level_sprites)
theatre_button.image = load_image("theatre_button.png")
theatre_button.image = pygame.transform.scale(theatre_button.image, (254, 318))
theatre_button.rect = theatre_button.image.get_rect()
theatre_button.rect.x = 50
theatre_button.rect.y = 250

# запуск мрамора
marble_button = pygame.sprite.Sprite(select_level_sprites)
marble_button.image = load_image("marble_button.png")
marble_button.image = pygame.transform.scale(marble_button.image, (254, 319))
marble_button.rect = marble_button.image.get_rect()
marble_button.rect.x = 400
marble_button.rect.y = 250

# передняя часть
theatre_front_box = pygame.sprite.Sprite(theatre_front_sprites)
theatre_front_box.image = load_image("theatre_front_box.png")
theatre_front_box.image = pygame.transform.scale(theatre_front_box.image, (214, 266))
theatre_front_box.rect = theatre_front_box.image.get_rect()
theatre_front_box.rect.x = 0
theatre_front_box.rect.y = 420

theatre_front_door = pygame.sprite.Sprite(theatre_front_sprites)
theatre_front_door.image = load_image("theatre_front_door.png")
theatre_front_door.image = pygame.transform.scale(theatre_front_door.image, (245, 500))
theatre_front_door.rect = theatre_front_door.image.get_rect()
theatre_front_door.rect.x = 410
theatre_front_door.rect.y = 200

theatre_front_hanger = pygame.sprite.Sprite(theatre_front_sprites)
theatre_front_hanger.image = load_image("theatre_front_hanger.png")
theatre_front_hanger.image = pygame.transform.scale(theatre_front_hanger.image, (124, 575))
theatre_front_hanger.rect = theatre_front_hanger.image.get_rect()
theatre_front_hanger.rect.x = 260
theatre_front_hanger.rect.y = 125

theatre_front_noteboard = pygame.sprite.Sprite(theatre_front_sprites)
theatre_front_noteboard.image = load_image("theatre_front_noteboard.png")
theatre_front_noteboard.image = pygame.transform.scale(theatre_front_noteboard.image, (234, 235))
theatre_front_noteboard.rect = theatre_front_noteboard.image.get_rect()
theatre_front_noteboard.rect.x = 0
theatre_front_noteboard.rect.y = 90

# левая часть
theatre_left_box = pygame.sprite.Sprite(theatre_left_sprites)
theatre_left_box.image = load_image("theatre_left_box.png")
theatre_left_box.image = pygame.transform.scale(theatre_left_box.image, (140, 81))
theatre_left_box.rect = theatre_left_box.image.get_rect()
theatre_left_box.rect.x = 340
theatre_left_box.rect.y = 595

theatre_front_door = pygame.sprite.Sprite(theatre_left_sprites)
theatre_front_door.image = load_image("theatre_left_door.png")
theatre_front_door.image = pygame.transform.scale(theatre_front_door.image, (273, 273))
theatre_front_door.rect = theatre_front_door.image.get_rect()
theatre_front_door.rect.x = 0
theatre_front_door.rect.y = 410

theatre_left_sprout = pygame.sprite.Sprite(theatre_left_sprites)
theatre_left_sprout.image = load_image("theatre_left_sprout.png")
theatre_left_sprout.image = pygame.transform.scale(theatre_left_sprout.image, (35, 54))
theatre_left_sprout.rect = theatre_left_sprout.image.get_rect()
theatre_left_sprout.rect.x = 215
theatre_left_sprout.rect.y = 257

theatre_left_clockface = pygame.sprite.Sprite(theatre_left_sprites)
theatre_left_clockface.image = load_image("theatre_left_clockface.png")
theatre_left_clockface.image = pygame.transform.scale(theatre_left_clockface.image, (114, 107))
theatre_left_clockface.rect = theatre_left_clockface.image.get_rect()
theatre_left_clockface.rect.x = 353
theatre_left_clockface.rect.y = 95

# правая часть
theatre_right_box = pygame.sprite.Sprite(theatre_right_sprites)
theatre_right_box.image = load_image("theatre_right_box.png")
theatre_right_box.image = pygame.transform.scale(theatre_right_box.image, (417, 96))
theatre_right_box.rect = theatre_right_box.image.get_rect()
theatre_right_box.rect.x = 32
theatre_right_box.rect.y = 560

theatre_right_crack = pygame.sprite.Sprite(theatre_right_sprites)
theatre_right_crack.image = load_image("theatre_right_crack.png")
theatre_right_crack.image = pygame.transform.scale(theatre_right_crack.image, (223, 272))
theatre_right_crack.rect = theatre_right_crack.image.get_rect()
theatre_right_crack.rect.x = 480
theatre_right_crack.rect.y = 240

# задняя часть
theatre_back_seat = pygame.sprite.Sprite(theatre_back_sprites)
theatre_back_seat.image = load_image("theatre_back_seats.png")
theatre_back_seat.image = pygame.transform.scale(theatre_back_seat.image, (700, 530))
theatre_back_seat.rect = theatre_back_seat.image.get_rect()
theatre_back_seat.rect.x = 0
theatre_back_seat.rect.y = 0

theatre_back_scene = pygame.sprite.Sprite(theatre_back_sprites)
theatre_back_scene.image = load_image("theatre_back_scene.png")
theatre_back_scene.image = pygame.transform.scale(theatre_back_scene.image, (700, 333))
theatre_back_scene.rect = theatre_back_scene.image.get_rect()
theatre_back_scene.rect.x = 0
theatre_back_scene.rect.y = 367

water = pygame.sprite.Sprite(seat_sprites)
water.image = load_image("water.png")
water.image = pygame.transform.scale(water.image, (172*1.5, 307*1.5))
water.rect = water.image.get_rect()
water.rect.x = 200
water.rect.y = 150

comedy = pygame.sprite.Sprite(board_sprites)
comedy.image = load_image("comedy.png")
comedy.image = pygame.transform.scale(comedy.image, (252, 332))
comedy.rect = comedy.image.get_rect()
comedy.rect.x = 200
comedy.rect.y = 150

def terminate():
    pygame.quit()
    sys.exit()

def start_screen():
    global start
    fon = pygame.transform.scale(load_image('start_screen.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    start_screen_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    return select_level()
                elif rules_button.rect.collidepoint(event.pos):
                    return show_rules()

def select_level():
    fon = pygame.transform.scale(load_image('level_select.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    select_level_sprites.draw(screen)
    arrows_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return start_screen()
                elif theatre_button.rect.collidepoint(event.pos):
                    return theatre_front()
                elif marble_button.rect.collidepoint(event.pos):
                    return marble_front()

def show_rules():
    fon = pygame.transform.scale(load_image('rules_screen.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    arrows_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return start_screen()

def marble_front():
    screen = pygame.display.set_mode(size)
    screen.fill('turquoise')
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

def theatre_front():
    fon = pygame.transform.scale(load_image('theatre_front.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    theatre_front_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return theatre_left()
                elif right_arrow.rect.collidepoint(event.pos):
                    return theatre_right()

def theatre_left():
    fon = pygame.transform.scale(load_image('theatre_left.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    theatre_left_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return theatre_back()
                elif right_arrow.rect.collidepoint(event.pos):
                    return theatre_front()

def theatre_right():
    fon = pygame.transform.scale(load_image('theatre_right.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    theatre_right_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return theatre_front()
                elif right_arrow.rect.collidepoint(event.pos):
                    return theatre_back()

def theatre_back():
    fon = pygame.transform.scale(load_image('theatre_back.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    theatre_back_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return theatre_right()
                elif right_arrow.rect.collidepoint(event.pos):
                    return theatre_left()
                elif theatre_back_seat.rect.collidepoint(event.pos):
                    return seat()
                elif theatre_back_scene.rect.collidepoint(event.pos):
                    return board()

def seat():
    fon = pygame.transform.scale(load_image('seat.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    seat_sprites.draw(screen)
    arro_sprites.draw(screen)  # стрелка вниз
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if down_arrow.rect.collidepoint(event.pos):
                    return theatre_back()

def board():
    fon = pygame.transform.scale(load_image('board.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    board_sprites.draw(screen)
    arro_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if down_arrow.rect.collidepoint(event.pos):
                    return theatre_back()


start_screen()
screen.blit(pygame.transform.scale(load_image('theatre_front.png'), (WIDTH, HEIGHT)), (0, 0))
theatre_front_sprites.draw(screen)
arrows_sprites.draw(screen)
arrow_sprites.draw(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if left_arrow.rect.collidepoint(event.pos):
                theatre_left()
            if right_arrow.rect.collidepoint(event.pos):
                theatre_right()
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
