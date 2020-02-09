###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Button(Object):
    def __init__(self, filename, posX, posY, size_w, size_h, tag, scene):
        super().__init__()
        # 이미지 설정
        self.imageSetUp(scene.loadImageFileDict[filename], size_w, size_h, 0, 0)
        self.rect.x = posX
        self.rect.y = posY
        self.originPosX = posX
        self.originPosY = posY
        self.tag = tag

        #눌렸을떄
        self.isIn = False
        self.active = False

    def key(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.isIn = True
            else:
                self.isIn = False

        #마우스 클릭
        if event.type == pygame.MOUSEBUTTONDOWN:
            # rect충돌 마우스와 충돌 했을 경우
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        else:
            self.active = False

    #update
    def update(self, deltatime):
        if self.isIn == True:
            rect = (self.spriteWidth * 1, 0,  # 이미지의 위치, 크기를 사용하여 처리
                    self.spriteWidth, self.spriteHeight)

            self.image.fill((0, 0, 0, 0))
            self.image.set_colorkey(pygame.Color(0, 0, 0, 0))  # 이미지 색상 설정
            self.image.blit(self.spriteSheet, (0, 0), rect)  # 이미지 랜더
            self.rect = self.image.get_rect()  # 이미지 rect가져오기
            self.rect.x = self.originPosX
            self.rect.y = self.originPosY
        else:
            rect = (self.spriteWidth * 0, 0,  # 이미지의 위치, 크기를 사용하여 처리
                    self.spriteWidth, self.spriteHeight)

            self.image.fill((0, 0, 0, 0))
            self.image.set_colorkey(pygame.Color(0, 0, 0, 0))  # 이미지 색상 설정
            self.image.blit(self.spriteSheet, (0, 0), rect)  # 이미지 랜더
            self.rect = self.image.get_rect()  # 이미지 rect가져오기
            self.rect.x = self.originPosX
            self.rect.y = self.originPosY