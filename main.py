import pygame
import sys
import os


pygame.init()
FPS = 60
size = WIDTH, HEIGHT = 700, 900  # чисто для себя размер поставила
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
# спрайты театра
theatre_front_sprites = pygame.sprite.Group()  # перед
theatre_left_sprites = pygame.sprite.Group()  # лево
theatre_right_sprites = pygame.sprite.Group()  # право
theatre_back_sprites = pygame.sprite.Group()  # сзади
seat_sprites = pygame.sprite.Group()  # сиденье
board_sprites = pygame.sprite.Group()  # доска
key_sprites = pygame.sprite.Group()
theatre_right_box_inside = pygame.sprite.Group()  # право внутри ящика
theatre_right_box_clock_arrows = pygame.sprite.Group()  # право стрелки часов
theatre_right_box_code_first = pygame.sprite.Group()  # код первая цифра
inventory_sprites_key = pygame.sprite.Group()
inventory_sprites_clock_arrows = pygame.sprite.Group()
inventory_sprites_code_first = pygame.sprite.Group()
theatre_left_clock_arrows = pygame.sprite.Group()  # право стрелки часов
show_theatre_front_box_sprites = pygame.sprite.Group()  # перед внутри ящика
clock_box_inside_sprites = pygame.sprite.Group()  # лево внутри ящика часов
box_inside_sprites = pygame.sprite.Group()  # лево внутри ящика
inventory_sprites_coin = pygame.sprite.Group()
inventory_sprites_code_second = pygame.sprite.Group()
inventory_sprites_code_third = pygame.sprite.Group()
inventory_sprites_code_fourth = pygame.sprite.Group()

# спрайты мрамора
marble_front_sprites = pygame.sprite.Group()
marble_right_sprites = pygame.sprite.Group()
marble_left_sprites = pygame.sprite.Group()
marble_back_sprites = pygame.sprite.Group()
bottombox_sprites = pygame.sprite.Group()
topbox_sprites = pygame.sprite.Group()

# начальный экран
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

# передняя часть театра
exit_button = pygame.sprite.Sprite(theatre_front_sprites)
exit_button.image = load_image("exit_button.png")
exit_button.image = pygame.transform.scale(exit_button.image, (111, 39))
exit_button.rect = exit_button.image.get_rect()
exit_button.rect.x = 10
exit_button.rect.y = 20

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

tragedy = pygame.sprite.Sprite(show_theatre_front_box_sprites)  # маска
tragedy.image = load_image("tragedy.png")
tragedy.image = pygame.transform.scale(tragedy.image, (252, 332))
tragedy.rect = tragedy.image.get_rect()
tragedy.rect.x = 200
tragedy.rect.y = 150

# передняя часть мрамора
exit_button = pygame.sprite.Sprite(marble_front_sprites)
exit_button.image = load_image("exit_button.png")
exit_button.image = pygame.transform.scale(exit_button.image, (111, 39))
exit_button.rect = exit_button.image.get_rect()
exit_button.rect.x = 10
exit_button.rect.y = 20

marble_front_painting = pygame.sprite.Sprite(marble_front_sprites)
marble_front_painting.image = load_image("marble_front_painting.png")
marble_front_painting.image = pygame.transform.scale(marble_front_painting.image, (263, 245))
marble_front_painting.rect = marble_front_painting.image.get_rect()
marble_front_painting.rect.x = 70
marble_front_painting.rect.y = 455

marble_front_door = pygame.sprite.Sprite(marble_front_sprites)
marble_front_door.image = load_image("marble_front_door.png")
marble_front_door.image = pygame.transform.scale(marble_front_door.image, (289, 616))
marble_front_door.rect = marble_front_door.image.get_rect()
marble_front_door.rect.x = 350
marble_front_door.rect.y = 85

# левая часть театра
theatre_left_box = pygame.sprite.Sprite(theatre_left_sprites)
theatre_left_box.image = load_image("theatre_left_box.png")
theatre_left_box.image = pygame.transform.scale(theatre_left_box.image, (140, 81))
theatre_left_box.rect = theatre_left_box.image.get_rect()
theatre_left_box.rect.x = 340
theatre_left_box.rect.y = 595

theatre_left_door = pygame.sprite.Sprite(theatre_left_sprites)
theatre_left_door.image = load_image("theatre_left_door.png")
theatre_left_door.image = pygame.transform.scale(theatre_left_door.image, (273, 273))
theatre_left_door.rect = theatre_left_door.image.get_rect()
theatre_left_door.rect.x = 0
theatre_left_door.rect.y = 410

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
# внутри часов
scrap = pygame.sprite.Sprite(clock_box_inside_sprites)
scrap.image = load_image("scrap.png")
scrap.image = pygame.transform.scale(scrap.image, (284, 347))
scrap.rect = scrap.image.get_rect()
scrap.rect.x = 100
scrap.rect.y = 100

coin = pygame.sprite.Sprite(clock_box_inside_sprites)
coin.image = load_image("coin.png")
coin.image = pygame.transform.scale(coin.image, (67, 70))
coin.rect = coin.image.get_rect()
coin.rect.x = 350
coin.rect.y = 200

code_two = pygame.sprite.Sprite(clock_box_inside_sprites)
code_two.image = load_image("code_two.png")
code_two.image = pygame.transform.scale(code_two.image, (92, 96))
code_two.rect = code_two.image.get_rect()
code_two.rect.x = 400
code_two.rect.y = 400
# внутри ящика
code_four = pygame.sprite.Sprite(box_inside_sprites)
code_four.image = load_image("code_four.png")
code_four.image = pygame.transform.scale(code_four.image, (101, 56))
code_four.rect = code_four.image.get_rect()
code_four.rect.x = 320
code_four.rect.y = 350

key_theatre_door = pygame.sprite.Sprite(box_inside_sprites)
key_theatre_door.image = load_image("key_theatre_door.png")
key_theatre_door.image = pygame.transform.scale(key_theatre_door.image, (40, 90))
key_theatre_door.rect = key_theatre_door.image.get_rect()
key_theatre_door.rect.x = 50
key_theatre_door.rect.y = 570

# левая часть мрамора
marble_left_armchair = pygame.sprite.Sprite(marble_left_sprites)
marble_left_armchair.image = load_image("marble_left_armchair.png")
marble_left_armchair.image = pygame.transform.scale(marble_left_armchair.image, (259, 308))
marble_left_armchair.rect = marble_left_armchair.image.get_rect()
marble_left_armchair.rect.x = 50
marble_left_armchair.rect.y = 392

# правая часть театра
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

# правая часть мрамора
marble_right_pot = pygame.sprite.Sprite(marble_right_sprites)
marble_right_pot.image = load_image("marble_right_pot.png")
marble_right_pot.image = pygame.transform.scale(marble_right_pot.image, (131, 130))
marble_right_pot.rect = marble_right_pot.image.get_rect()
marble_right_pot.rect.x = 540
marble_right_pot.rect.y = 570

marble_right_pillow = pygame.sprite.Sprite(marble_right_sprites)
marble_right_pillow.image = load_image("marble_right_pillow.png")
marble_right_pillow.image = pygame.transform.scale(marble_right_pillow.image, (108, 65))
marble_right_pillow.rect = marble_right_pillow.image.get_rect()
marble_right_pillow.rect.x = 400
marble_right_pillow.rect.y = 405

marble_right_lattice = pygame.sprite.Sprite(marble_right_sprites)
marble_right_lattice.image = load_image("marble_right_lattice.png")  # при взаимодействие поворачивается на 90 вниз
marble_right_lattice.image = pygame.transform.scale(marble_right_lattice.image, (222, 78))
marble_right_lattice.rect = marble_right_lattice.image.get_rect()
marble_right_lattice.rect.x = 6
marble_right_lattice.rect.y = 26

# задняя часть театра
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

comedy = pygame.sprite.Sprite(board_sprites)  # маска
comedy.image = load_image("comedy.png")
comedy.image = pygame.transform.scale(comedy.image, (252, 332))
comedy.rect = comedy.image.get_rect()
comedy.rect.x = 200
comedy.rect.y = 150

# задняя часть мрамора
marble_back_topbox = pygame.sprite.Sprite(marble_back_sprites)
marble_back_topbox.image = load_image("marble_back_topbox.png")
marble_back_topbox.image = pygame.transform.scale(marble_back_topbox.image, (415, 128))
marble_back_topbox.rect = marble_back_topbox.image.get_rect()
marble_back_topbox.rect.x = 252
marble_back_topbox.rect.y = 430

marble_back_bottombox = pygame.sprite.Sprite(marble_back_sprites)
marble_back_bottombox.image = load_image("marble_back_bottombox.png")
marble_back_bottombox.image = pygame.transform.scale(marble_back_bottombox.image, (415, 96))
marble_back_bottombox.rect = marble_back_bottombox.image.get_rect()
marble_back_bottombox.rect.x = 252
marble_back_bottombox.rect.y = 560

screwdriver = pygame.sprite.Sprite(topbox_sprites)
screwdriver.image = load_image("screwdriver.png")
screwdriver.image = pygame.transform.scale(screwdriver.image, (321, 210))
screwdriver.rect = screwdriver.image.get_rect()
screwdriver.rect.x = 200
screwdriver.rect.y = 250

tassel = pygame.sprite.Sprite(bottombox_sprites)
tassel.image = load_image("tassel.png")
tassel.image = pygame.transform.scale(tassel.image, (219, 219))
tassel.rect = tassel.image.get_rect()
tassel.rect.x = 200
tassel.rect.y = 250

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

inventory_code_second = pygame.sprite.Sprite(inventory_sprites_code_second)
inventory_code_second.image = load_image("code_two.png")
inventory_code_second.image = pygame.transform.scale(inventory_code_second.image, (50, 50))
inventory_code_second.rect = inventory_code_second.image.get_rect()
inventory_code_second.rect.x = 90
inventory_code_second.rect.y = 200

#inventory_code_third = pygame.sprite.Sprite(inventory_sprites_code_third)
#inventory_code_third.image = load_image("code_third.png")
#inventory_code_third.image = pygame.transform.scale(inventory_code_third.image, (50, 50))
#inventory_code_third.rect = inventory_code_third.image.get_rect()
#inventory_code_third.rect.x = 160
#inventory_code_third.rect.y = 200

inventory_code_fourth = pygame.sprite.Sprite(inventory_sprites_code_fourth)
inventory_code_fourth.image = load_image("code_four.png")
inventory_code_fourth.image = pygame.transform.scale(inventory_code_fourth.image, (50, 50))
inventory_code_fourth.rect = inventory_code_fourth.image.get_rect()
inventory_code_fourth.rect.x = 230
inventory_code_fourth.rect.y = 200


inventory_coin = pygame.sprite.Sprite(inventory_sprites_coin)
inventory_coin.image = load_image("coin.png")
inventory_coin.image = pygame.transform.scale(inventory_coin.image, (67, 70))
inventory_coin.rect = inventory_coin.image.get_rect()
inventory_coin.rect.x = 317
inventory_coin.rect.y = 715


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
                    theatre_front()
                elif marble_button.rect.collidepoint(event.pos):
                    screen.fill((255, 255, 255))
                    marble_front()


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


def render_inventory():
    for i in inventory:
        globals()["inventory_sprites_" + i].draw(screen)


# Мрамор
def marble_front():
    fon = pygame.transform.scale(load_image('marble_front.png'), (700, 700))
    screen.blit(fon, (0, 0))
    marble_front_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return marble_left()
                elif right_arrow.rect.collidepoint(event.pos):
                    return marble_right()
                elif exit_button.rect.collidepoint(event.pos):
                    return select_level()


def marble_right():
    fon = pygame.transform.scale(load_image('marble_right.png'), (700, 700))
    screen.blit(fon, (0, 0))
    marble_right_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return marble_front()
                elif right_arrow.rect.collidepoint(event.pos):
                    return marble_back()


def marble_left():
    fon = pygame.transform.scale(load_image('marble_left.png'), (700, 700))
    screen.blit(fon, (0, 0))
    marble_left_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return marble_back()
                elif right_arrow.rect.collidepoint(event.pos):
                    return marble_front()


def marble_back():
    fon = pygame.transform.scale(load_image('marble_back.png'), (700, 700))
    screen.blit(fon, (0, 0))
    marble_back_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return marble_right()
                elif right_arrow.rect.collidepoint(event.pos):
                    return marble_left()
                elif marble_back_topbox.rect.collidepoint(event.pos):
                    return top_box()
                elif marble_back_bottombox.rect.collidepoint(event.pos):
                    return bottom_box()


def top_box():
    fon = pygame.transform.scale(load_image('marble_top_box.png'), (700, 700))
    screen.blit(fon, (0, 0))
    topbox_sprites.draw(screen)
    arro_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if down_arrow.rect.collidepoint(event.pos):
                    return marble_back()


def bottom_box():
    fon = pygame.transform.scale(load_image('marble_bottom_box.png'), (700, 700))
    screen.blit(fon, (0, 0))
    bottombox_sprites.draw(screen)
    arro_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if down_arrow.rect.collidepoint(event.pos):
                    return marble_back()


# Театр
def theatre_front():
    global first_code
    global second_code
    global third_code
    global fourth_code
    screen.fill((255, 255, 255))
    fon = pygame.transform.scale(load_image('theatre_front.png'), (700, 700))
    screen.blit(fon, (0, 0))
    theatre_front_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    if first_code:
        inventory_sprites_code_first.draw(screen)
    if second_code:
        inventory_sprites_code_second.draw(screen)
    if third_code:
        inventory_sprites_code_third.draw(screen)
    if fourth_code:
        inventory_sprites_code_fourth.draw(screen)
    while True:
        render_inventory()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return theatre_left()
                elif right_arrow.rect.collidepoint(event.pos):
                    return theatre_right()
                elif exit_button.rect.collidepoint(event.pos):
                    return select_level()
                elif theatre_front_box.rect.collidepoint(event.pos):
                    return show_theatre_front_box()
                elif theatre_front_hanger.rect.collidepoint(event.pos) and 'key' not in inventory:
                    return show_key()
        pygame.display.flip()


def show_theatre_front_box():
    fon = pygame.transform.scale(load_image('theatre_front_box_inside.png'), (700, 700))
    screen.blit(fon, (0, 0))
    show_theatre_front_box_sprites.draw(screen)
    arro_sprites.draw(screen)
    while True:
        render_inventory()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if down_arrow.rect.collidepoint(event.pos):
                    return theatre_front()


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
                elif theatre_left_box.rect.collidepoint(event.pos) and clock_arrows_set:
                    return clock_box_inside()
                elif theatre_left_door.rect.collidepoint(event.pos):
                    return box_inside()
                elif theatre_left_clockface.rect.collidepoint(event.pos) and 'clock_arrows' in inventory:
                    clock_arrows_set = True
                    inventory.remove('clock_arrows')
                    screen.fill((255, 255, 255))
                    screen.blit(fon, (0, 0))
                    theatre_left_sprites.draw(screen)
                    arrows_sprites.draw(screen)  # левая стрелка
                    arrow_sprites.draw(screen)  # правая стрелка
                    theatre_left_clock_arrows.draw(screen)
                    render_inventory()


def clock_box_inside():
    global second_code
    fon = pygame.transform.scale(load_image('clock_box_inside.png'), (700, 700))
    screen.blit(fon, (0, 0))
    clock_box_inside_sprites.draw(screen)
    arro_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if down_arrow.rect.collidepoint(event.pos):
                    return theatre_left()
                elif coin.rect.collidepoint(event.pos):
                    coin.kill()
                    screen.blit(fon, (0, 0))
                    clock_box_inside_sprites.draw(screen)
                    arro_sprites.draw(screen)
                    inventory.append('coin')
                elif code_two.rect.collidepoint(event.pos):
                    code_two.kill()
                    screen.blit(fon, (0, 0))
                    clock_box_inside_sprites.draw(screen)
                    arro_sprites.draw(screen)
                    second_code = True
        render_inventory()


def box_inside():
    fon = pygame.transform.scale(load_image('box_inside.png'), (700, 700))
    screen.blit(fon, (0, 0))
    box_inside_sprites.draw(screen)
    arro_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if down_arrow.rect.collidepoint(event.pos):
                    return theatre_left()
        render_inventory()


def theatre_right():
    fon = pygame.transform.scale(load_image('theatre_right.png'), (700, 700))
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
                elif theatre_right_box.rect.collidepoint(event.pos) and 'key' in inventory:
                    return show_theatre_right_box()
        render_inventory()


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
                elif down_arrow.rect.collidepoint(event.pos) and first_code and \
                        ('clock_arrows' in inventory or clock_arrows_set):
                    inventory.remove('key')
                    return theatre_right()
                elif down_arrow.rect.collidepoint(event.pos):
                    return theatre_right()
        render_inventory()


def theatre_back():
    fon = pygame.transform.scale(load_image('theatre_back.png'), (700, 700))
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
        render_inventory()


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
        render_inventory()


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
        render_inventory()


start_screen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
