###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Stage1Background(Object):
    def __init__(self, posX, posY, speed, _tag, scene, setPos):
        super().__init__()
        # 이미지 설정
        self.spriteWidth = 1920                                           # 이미지 사이즈 설정
        self.spriteHeight = 3240
        self.spriteSheet = scene.loadImageFileDict['resource/background/background_a1.png']
        self.spriteRows = 4                                                  # 이미지 장수(가로)
        self.currentFrame = 0                                               # 이미지 프레임, 애니메이션
        self.image = pygame.Surface((0, 0)).convert_alpha()     # 이미지 사이즈 설정, 아마 충돌할때 필요 할듯

        self.imageRect = (self.spriteWidth * self.currentFrame, 0,                        # 이미지 사각형으로 설정, 아마 애니메이션 할때 필요, 이것은 한장에 모두 있는
                self.spriteWidth, self.spriteHeight)                            # 애니메이션형식

        self.rect = self.image.get_rect()                                       # 이미지 rect가져오기

        self.rect.x = posX
        self.rect.y = posY
        self.speed = speed
        self.tag = _tag
        self.nowScene = scene
        self.setPos = setPos

    def imageChange(self, filename, posX, posY):
        # 이미지 설정
        self.spriteWidth = 1920  # 이미지 사이즈 설정
        self.spriteHeight = 3240
        self.spriteSheet = self.nowScene.loadImageFileDict[filename]
        self.spriteRows = 4  # 이미지 장수(가로)
        self.currentFrame = 0  # 이미지 프레임, 애니메이션
        self.image = pygame.Surface((0, 0)).convert_alpha()  # 이미지 사이즈 설정, 아마 충돌할때 필요 할듯

        self.imageRect = (self.spriteWidth * self.currentFrame, 0,  # 이미지 사각형으로 설정, 아마 애니메이션 할때 필요, 이것은 한장에 모두 있는
                          self.spriteWidth, self.spriteHeight)  # 애니메이션형식

        self.rect = self.image.get_rect()  # 이미지 rect가져오기

        self.rect.x = posX
        self.rect.y = posY

    def move(self, deltatime):
        self.rect.y += self.speed * 0.08

        if self.rect.y > 1080:
            self.rect.y = self.setPos

    # 이미지 한장으로 사용하는 애니메이션 형식
    def animation(self, deltatime, posX, posY):
        self.animationTime += deltatime

        if self.animationTime > 0.4:
            if self.currentFrame >= self.spriteRows:
                self.currentFrame = 0

            self.imageRect = (self.spriteWidth * self.currentFrame, 0,  #이미지의 위치, 크기를 사용하여 처리
                    self.spriteWidth, self.spriteHeight)

            self.currentFrame += 1
            self.animationTime = 0

    def update(self, deltatime):
        self.move(deltatime)
        self.animation(deltatime, self.rect.x, self.rect.y)

    def render(self, screen):
        screen.blit(self.spriteSheet, (self.rect.x, self.rect.y), self.imageRect)


