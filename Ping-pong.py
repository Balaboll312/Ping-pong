import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")


paddle_width, paddle_height = 10, 100
ball_size = 15


class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)

    def move(self, dy):
        self.rect.y += dy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1


def main():
    clock = pygame.time.Clock()
    running = True

    paddle1 = Paddle(30)
    paddle2 = Paddle(WIDTH - 30 - paddle_width)
    ball = Ball()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move(-5)
        if keys[pygame.K_s]:
            paddle1.move(5)
        if keys[pygame.K_UP]:
            paddle2.move(-5)
        if keys[pygame.K_DOWN]:
            paddle2.move(5)

        ball.move()

       
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.dx *= -1

       
        if ball.rect.left <= 0 or ball.rect.right >= WIDTH:
            ball.rect.x = WIDTH // 2 - ball_size // 2
            ball.rect.y = HEIGHT // 2 - ball_size // 2
            ball.dx *= random.choice([-1, 1])
            ball.dy *= random.choice([-1, 1])

       
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, paddle1.rect)
        pygame.draw.rect(screen, WHITE, paddle2.rect)
        pygame.draw.ellipse(screen, WHITE, ball.rect)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()