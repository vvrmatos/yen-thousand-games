import pygame
import random

pygame.init()

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Balloonic")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.font.init()
score_font = pygame.font.Font("PressStart2P.ttf", 18)
large_font = pygame.font.Font("PressStart2P.ttf", 30)

pygame.mixer.init()
pygame.mixer.music.load("balloonic.mp3")
pygame.mixer.music.play(-1)
pop_sound = pygame.mixer.Sound("pop_sound.mp3")
pop_sound.set_volume(0.75)

pygame.mouse.set_visible(False)


class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(50, screen_width - 50)
        self.rect.bottom = screen_height + 10
        self.speedy = random.randint(1, 4)

    def update(self):
        self.rect.y -= self.speedy
        if self.rect.bottom < 0:
            self.rect.top = screen_height + 10
            self.rect.centerx = random.randint(50, screen_width - 50)
            self.speedy = random.randint(1, 4)


def add_balloon(all_sprites, balloons):
    balloon = Balloon()
    all_sprites.add(balloon)
    balloons.add(balloon)


def draw_custom_cursor(pos):
    cursor_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
    pygame.draw.polygon(cursor_surface, BLACK, [(0, 0), (20, 10), (0, 20)])
    screen.blit(cursor_surface, pos)


def game_loop():
    global score
    start_ticks = pygame.time.get_ticks()
    score = 0

    all_sprites = pygame.sprite.Group()
    balloons = pygame.sprite.Group()

    for _ in range(10):
        add_balloon(all_sprites, balloons)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in balloons if s.rect.collidepoint(pos)]
                for sprite in clicked_sprites:
                    sprite.kill()
                    pop_sound.play()
                    score += 1

        all_sprites.update()

        if len(balloons) < 10:
            add_balloon(all_sprites, balloons)

        screen.fill(WHITE)
        all_sprites.draw(screen)

        score_text = score_font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        time_left = max(30 - seconds, 0)
        timer_text = score_font.render(f"Time left: {time_left}", True, BLACK)
        screen.blit(timer_text, (screen_width - 250, 10))

        if time_left <= 0:
            running = False

        mouse_pos = pygame.mouse.get_pos()
        draw_custom_cursor(mouse_pos)

        pygame.display.flip()

        pygame.time.Clock().tick(60)

    game_over()


def game_over():
    global score
    screen.fill(WHITE)
    game_over_text = large_font.render(f"Game Over!", True, BLACK)
    screen.blit(
        game_over_text,
        (
            screen_width // 2 - game_over_text.get_width() // 2,
            screen_height // 2 - game_over_text.get_height() // 2 - 50,
        ),
    )
    score_text = large_font.render(f"Score {score}", True, BLACK)
    screen.blit(
        score_text,
        (
            screen.get_width() // 2 - score_text.get_width() // 2,
            screen.get_height() // 2 - score_text.get_height() // 2,
        ),
    )
    play_again_text = score_font.render("Press SPACE to play again", True, BLACK)
    screen.blit(
        play_again_text,
        (
            screen.get_width() // 2 - play_again_text.get_width() // 2,
            screen.get_height() // 2 + score_text.get_height() // 2 + 50,
        ),
    )
    exit_text = score_font.render("Press Esc to leave", True, BLACK)
    screen.blit(
        exit_text,
        (
            screen.get_width() // 2 - exit_text.get_width() // 2,
            screen.get_height() // 2 + score_text.get_height() // 2 + 80,
        ),
    )
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    game_loop()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()


game_loop()
