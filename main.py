import pygame
import sys
import os
import time


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
fertilizers_used = False
box_key_used = False


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
inventory_sprites_code_four = pygame.sprite.Group()
inventory_sprites_scrap = pygame.sprite.Group()
inventory_sprites_comedy = pygame.sprite.Group()
inventory_sprites_water = pygame.sprite.Group()
fertilizers_sprite = pygame.sprite.Group()
inventory_sprites_fertilizers = pygame.sprite.Group()
door_key_sprite = pygame.sprite.Group()
inventory_sprites_door_key = pygame.sprite.Group()
inventory_sprites_key_theatre_door = pygame.sprite.Group()
code_three_sprites = pygame.sprite.Group()
inventory_sprites_tragedy = pygame.sprite.Group()
# финал
final_sprites = pygame.sprite.Group()

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
theatre_left_sprout.rect.x = 205
theatre_left_sprout.rect.y = 257

code_three = pygame.sprite.Sprite(code_three_sprites)
code_three.image = load_image("code_two.png")
code_three.image = pygame.transform.scale(code_three.image, (40, 40))
code_three.rect = code_three.image.get_rect()
code_three.rect.x = 250
code_three.rect.y = 320

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

door_key = pygame.sprite.Sprite(door_key_sprite)
door_key.image = load_image("key.png")
door_key.image = pygame.transform.scale(door_key.image, (20, 45))
door_key.rect = door_key.image.get_rect()
door_key.rect.x = 220
door_key.rect.y = 320
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

fertilizers = pygame.sprite.Sprite(fertilizers_sprite)
fertilizers.image = load_image("fertilizers.png")
fertilizers.image = pygame.transform.scale(fertilizers.image, (52, 64))
fertilizers.rect = fertilizers.image.get_rect()
fertilizers.rect.x = 550
fertilizers.rect.y = 340

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
theatre_back_seat.image = pygame.transform.scale(theatre_back_seat.image, (128, 80))
theatre_back_seat.rect = theatre_back_seat.image.get_rect()
theatre_back_seat.rect.x = 200
theatre_back_seat.rect.y = 290

theatre_back_scene = pygame.sprite.Sprite(theatre_back_sprites)
theatre_back_scene.image = load_image("theatre_back_scene.png")
theatre_back_scene.image = pygame.transform.scale(theatre_back_scene.image, (205, 74))
theatre_back_scene.rect = theatre_back_scene.image.get_rect()
theatre_back_scene.rect.x = 250
theatre_back_scene.rect.y = 500

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
inventory_code_first.image = pygame.transform.scale(inventory_code_first.image, (35, 35))
inventory_code_first.rect = inventory_code_first.image.get_rect()
inventory_code_first.rect.x = 20
inventory_code_first.rect.y = 200

inventory_code_second = pygame.sprite.Sprite(inventory_sprites_code_second)
inventory_code_second.image = load_image("code_two.png")
inventory_code_second.image = pygame.transform.scale(inventory_code_second.image, (35, 35))
inventory_code_second.rect = inventory_code_second.image.get_rect()
inventory_code_second.rect.x = 75
inventory_code_second.rect.y = 200

inventory_code_third = pygame.sprite.Sprite(inventory_sprites_code_third)
inventory_code_third.image = load_image("code_two.png")
inventory_code_third.image = pygame.transform.scale(inventory_code_third.image, (35, 35))
inventory_code_third.rect = inventory_code_third.image.get_rect()
inventory_code_third.rect.x = 130
inventory_code_third.rect.y = 200

inventory_code_fourth = pygame.sprite.Sprite(inventory_sprites_code_four)
inventory_code_fourth.image = load_image("code_four.png")
inventory_code_fourth.image = pygame.transform.scale(inventory_code_fourth.image, (35, 35))
inventory_code_fourth.rect = inventory_code_fourth.image.get_rect()
inventory_code_fourth.rect.x = 185
inventory_code_fourth.rect.y = 200


inventory_coin = pygame.sprite.Sprite(inventory_sprites_coin)
inventory_coin.image = load_image("coin.png")
inventory_coin.image = pygame.transform.scale(inventory_coin.image, (67, 70))
inventory_coin.rect = inventory_coin.image.get_rect()
inventory_coin.rect.x = 317
inventory_coin.rect.y = 715

inventory_scrap = pygame.sprite.Sprite(inventory_sprites_scrap)
inventory_scrap.image = load_image("scrap.png")
inventory_scrap.image = pygame.transform.scale(inventory_scrap.image, (95, 116))
inventory_scrap.rect = inventory_scrap.image.get_rect()
inventory_scrap.rect.x = 443
inventory_scrap.rect.y = 700

inventory_comedy = pygame.sprite.Sprite(inventory_sprites_comedy)
inventory_comedy.image = load_image("comedy.png")
inventory_comedy.image = pygame.transform.scale(inventory_comedy.image, (63, 83))
inventory_comedy.rect = inventory_comedy.image.get_rect()
inventory_comedy.rect.x = 598
inventory_comedy.rect.y = 709

inventory_tragedy = pygame.sprite.Sprite(inventory_sprites_tragedy)
inventory_tragedy.image = load_image("tragedy.png")
inventory_tragedy.image = pygame.transform.scale(inventory_tragedy.image, (63, 83))
inventory_tragedy.rect = inventory_tragedy.image.get_rect()
inventory_tragedy.rect.x = 458
inventory_tragedy.rect.y = 709

inventory_water = pygame.sprite.Sprite(inventory_sprites_water)
inventory_water.image = load_image("water.png")
inventory_water.image = pygame.transform.scale(inventory_water.image, (65, 98))
inventory_water.rect = inventory_water.image.get_rect()
inventory_water.rect.x = 38
inventory_water.rect.y = 803

inventory_fertilizers = pygame.sprite.Sprite(inventory_sprites_fertilizers)
inventory_fertilizers.image = load_image("fertilizers.png")
inventory_fertilizers.image = pygame.transform.scale(inventory_fertilizers.image, (52, 64))
inventory_fertilizers.rect = inventory_fertilizers.image.get_rect()
inventory_fertilizers.rect.x = 185
inventory_fertilizers.rect.y = 818

inventory_door_key = pygame.sprite.Sprite(inventory_sprites_door_key)
inventory_door_key.image = load_image("key.png")
inventory_door_key.image = pygame.transform.scale(inventory_door_key.image, (40, 90))
inventory_door_key.rect = inventory_door_key.image.get_rect()
inventory_door_key.rect.x = 330
inventory_door_key.rect.y = 805

inventory_key_theatre_door = pygame.sprite.Sprite(inventory_sprites_key_theatre_door)
inventory_key_theatre_door.image = load_image("key_theatre_door.png")
inventory_key_theatre_door.image = pygame.transform.scale(inventory_key_theatre_door.image, (40, 90))
inventory_key_theatre_door.rect = inventory_key_theatre_door.image.get_rect()
inventory_key_theatre_door.rect.x = 610
inventory_key_theatre_door.rect.y = 805
# конец
return_button = pygame.sprite.Sprite(final_sprites)  # нужно добавить на финальное окно( оно возвражает на экран выбора)
return_button.image = load_image("return_button.png")
return_button.image = pygame.transform.scale(return_button.image, (111, 39))
return_button.rect = return_button.image.get_rect()
return_button.rect.x = 580
return_button.rect.y = 850
# мрамор дополнение
biscuit = pygame.sprite.Sprite()  # печенье (нет спрайта)
biscuit.image = load_image("biscuit.png")
biscuit.image = pygame.transform.scale(biscuit.image, (54, 54))
biscuit.rect = biscuit.image.get_rect()
biscuit.rect.x = 0
biscuit.rect.y = 0
hammer = pygame.sprite.Sprite()  # молоток (нет спрайта)
hammer.image = load_image("hammer.png")
hammer.image = pygame.transform.scale(hammer.image, (270, 295))
hammer.rect = hammer.image.get_rect()
hammer.rect.x = 0
hammer.rect.y = 0
knife = pygame.sprite.Sprite()  # нож (нет спрайта)
knife.image = load_image("knife.png")
knife.image = pygame.transform.scale(knife.image, (248, 370))
knife.rect = knife.image.get_rect()
knife.rect.x = 0
knife.rect.y = 0
palette = pygame.sprite.Sprite()  # палитра (нет спрайта)
palette.image = load_image("palette.png")
palette.image = pygame.transform.scale(palette.image, (228, 231))
palette.rect = palette.image.get_rect()
palette.rect.x = 200
palette.rect.y = 200
broken_armchair = pygame.sprite.Sprite()  # сломаное кресло (нет спрайта)
broken_armchair.image = load_image("broken_armchair.png")
broken_armchair.image = pygame.transform.scale(broken_armchair.image, (259, 308))
broken_armchair.rect = broken_armchair.image.get_rect()
broken_armchair.rect.x = 50
broken_armchair.rect.y = 392
broken_pot = pygame.sprite.Sprite()  # сломаный горшок (нет спрайта)
broken_pot.image = load_image("broken_pot.png")
broken_pot.image = pygame.transform.scale(broken_pot.image, (209, 129))
broken_pot.rect = broken_pot.image.get_rect()
broken_pot.rect.x = 0
broken_pot.rect.y = 0
tree = pygame.sprite.Sprite()  # дерева (нет спрайта)
tree.image = load_image("tree.png")
tree.image = pygame.transform.scale(tree.image, (159, 233))
tree.rect = tree.image.get_rect()
tree.rect.x = 0
tree.rect.y = 0


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


def final_screen():
    fon = pygame.transform.scale(load_image('the_end.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))


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
        inventory_sprites_code_four.draw(screen)
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
                elif theatre_front_door.rect.collidepoint(event.pos) and 'tragedy' in inventory\
                        and 'comedy' in inventory:
                    inventory.remove('comedy')
                    inventory.remove('tragedy')
                    return final_screen()
                elif theatre_front_box.rect.collidepoint(event.pos) and 'key_theatre_door' in inventory \
                        and first_code and second_code and third_code and fourth_code:
                    return show_theatre_front_box()
                elif theatre_front_hanger.rect.collidepoint(event.pos) and box_key_used is False \
                        and 'key' not in inventory:
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
                    if len(show_theatre_front_box_sprites.sprites()) == 0:
                        inventory.remove('key_theatre_door')
                        screen.fill((255, 255, 255), (0, 700, 700, 200))
                        render_inventory()
                    return theatre_front()
                elif tragedy.rect.collidepoint(event.pos):
                    tragedy.kill()
                    screen.blit(fon, (0, 0))
                    show_theatre_front_box_sprites.draw(screen)
                    arro_sprites.draw(screen)
                    inventory.append('tragedy')
                    screen.fill((255, 255, 255), (0, 700, 700, 200))
                    render_inventory()


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
    global fertilizers_used
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
                elif theatre_left_door.rect.collidepoint(event.pos) and 'door_key' in inventory:
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
                elif theatre_left_sprout.rect.collidepoint(event.pos) and 'fertilizers' in inventory:
                    inventory.remove('fertilizers')
                    screen.fill((255, 255, 255), (0, 700, 700, 200))
                    render_inventory()
                    fertilizers_used = True
                elif theatre_left_sprout.rect.collidepoint(event.pos) and fertilizers_used and 'water' in inventory:
                    inventory.remove('water')
                    screen.fill((255, 255, 255), (0, 700, 700, 200))
                    render_inventory()
                    spout_grow()
        render_inventory()


def spout_grow():
    global third_code
    actions = 0
    while True:
        door_key_sprite.draw(screen)
        code_three_sprites.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if door_key.rect.collidepoint(event.pos):
                    door_key.kill()
                    screen.fill((255, 255, 255))
                    screen.blit(pygame.transform.scale(load_image('theatre_left.png'), (700, 700)), (0, 0))
                    theatre_left_sprites.draw(screen)
                    theatre_left_clock_arrows.draw(screen)
                    arrows_sprites.draw(screen)
                    arrow_sprites.draw(screen)
                    inventory.append('door_key')
                    inventory_sprites_door_key.draw(screen)
                    render_inventory()
                    actions += 1
                elif code_three.rect.collidepoint(event.pos):
                    code_three.kill()
                    screen.fill((255, 255, 255))
                    screen.blit(pygame.transform.scale(load_image('theatre_left.png'), (700, 700)), (0, 0))
                    theatre_left_sprites.draw(screen)
                    theatre_left_clock_arrows.draw(screen)
                    arrows_sprites.draw(screen)
                    arrow_sprites.draw(screen)
                    third_code = True
                    actions += 1
                if actions == 2:
                    return theatre_left()


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
                elif scrap.rect.collidepoint(event.pos):
                    scrap.kill()
                    screen.blit(fon, (0, 0))
                    clock_box_inside_sprites.draw(screen)
                    arro_sprites.draw(screen)
                    inventory.append('scrap')
        render_inventory()


def box_inside():
    global fourth_code
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
                    if len(box_inside_sprites.sprites()) == 0:
                        inventory.remove('door_key')
                        screen.fill((255, 255, 255), (0, 700, 700, 200))
                        render_inventory()
                    return theatre_left()
                elif code_four.rect.collidepoint(event.pos):
                    code_four.kill()
                    screen.blit(fon, (0, 0))
                    box_inside_sprites.draw(screen)
                    arro_sprites.draw(screen)
                    fourth_code = True
                elif key_theatre_door.rect.collidepoint(event.pos):
                    key_theatre_door.kill()
                    screen.blit(fon, (0, 0))
                    box_inside_sprites.draw(screen)
                    arro_sprites.draw(screen)
                    inventory.append('key_theatre_door')
        render_inventory()


def theatre_right():
    fon = pygame.transform.scale(load_image('theatre_right.png'), (700, 700))
    screen.blit(fon, (0, 0))
    theatre_right_sprites.draw(screen)
    arrows_sprites.draw(screen)  # левая стрелка
    arrow_sprites.draw(screen)  # правая стрелка
    while True:
        render_inventory()
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
                elif theatre_right_crack.rect.collidepoint(event.pos) and 'coin' in inventory:
                    inventory.remove('coin')
                    screen.fill((255, 255, 255), (0, 700, 700, 200))
                    render_inventory()
                    show_fertilizers()


def show_fertilizers():
    fertilizers_sprite.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fertilizers.rect.collidepoint(event.pos):
                    inventory.append('fertilizers')
                    inventory_sprites_fertilizers.draw(screen)
                    return theatre_right()


def show_theatre_right_box():
    global box_key_used
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
                    screen.fill((255, 255, 255), (0, 700, 700, 200))
                    render_inventory()
                    box_key_used = True
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
                elif theatre_back_scene.rect.collidepoint(event.pos) and 'scrap' in inventory:
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
                if water.rect.collidepoint(event.pos):
                    water.kill()
                    screen.blit(fon, (0, 0))
                    seat_sprites.draw(screen)
                    arro_sprites.draw(screen)
                    inventory.append('water')
                elif down_arrow.rect.collidepoint(event.pos):
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
                if comedy.rect.collidepoint(event.pos):
                    comedy.kill()
                    screen.blit(fon, (0, 0))
                    board_sprites.draw(screen)
                    arro_sprites.draw(screen)
                    inventory.append('comedy')
                elif down_arrow.rect.collidepoint(event.pos) and 'comedy' in inventory:
                    inventory.remove('scrap')
                    screen.fill((255, 255, 255))
                    screen.blit(fon, (0, 0))
                    arrows_sprites.draw(screen)  # левая стрелка
                    arrow_sprites.draw(screen)  # правая стрелка
                    board_sprites.draw(screen)
                    return theatre_back()
        render_inventory()


start_screen()
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#    clock.tick(FPS)
#    pygame.display.flip()
#pygame.quit()
