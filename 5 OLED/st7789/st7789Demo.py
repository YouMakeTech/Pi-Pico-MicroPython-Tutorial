from time import sleep
import random
from st7789 import ST7789

width = 240
height = 240
display = ST7789()
# display = ST7789(width, height, sck=18, mosi=19, dc=20, rst=21, cs=17, bl=22, baudrate=62500000)

class Ball:
    def __init__(self, x, y, r, dx, dy, pen):
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.pen = pen


# initialise shapes
balls = []
for i in range(0, 100):
    r = random.randint(0, 10) + 3
    balls.append(
        Ball(
            random.randint(r, r + (width - 2 * r)),
            random.randint(r, r + (height - 2 * r)),
            r,
            (14 - r) / 2,
            (14 - r) / 2,
            ST7789.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        )
    )

while True:
    display.fill(0)

    for ball in balls:
        ball.x += ball.dx
        ball.y += ball.dy

        xmax = width - ball.r
        xmin = ball.r
        ymax = height - ball.r
        ymin = ball.r

        if ball.x < xmin or ball.x > xmax:
            ball.dx *= -1

        if ball.y < ymin or ball.y > ymax:
            ball.dy *= -1

        display.fill_rect(int(ball.x), int(ball.y), int(ball.r), int(ball.r), ball.pen)

    display.show()
    sleep(0.01)
