###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Number:
    def __init__(self, posX, posY, _tag, scene):
        self.numSprite = []

        for i in range(10):
            self.numSprite.append(Object())
            self.numSprite[i].imageSetUp(scene.loadImageFileDict['resource/number/' + str(0) + '.png'], 0, 0, 0, 0)
            self.numSprite[i].rect.x = i * 50

        self.posX = posX
        self.posY = posY
        self.tag = _tag
        self.nowScene = scene
        self.score = 0

    def render(self, screen):

        temp = self.score
        for i in reversed(range(10)):
            temp1 = temp % 10
            self.numSprite[i].imageSetUp(self.nowScene.loadImageFileDict['resource/number/' + str(temp1) + '.png'], 0, 0, 0, 0)
            self.numSprite[i].rect.x = i * 50
            temp //= 10
            screen.blit(self.numSprite[i].spriteSheet, (self.numSprite[i].rect.x + self.posX, self.numSprite[i].rect.y + self.posY))
