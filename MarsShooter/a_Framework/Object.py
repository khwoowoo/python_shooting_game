###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *
x = 0
y = 0
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() # 스프라이트를 사용하기 위해
        self.animationTime = 0              # 애니메이션 시간
        self.curSpriteImageFile = 0         # 애니메이션 현재 프레임
        self.tag = ''                       # 이름
        self.die = False                    #삭제
        self.alphaVal = 255

    #선형보간
    def lerp(self, start, end, time):
        return start + time * (end - start)

    def imageSetUp(self, loadImage, size_width, size_height, rows, Frame):
        self.spriteWidth = size_width                                           # 이미지 사이즈 설정
        self.spriteHeight = size_height
        self.spriteSheet = loadImage
        self.spriteRows = rows                                                  # 이미지 장수(가로)
        self.currentFrame = Frame                                               # 이미지 프레임, 애니메이션
        self.image = pygame.Surface((self.spriteWidth, self.spriteHeight)).convert_alpha()     # 이미지 사이즈 설정, 아마 충돌할때 필요 할듯

        rect = (self.spriteWidth * self.currentFrame, 0,                        # 이미지 사각형으로 설정, 아마 애니메이션 할때 필요, 이것은 한장에 모두 있는
                self.spriteWidth, self.spriteHeight)                            # 애니메이션형식

        self.image.fill((0,0,0, 0))
        #self.image.set_colorkey(pygame.Color(0, 0, 0, 0))                       # 이미지 색상 설정
        self.image.blit(self.spriteSheet, (0, 0), rect)                         # 이미지 랜더
        self.rect = self.image.get_rect()                                       # 이미지 rect가져오기

    def imageSetUpAM(self, loadImage, size_width, size_height, rows, Frame):
        self.spriteWidth = size_width                                           # 이미지 사이즈 설정
        self.spriteHeight = size_height
        self.spriteSheet = loadImage
        self.spriteRows = rows                                                  # 이미지 장수(가로)
        self.currentFrame = Frame                                               # 이미지 프레임, 애니메이션
        self.image = pygame.Surface((self.spriteWidth, self.spriteHeight)).convert_alpha()      # 이미지 사이즈 설정, 아마 충돌할때 필요 할듯

        rect = (self.spriteWidth * self.currentFrame, 0,                        # 이미지 사각형으로 설정, 아마 애니메이션 할때 필요, 이것은 한장에 모두 있는
                self.spriteWidth, self.spriteHeight)                            # 애니메이션형식

        self.image.fill((0,0,0, 0))
        #self.image.set_colorkey(pygame.Color(0, 0, 0, 0))                       # 이미지 색상 설정
        self.image.blit(self.spriteSheet, (0, 0), rect)                         # 이미지 랜더
        self.rect = self.image.get_rect()                                       # 이미지 rect가져오기

    # 이미지 한장으로 사용하는 애니메이션 형식
    def Animation(self, deltatime, posX, posY):
        self.animationTime += deltatime

        if self.animationTime > 0.4:
            if self.currentFrame >= self.spriteRows:
                self.currentFrame = 0

            rect = (self.spriteWidth * self.currentFrame, 0,  #이미지의 위치, 크기를 사용하여 처리
                    self.spriteWidth, self.spriteHeight)

            self.image.fill((0, 0, 0, 0))
            self.image.set_colorkey(pygame.Color(0, 0, 0, 0))  # 이미지 색상 설정
            self.image.blit(self.spriteSheet, (0, 0), rect)  # 이미지 랜더
            self.rect = self.image.get_rect()  # 이미지 rect가져오기
            self.rect.x = posX
            self.rect.y = posY

            self.currentFrame += 1
            self.animationTime = 0

    # 한장 한장씩 출력하여 사용하는 애니메이션 형식
    def Animation_one(self, deltatime, imageListFie, rows, posX, posY, width, height, loadImageFile):
        self.animationTime += deltatime

        if self.curSpriteImageFile == rows:
            self.curSpriteImageFile = 0

        if self.animationTime > 0.4:
            self.imageSetUpAM(loadImageFile[imageListFie[self.curSpriteImageFile]], width, height, 0, 0)
            self.rect.x = posX
            self.rect.y = posY
            self.curSpriteImageFile += 1
            self.animationTime = 0


    def Collision(self):
        pass




