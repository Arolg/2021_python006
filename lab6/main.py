from random import randrange as rnd, choice
import math
import time
import pygame
import pygame.draw as draw

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255,165,0)
RED = (255, 0, 0)
FPS = 30
n = int(2)
l0 = 20
zleep = 3
pygame.init()
screen = pygame.display.set_mode((800, 600))  # 800, 600
screen.fill(WHITE)


class ball():
    def __init__(self, x=40, y=450):
        """
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        draw.circle(screen, self.color, (self.x, self.y), self.r)
        self.live = 30

    def set_coords(self):
        draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):
        """Переместить мяч по прошествии единицы времени."""

        if self.x >= 800:
            self.vx *= -1
        if self.y >= 600:
            self.vy *= -0.5
        #self.vy += 1
        self.x += self.vx
        self.y += self.vy
        self.set_coords()

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r) ** 2:
            return True
        else:
            return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = BLACK

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        x, y = event.pos
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((y - new_ball.y) / (x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self):
        """Прицеливание. Зависит от положения мыши."""
        [x, y] = pygame.mouse.get_pos()
        if pygame.mouse.get_pos():
            if x != 20:
                self.an = math.atan((y - 450) / (x - 20))
            else:
                if y - 450 > 0:
                    self.an = math.pi / 2
                else:
                    self.an = -math.pi / 2

        if self.f2_on:
            self.color = ORANGE
        else:
            self.color = BLACK

        draw.line(screen, self.color, (20, 450), (20 + max(self.f2_power, 20) * math.cos(self.an), 450 + max(self.f2_power, 20) * math.sin(self.an)), 7)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            draw.line(screen, ORANGE, (20, 450), (50, 420), 7)
        else:
            draw.line(screen, BLACK, (20, 450), (50, 420), 7)


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        # draw.circle(screen, RED, 0, 0)
        self.new_target()


    def new_target(self):
        """новая цель. """
        x = self.x = rnd(500, 600)
        y = self.y = rnd(300, 500)
        r = self.r = rnd(20, 50)
        self.vx = 0
        self.vy = 0
        color = self.color = 'red'
        draw.circle(screen, color, (x, y), r)
        # canvas.coords(self.id, x - r, y - r, x + r, y + r)
        # canvas.itemconfig(self.id, fill=color)

    def set_coords(self):
        draw.circle(screen, self.color, (self.x, self.y), self.r)

    def move(self):

        self.x += self.vx
        self.y += self.vy
        if self.x >= 800 or self.x <= 0:
            self.vx *= -1
        if self.y >= 600 or self.y <= 0:
            self.vy *= -1
        self.vx += self.acceleration()[0]
        self.vy += self.acceleration()[1]
        if abs(self.vx) > 5:
            self.vx -= self.acceleration()[0]
        if abs(self.vy) > 5:
            self.vy -= self.acceleration()[1]
        self.set_coords()

    def acceleration(self):
        ax = 0.01
        ay = 0.01
        for i in targets:
            if i.x != self.x and i.y != self.y:
                l = ((i.x - self.x) ** 2 + (i.x - self.x) ** 2) ** 0.5
                a = l - l0
                ax = a * self.x / l * 0.0001
                ay = a * self.y / l * 0.0001
        return [ax, ay]

    def hit(self, points=1):
        """Попадание шарика в цель."""
        pygame.display.update()
        # screen.fill(WHITE)
        self.x = -50
        self.y = -50
        self.points += points


glob_points = 0
font = pygame.font.Font(None, 50)

def glob_point():
    text_score = font.render(str(glob_points), True, BLACK)
    screen.blit(text_score, [30, 30])


targets = []
squares = []

g1 = gun()
bullet = 0
balls = []
clock = pygame.time.Clock()
glob_point()
lives = 1


def empty(event):
    pass


def hit_happens():
    global bullet, lives, glob_points, balls
    screen.fill(WHITE)
    text = font.render("Вы уничтожили цель за: " + str(bullet) + " выстрелов", True, BLACK)
    screen.blit(text, [100, 250])
    pygame.display.update()
    balls = []
    lives = 0
    glob_points += 1


def new_game():
    global gun, t1, screen1, balls, bullet, glob_points, targets
    for i in range(n):
        targets.append(target())
    for i in targets:
        i.new_target()
        i.live = 1
    bullet = 0
    balls = []


    z = 0.03
    all_live = n
    while (all_live or balls):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                g1.fire2_start(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                g1.fire2_end(event)

        g1.targetting()
        for t in targets:
            t.move()
            t.set_coords()
        for s in squares:
            s.move()
            s.set_coords()
        for b in balls:
            b.move()
            b.set_coords()
            for t in targets:
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    all_live -= 1
                    glob_points += 1
                    glob_point()
                if not all_live:
                    hit_happens()
            if not all_live:
                targets = []
                balls = []
            pygame.display.update()

        text_score = font.render(str(glob_points), True, BLACK)
        screen.blit(text_score, [30, 30])
        pygame.display.update()
        g1.power_up()
        g1.targetting()
        g1.power_up()
        screen.fill(WHITE)  # для исчезания прошлого рисунка
    time.sleep(zleep)
    new_game()


new_game()