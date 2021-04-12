import pygame
from time import sleep

# initialize things

# create window with size (our image size)
window = pygame.display.set_mode((700, 400))  # track 1
window = pygame.display.set_mode((1155, 399))  # track 2



# load image file
bg = pygame.image.load("track1.png")
bg = pygame.image.load("track2.png")

car = pygame.image.load("car.png")
car = pygame.transform.scale(car, (40, 40))  # resize car image


# set up timer clock
clock = pygame.time.Clock()


car_x = 30
car_y = 260

GO_CAR = 25
direction = 'y_up'
run = 1


while run:
    clock.tick(30)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = 0


    window.blit(bg, (0, 0))
    window.blit(car, (car_x, car_y))

    last_x, last_y = car_x, car_y

    center_x, center_y = (int(car_x + 40 / 2), int(car_y + 40 / 2))
    pygame.draw.circle(window, (0, 255, 255), (center_x, center_y), 5, 5)


    cal_value = 30
    y_up = window.get_at((center_x, center_y - cal_value))[0]
    y_down = window.get_at((center_x, center_y + cal_value))[0]
    x_right = window.get_at((center_x + cal_value, center_y))[0]
    x_left = window.get_at((center_x - cal_value, center_y))[0]
    print("y_up   ", y_up)
    print("y_down ", y_down)
    print("x_right", x_right)
    print("x_left ", x_left)
    print("-----------")


    # go up
    if y_up == 255 and direction == 'y_up' and x_left != 255 and x_right != 255:
        # move up
        car_y -= 2

    # make the turn
    if y_up == 255 and direction == 'y_up' and x_left != 255 and x_right == 255:
        # make a right turn
        direction = 'x_right'
        car_y -= GO_CAR
        car_x += GO_CAR
        car = pygame.transform.rotate(car, -90)
        window.blit(car, (car_x, car_y))
        print('Turn Right')

    #  x right
    elif y_up != 255 and direction == 'x_right' and y_down != 255 and x_right == 255:
        car_x += 2

    elif y_down == 255 and direction == 'x_right' and x_left == 255 and x_right == 255:
        # make a turn from x_right
        car = pygame.transform.rotate(car, -90)
        direction = 'y_down'
        car_y += GO_CAR + 5
        car_x += GO_CAR
        window.blit(car, (car_x, car_y))
        print('Turn Right')

    # y down
    elif y_down == 255 and direction == 'y_down' and x_left != 255 and x_right != 255:
        # move down
        car_y += 2

    # left turn
    elif y_down == 255 and direction == 'y_down' and x_left != 255 and x_right == 255:
        # turn from y_down
        car = pygame.transform.rotate(car, 90)
        direction = 'x_right'
        car_y += GO_CAR
        car_x += GO_CAR
        print('Turn left')

    # turn to y up
    elif y_up == 255 and direction == 'x_right' and x_left == 255 and x_right == 255:
        # turn from y_down
        car = pygame.transform.rotate(car, 90)
        direction = 'y_up'
        car_y -= GO_CAR + 5
        car_x += GO_CAR
        print('Turn left')

    # if car is stopped
    if car_x == last_x and car_y == last_y:
        # stop the engine sound
        print("STOPPED")

    pygame.display.update()  # update the window

pygame.quit()
