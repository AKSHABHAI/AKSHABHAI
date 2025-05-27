import pygame
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 480, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player setup
player = pygame.Rect(WIDTH//2 - 25, HEIGHT - 60, 50, 50)
player_speed = 7

# Enemy setup
enemies = []
enemy_speed = 5
spawn_delay = 25
score = 0

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # Spawn enemies
    if random.randint(1, spawn_delay) == 1:
        enemies.append(pygame.Rect(random.randint(0, WIDTH-50), 0, 50, 50))

    # Move enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            score += 1
        if enemy.colliderect(player):
            running = False

    # Draw player and enemies
    pygame.draw.rect(screen, BLUE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Move player based on touch
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] < WIDTH // 2:
                player.x -= player_speed * 2
            else:
                player.x += player_speed * 2

    player.x = max(0, min(WIDTH - player.width, player.x))

    # Show score
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
print("Game Over! Final Score:", score)