###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Cut(Object):
    def __init__(self, scene, player):
        super().__init__()
        self.imageSetUp(scene.loadImageFileDict['resource/cut.png'], 512, 256, 0, 0)
        self.tag = 'Cut'
        self.nowScene = scene
        self.playerAddress = player
        self.curSprite = 0

    def move(self):
        self.rect.x = self.playerAddress.rect.x
        self.rect.y = self.playerAddress.rect.y


    def animation(self):
        self.curSprite = self.nowScene.spaceCount

        if self.curSprite < 0:
            self.curSprite = 0
        if self.curSprite > 4:
            self.curSprite = 4;

        rect = (self.spriteWidth * self.curSprite , 0,  #이미지의 위치, 크기를 사용하여 처리
                    self.spriteWidth, self.spriteHeight)

        self.image.fill((0, 0, 0, 0))
        self.image.set_colorkey(pygame.Color(0, 0, 0, 0))  # 이미지 색상 설정
        self.image.blit(self.spriteSheet, (0, 0), rect)  # 이미지 랜더
        self.rect = self.image.get_rect()  # 이미지 rect가져오기


    # 업데이트
    def update(self, deltatime):
        self.animation()
        self.move()

