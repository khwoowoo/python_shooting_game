###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class BossLaser(Object):
    def __init__(self, filename, size_w, size_h, _tag, scene, player):
        super().__init__()
        self.imageSetUp(scene.loadImageFileDict[filename], size_w, size_h, 2, 0)
        self.rect.x = random.randint(0, 896)
        self.rect.y = 56
        self.tag = _tag
        self.nowScene = scene
        self.lifeTime = 0
        self.playerAddress = player
        self.playerDamage = 0.0
        self.playerHit = False

    def Collision(self, deltatime):
        if self.lifeTime >= 5 and self.die == False:
            self.die = True
            self.nowScene.spriteBulletGroup.remove(self)

        if len(self.nowScene.spriteGroup):
            if self.playerAddress.rect.x > self.rect.x and self.rect.x + self.spriteWidth > self.playerAddress.rect.x + self.playerAddress.spriteWidth and self.playerAddress.die == False \
                    and self.playerHit == False:
                self.playerHit = True
                self.playerDamage += deltatime
                if self.playerDamage >= 2.0:
                    self.playerDamage = 0.0
                    self.playerHit = False

                self.playerAddress.health -= 20
                temp = Effect('resource/damage.png', 1920, 1080, 0, self.nowScene, 0, 0, False)
                temp.bFadeOut = True
                temp.fadeOutDelay = 3.0
                self.nowScene.spriteEffectGroup.add(temp)
                print('Player: Laser 충돌')

    # 업데이트
    def update(self, deltatime):
        self.lifeTime += deltatime
        self.Collision(deltatime)
        self.Animation(deltatime, self.rect.x, self.rect.y)
