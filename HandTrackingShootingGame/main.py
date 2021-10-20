import cv2
import mediapipe as mp
import time
import handTrackingModule as htm
import pygame
import math
import random

pygame.init()

Size = 1500

kills = 0

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
cap.set(3, Size)
cap.set(4, Size)

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)

ZombieX, ZombieY = random.randint(0, Size - 400), 400


def ShootGuns():
    global ZombieX
    global ZombieY
    global kills
    ShotGunShot.play()
    if abs(x10 - ZombieX) < 75 and abs(y10 - ZombieY) < 75:
        ZombieX, ZombieY = random.randint(0, Size - 400), 400
        kills += 1


screen = pygame.display.set_mode((Size - 200, Size - 800))
Mouse = pygame.transform.scale(pygame.image.load("use153.png"), (50, 50))
Zombie = pygame.transform.scale(pygame.image.load("Zombie.png"), (150, 150))
BG = pygame.transform.scale(pygame.image.load("BG.png"), (Size - 200, Size - 800))
GUN = pygame.transform.scale(pygame.image.load("output-onlinepngtools.png"), (300, 300))
ShotGunShot = pygame.mixer.Sound("ShotGun.mp3")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    screen.blit(BG, (0, 0))
    font = pygame.font.Font("freesansbold.ttf", 32)
    if len(lmList) != 0:
        x12, y12 = lmList[12][1], lmList[12][2]
        x8, y8 = lmList[8][1], lmList[8][2]
        x10, y10 = lmList[10][1], lmList[10][2]
        # print(abs(x12 - x8) and abs(y12 - y8))
        screen.blit(Zombie, (ZombieX, ZombieY))
        screen.blit(Zombie, (ZombieX, ZombieY))
        screen.blit(GUN, (x10, 400))
        screen.blit(Mouse, (x10, y10))
        textKills = font.render("Kills: " + str(kills), True, RED, BLUE)
        screen.blit(textKills, (5, 5))
        pygame.display.update()
        if abs(x12 - x8) < 15 and abs(y12 - y8) < 15:
            ShootGuns()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    # cv2.imshow("Image", img)
    cv2.waitKey(1)
