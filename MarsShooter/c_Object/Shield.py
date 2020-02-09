###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Shield(Object):
    def __init__(self, scene, player):
        super().__init__()
        self.imageSetUp(scene.loadImageFileDict['resource/effect/shield.png'], 256, 256, 5, 0)
        self.tag = 'Shield'
        self.nowScene = scene
        self.playerAddress = player
        self.life = 1

    def Collision(self):
        if self.die == False and self.life <= 0:
            self.die = True
            self.nowScene.spriteBulletGroup.remove(self)

    def move(self):
        self.rect.x = self.playerAddress.rect.x - 60
        self.rect.y = self.playerAddress.rect.y - 50


    # 업데이트
    def update(self, deltatime):
        self.move()
        self.Collision()
        self.Animation(deltatime, self.rect.x, self.rect.y)
