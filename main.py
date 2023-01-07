import pygame
import sys
import os


pygame.init()
FPS = 60
size = WIDTH, HEIGHT = 700, 900
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Мистер Банеееейн, Mr. Bannaaaame')
clock = pygame.time.Clock()
inventory = []
first_code = False
second_code = False
third_code = False
fourth_code = False
clock_arrows_set = False


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
key_sprites = pygame.sprite.Group()
theatre_right_box_inside = pygame.sprite.Group()
theatre_right_box_clock_arrows = pygame.sprite.Group()
theatre_right_box_code_first = pygame.sprite.Group()
inventory_sprites_key = pygame.sprite.Group()
inventory_sprites_clock_arrows = pygame.sprite.Group()
inventory_sprites_code_first = pygame.sprite.Group()
theatre_left_clock_arrows = pygame.sprite.Group()


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
left_arrow.rect.x = 20
left_arrow.rect.y = 630

# правая стрелка
right_arrow = pygame.sprite.Sprite(arrow_sprites)
right_arrow.image = load_image("right_arrow.png")
right_arrow.rect = right_arrow.image.get_rect()
right_arrow.rect.x = 648
right_arrow.rect.y = 630

# стрелка вниз
down_arrow = pygame.sprite.Sprite(arro_sprites)
down_arrow.image = load_image("down_arrow.png")
down_arrow.rect = down_arrow.image.get_rect()
down_arrow.rect.x = 350
down_arrow.rect.y = 653

# запуск театра
theatre_button = pygame.sprite.Sprite(select_level_sprites)
theatre_button.image = load_image("theatre_button.png")
theatre_button.image = pygame.transform.scale(theatre_button.image, (254, 318))
theatre_button.rect = theatre_button.image.get_rect()
theatre_button.rect.x = 50
theatre_button.rect.y = 300

# запуск мрамора
marble_button = pygame.sprite.Sprite(select_level_sprites)
marble_button.image = load_image("marble_button.png")
marble_button.image = pygame.transform.scale(marble_button.image, (254, 319))
marble_button.rect = marble_button.image.get_rect()
marble_button.rect.x = 400
marble_button.rect.y = 300

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

key = pygame.sprite.Sprite(key_sprites)
key.image = load_image("key.png")
key.image = pygame.transform.scale(key.image, (40, 90))
key.rect = key.image.get_rect()
key.rect.x = 330
key.rect.y = 350

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

clock_arrows_left = pygame.sprite.Sprite(theatre_left_clock_arrows)
clock_arrows_left.image = load_image("clock_arrows.png")
clock_arrows_left.image = pygame.transform.scale(clock_arrows_left.image, (65, 53))
clock_arrows_left.rect = clock_arrows_left.image.get_rect()
clock_arrows_left.rect.x = 384
clock_arrows_left.rect.y = 134

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

clock_arrows = pygame.sprite.Sprite(theatre_right_box_clock_arrows)
clock_arrows.image = load_image("clock_arrows.png")
clock_arrows.image = pygame.transform.scale(clock_arrows.image, (114, 107))
clock_arrows.rect = clock_arrows.image.get_rect()
clock_arrows.rect.x = 240
clock_arrows.rect.y = 240

code_first = pygame.sprite.Sprite(theatre_right_box_code_first)
code_first.image = load_image("code_first.png")
code_first.rect = code_first.image.get_rect()
code_first.rect.x = 480
code_first.rect.y = 240

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

# инвентарь
inventory_key = pygame.sprite.Sprite(inventory_sprites_key)
inventory_key.image = load_image("key.png")
inventory_key.image = pygame.transform.scale(inventory_key.image, (40, 90))
inventory_key.rect = inventory_key.image.get_rect()
inventory_key.rect.x = 50
inventory_key.rect.y = 705

inventory_clock_arrows = pygame.sprite.Sprite(inventory_sprites_clock_arrows)
inventory_clock_arrows.image = load_image("clock_arrows.png")
inventory_clock_arrows.image = pygame.transform.scale(inventory_clock_arrows.image, (57, 53))
inventory_clock_arrows.rect = inventory_clock_arrows.image.get_rect()
inventory_clock_arrows.rect.x = 153
inventory_clock_arrows.rect.y = 725

inventory_code_first = pygame.sprite.Sprite(inventory_sprites_code_first)
inventory_code_first.image = load_image("code_first.png")
inventory_code_first.image = pygame.transform.scale(inventory_code_first.image, (50, 50))
inventory_code_first.rect = inventory_code_first.image.get_rect()
inventory_code_first.rect.x = 20
inventory_code_first.rect.y = 200


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
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
                    screen.fill((255, 255, 255))
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
    global first_code
    screen.fill((255, 255, 255))
    fon = pygame.transform.scale(load_image('theatre_front.png'), (700, 700))
    screen.blit(fon, (0, 0))
    theatre_front_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    if first_code is True:
        inventory_sprites_code_first.draw(screen)
    for i in inventory:
        globals()["inventory_sprites_" + i].draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return theatre_left()
                elif right_arrow.rect.collidepoint(event.pos):
                    return theatre_right()
                elif theatre_front_hanger.rect.collidepoint(event.pos) and 'key' not in inventory:
                    return show_key()
        pygame.display.flip()


def show_key():
    key_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if key.rect.collidepoint(event.pos):
                    inventory.append('key')
                    inventory_sprites_key.draw(screen)
                    return theatre_front()


def theatre_left():
    global clock_arrows_set
    fon = pygame.transform.scale(load_image('theatre_left.png'), (700, 700))
    screen.blit(fon, (0, 0))
    theatre_left_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    if clock_arrows_set:
        theatre_left_clock_arrows.draw(screen)
    for i in inventory:
        globals()["inventory_sprites_" + i].draw(screen)
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
                elif theatre_left_clockface.rect.collidepoint(event.pos) and 'clock_arrows' in inventory:
                    theatre_left_clock_arrows.draw(screen)
                    clock_arrows_set = True
                    inventory.remove('clock_arrows')


def theatre_right():
    fon = pygame.transform.scale(load_image('theatre_right.png'), (700, 700))
    screen.blit(fon, (0, 0))
    theatre_right_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    for i in inventory:
        globals()["inventory_sprites_" + i].draw(screen)
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
                elif theatre_right_box.rect.collidepoint(event.pos):
                    return show_theatre_right_box()


def show_theatre_right_box():
    global first_code
    global clock_arrows_set
    fon = pygame.transform.scale(load_image('theatre_right_box_inside.png'), (700, 700))
    screen.blit(fon, (0, 0))
    if first_code is False:
        if 'clock_arrows' not in inventory and clock_arrows_set is False:
            theatre_right_box_clock_arrows.draw(screen)
            theatre_right_box_code_first.draw(screen)
        else:
            theatre_right_box_code_first.draw(screen)
    else:
        if 'clock_arrows' not in inventory and clock_arrows_set is False:
            theatre_right_box_clock_arrows.draw(screen)
        else:
            pass
    arro_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if clock_arrows.rect.collidepoint(event.pos):
                    inventory.append('clock_arrows')
                    inventory_sprites_clock_arrows.draw(screen)
                    if first_code:
                        screen.blit(fon, (0, 0))
                        arro_sprites.draw(screen)
                    else:
                        screen.blit(fon, (0, 0))
                        theatre_right_box_code_first.draw(screen)
                        arro_sprites.draw(screen)
                elif code_first.rect.collidepoint(event.pos):
                    first_code = True
                    if 'clock_arrows' in inventory or clock_arrows_set:
                        screen.blit(fon, (0, 0))
                        arro_sprites.draw(screen)
                    else:
                        screen.blit(fon, (0, 0))
                        theatre_right_box_clock_arrows.draw(screen)
                        arro_sprites.draw(screen)
                elif down_arrow.rect.collidepoint(event.pos):
                    return theatre_right()


def theatre_back():
    fon = pygame.transform.scale(load_image('theatre_back.png'), (700, 700))
    screen.blit(fon, (0, 0))
    theatre_back_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    for i in inventory:
        globals()["inventory_sprites_" + i].draw(screen)
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
    fon = pygame.transform.scale(load_image('seat.png'), (700, 700))
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
    fon = pygame.transform.scale(load_image('board.png'), (700, 700))
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
screen.blit(pygame.transform.scale(load_image('theatre_front.png'), (700, 700)), (0, 0))
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
