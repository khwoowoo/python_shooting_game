###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Effect(Object):
    def __init__(self, filename, width, height, frame, scene, posX, posY, animation):
        super().__init__()
        #이미지 설정
        self.imageSetUp(scene.loadImageFileDict[filename], width, height, frame, 0)
        self.rect.x = posX
        self.rect.y = posY
        self.bAnimation = animation
        self.bFadeOut = False
        self.fadeOutDelay = 0.0
        self.bKeep = False


        #이미지 알파값
        self.colorAlphaTime = 0

        self.nowScene = scene


    def fadeOut(self, deltatime, delay):
        self.colorAlphaTime += deltatime / delay
        #self.image.set_alpha(self.lerp(0, 255, self.colorAlphaTime))
        temp = self.lerp(255, 0, self.colorAlphaTime) - 100

        if temp < 0 and self.die == False:
            self.die = True
            self.nowScene.spriteEffectGroup.remove(self)
            return

        self.image.fill((255, 0, 0, temp))

    # 이미지 한장으로 사용하는 애니메이션 형식
    def Animation(self, deltatime, posX, posY):
        self.animationTime += deltatime

        if self.animationTime > 0.4:
            if self.currentFrame >= self.spriteRows:
                if self.bKeep == False:
                    if self.die == False:
                        self.die = True
                        self.nowScene.spriteEffectGroup.remove(self)
                    else:
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

    # 업데이트
    def update(self, deltatime):
        if self.bAnimation:
            #self.Animation(deltatime, self.spriteFilename, len(self.spriteFilename), self.rect.x, self.rect.y, self.spriteWidth, self.spriteHeight)
            self.Animation(deltatime, self.rect.x, self.rect.y)
        if self.bFadeOut:
            self.fadeOut(deltatime, self.fadeOutDelay)