###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class ItemState(enum.Enum):
    EADD_ON = 0
    EBULLET = 1
    ELIFE = 2
    ESHIELD = 3
    ESPEED = 4

class Item(Object):
    def __init__(self, posX, posY, direction, _tag, scene):
        super().__init__()
        self.eType  = ItemState(random.randint(0, 4))

        if self.eType == ItemState.EADD_ON:
            self.imageSetUp(scene.loadImageFileDict['resource/item/add-on.png'], 256, 256, 0, 0)
        elif self.eType == ItemState.EBULLET:
            self.imageSetUp(scene.loadImageFileDict['resource/item/bullet.png'], 256, 256, 0, 0)
        elif self.eType == ItemState.ELIFE:
            self.imageSetUp(scene.loadImageFileDict['resource/item/life.png'], 256, 256, 0, 0)
        elif self.eType == ItemState.ESHIELD:
            self.imageSetUp(scene.loadImageFileDict['resource/item/shield.png'], 256, 256, 0, 0)
        elif self.eType == ItemState.ESPEED:
            self.imageSetUp(scene.loadImageFileDict['resource/item/speed up.png'], 256, 256, 0, 0)

        self.rect.x = posX
        self.rect.y = posY
        self.tag = _tag
        self.direction = direction
        self.nowScene = scene

    def Collision(self):
        if (self.rect.y < 0 or self.rect.y > WINSIZEY or self.rect.x < 0 or self.rect.x > WINSIZEX) and self.die == False:
            self.die = True
            self.nowScene.spriteItemGroup.remove(self)
            print('Item: 거리 죽음')

    # 이동
    def move(self, deltatime):
        self.rect.y += deltatime * (self.direction[1])
        self.rect.x += deltatime * (self.direction[0])

    # 업데이트
    def update(self, deltatime):
        self.move(deltatime)
        self.Collision()
