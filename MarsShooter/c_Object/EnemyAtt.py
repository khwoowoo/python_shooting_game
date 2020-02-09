###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class EnemyAtt(Object):
    def __init__(self, filename, size_w, size_h, posX, posY, direction, _tag, scene):
        super().__init__()
        self.imageSetUp(scene.loadImageFileDict[filename], size_w, size_h, 0, 0)
        self.rect.x = posX
        self.rect.y = posY
        self.tag = _tag
        self.direction = direction
        self.nowScene = scene

    def Collision(self):
        if (self.rect.y > WINSIZEY or self.rect.x < 0 or self.rect.x > WINSIZEX) and self.die == False:
            self.die = True
            self.nowScene.spriteBulletGroup.remove(self)
            print('EnemyAtt: 거리 죽음')

    # 이동
    def move(self, deltatime):
        self.rect.y += deltatime * (self.direction[1])
        self.rect.x += deltatime * (self.direction[0])

    # 업데이트
    def update(self, deltatime):
        self.move(deltatime)
        self.Collision()
