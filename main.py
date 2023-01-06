import pygame
import sys
import os


pygame.init()
FPS = 60
start = False
size = WIDTH, HEIGHT = 700, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Название игры')
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
arrows_sprites = pygame.sprite.Group()


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

left_arrow = pygame.sprite.Sprite(arrows_sprites)
left_arrow.image = load_image("left_arrow.png")
left_arrow.image = pygame.transform.scale(left_arrow.image, (WIDTH / 3, HEIGHT / 3))
left_arrow.rect = left_arrow.image.get_rect()
left_arrow.rect.x = 10
left_arrow.rect.y = HEIGHT - HEIGHT / 3

theatre_button = pygame.sprite.Sprite(select_level_sprites)
theatre_button.image = load_image("theatre_button.png")
theatre_button.image = pygame.transform.scale(theatre_button.image, (WIDTH / 2, HEIGHT / 2))
theatre_button.rect = theatre_button.image.get_rect()
theatre_button.rect.x = WIDTH / 6
theatre_button.rect.y = HEIGHT / 2 - HEIGHT / 6


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
    fon = pygame.transform.scale(load_image('start_screen.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    select_level_text = ["Выбор уровня:"]
    font = pygame.font.Font(None, 60)
    text_coord = HEIGHT / 4
    for line in select_level_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        rules_rect = string_rendered.get_rect()
        text_coord += 10
        rules_rect.top = text_coord
        rules_rect.x = WIDTH / 4
        text_coord += rules_rect.height
        screen.blit(string_rendered, rules_rect)
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
                    return


def show_rules():
    fon = pygame.transform.scale(load_image('rules_screen.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    rules_text = ["Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]
    font = pygame.font.Font(None, 30)
    text_coord = 400
    for line in rules_text:
        string_rendered = font.render(line, True, pygame.Color('black'))
        rules_rect = string_rendered.get_rect()
        text_coord += 10
        rules_rect.top = text_coord
        rules_rect.x = 200
        text_coord += rules_rect.height
        screen.blit(string_rendered, rules_rect)
    arrows_sprites.draw(screen)
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.rect.collidepoint(event.pos):
                    return start_screen()


start_screen()
screen.fill((123, 231, 213))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((123, 231, 213))
    all_sprites.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
