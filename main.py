import pygame
from sys import exit
# Game by Jimmy Logan
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Block Rally')
clock = pygame.time.Clock()

lx = 150
ly = 236
rx = 600
ry = 236
bx = 354

jumpingL = False
jumpingR = False
BlockR = False
gravity = 5
jump_heightL = 25
jump_velL = jump_heightL
jump_heightR = 25
jump_velR = jump_heightR
block_vel = 5

font = pygame.font.SysFont('freesansbold.ttf', 25)
score = 0
hiscore = 0
# background and sprites
bg_surface = pygame.Surface((800,400))
bg_surface.fill('beige')
ground_surface = pygame.Surface((800,100))
ground_surface.fill('darkseagreen4')
left_player = pygame.Rect(lx, ly, 48, 64)
right_player = pygame.Rect(rx, ry, 48, 64)
block = pygame.Rect(bx, 100, 64, 64)
# Z and X controls left and right rectangles respectively
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                jumpingL = True
            if event.key == pygame.K_x:
                jumpingR = True
# left player jump mechanic
    if jumpingL:
        left_player.y -= jump_velL
        jump_velL -= gravity
        if jump_velL < -jump_heightL:
            jumpingL = False
            jump_velL = jump_heightL
# right player jump mechanic
    if jumpingR:
        right_player.y -= jump_velR
        jump_velR -= gravity
        if jump_velR < -jump_heightR:
            jumpingR = False
            jump_velR = jump_heightR
# moves the block left and right
    if BlockR:
        block.x += block_vel
    else:
        block.x -= block_vel
# collision detection
    collide_L = pygame.Rect.colliderect(left_player, block)
    collide_R = pygame.Rect.colliderect(right_player, block)
# left player collision conditions
    if collide_L:
        left_player.y -= jump_velL
        jump_velL -= gravity
        BlockR = True
        block_vel += 0.5
        score += 1
# right player collision conditions
    if collide_R:
        right_player.y -= jump_velR
        jump_velR -= gravity
        BlockR = False
        block_vel += 0.5
        score += 1
# resets the block position, speed, and score if the block goes off-screen
    if block.x >= 800 or block.x <= -64:
        block.x = 354
        score = 0
        block_vel = 5
# keeps track of high score
    if hiscore < score:
        hiscore = score
# displays the backgrounds, sprites, score, high-score, and controls
    screen.blit(bg_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen, 'green', left_player)
    pygame.draw.rect(screen, 'red', right_player)
    pygame.draw.rect(screen,'yellow', block)
    text = font.render("Score: " + str(score), True, 'black')
    hiscoretext = font.render("High Score: " + str(hiscore), True, 'black')
    controltext = font.render("Controls:", True, 'black')
    Ztext = font.render("Z - Left Jump", True, 'black')
    Xtext = font.render("X - Right Jump", True, 'black')
    screen.blit(text, [10, 10])
    screen.blit(hiscoretext, [10, 30])
    screen.blit(controltext, [675, 10])
    screen.blit(Ztext,[675, 25])
    screen.blit(Xtext, [675, 40])

    pygame.display.update()
    clock.tick(30)
