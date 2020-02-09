###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class TypeState(enum.Enum):
    EZERO = 0
    EONE = 1
    ETWO = 2
    ETREE = 3

class Enemy1(EnemyBase):
    def __init__(self, _posX, _posy, _speed, tag, enumState, health, scene, stage):
        super().__init__()
        #이미지 설정
        if stage == 1:
            self.randType = random.randint(1,2)
        else:
            self.randType = random.randint(3, 4)

        self.imageSetUp(scene.loadImageFileDict['resource/enemy/enemy' + str(self.randType) + ' (1).png'], 250, 270, 0, 0)
        self.rect.x = _posX
        self.rect.y = _posy
        self.speed = _speed
        self.tag = tag
        self.health = health
        self.eWeaponState = WeaponState(enumState)
        self.eTypeState = TypeState(self.randType - 1)
        self.nowScene = scene

        if self.eTypeState == TypeState.EONE:
            self.speed += 20
            self.health += 20
        elif self.eTypeState == TypeState.ETWO:
            self.speed += 30
            self.health += 30
        elif self.eTypeState == TypeState.ETREE:
            self.speed += 40
            self.health += 40

        #애니메이션 설정
        self.curSpriteImageFile = 3
        self.spriteFilename = []

        for i in range(3):
            self.spriteFilename.append('resource/enemy/enemy' + str(self.randType) + ' (' + str(i + 1) + ').png')

        self.dir = random.randint(0,2)

    # 이동
    def move(self, deltatime):
        if self.dir == 0:
            self.rect.y += self.speed * deltatime
            self.rect.x += self.speed * deltatime
        elif self.dir == 0:
            self.rect.y += self.speed * deltatime
            self.rect.x -= self.speed * deltatime
        else:
            self.rect.y += self.speed * deltatime

        if self.die == False and (self.rect.y > WINSIZEY or self.rect.x > WINSIZEX or self.rect.x < 0) :
            self.die = True
            self.nowScene.spriteEnemyGroup.remove(self)

    def Collision(self):
        if len(self.nowScene.spriteBulletGroup):
            for i in self.nowScene.spriteBulletGroup:
                if (i.tag == 'Bullet' or i.tag  == 'Bullet_Add_on') and self.rect.colliderect(i.rect):
                    if i.die == False:
                        self.health -= 51
                        self.hit = True
                        self.nowScene.spriteBulletGroup.remove(i)
                        temp_filename = ''
                        if i.tag == 'Bullet':
                            temp_filename= 'resource/effect/effect_1.png'
                        elif i.tag  == 'Bullet_Add_on':
                            temp_filename = 'resource/effect/add-on_effect.png'
                        temp = Effect(temp_filename, 512, 512,5, self.nowScene, self.rect.x - self.spriteWidth / 2, self.rect.y, True)
                        self.nowScene.spriteEffectGroup.add(temp)
                        print('Enemy1: 총알 hit')
        if self.health  < 0 and self.die == False:
            self.die = True
            if self.nowScene.player.die == False:
                self.nowScene.player.bossCount += 1
                self.nowScene.player.score += 10
            self.nowScene.spriteItemGroup.add(Item(self.rect.x, self.rect.y, [self.dir , 50], 'Item', self.nowScene))
            self.nowScene.spriteEnemyGroup.remove(self)

    # 업데이트
    def update(self, deltatime):
        self.weapon()
        self.move(deltatime)
        self.updateHealthbar()
        self.Animation_one(deltatime, self.spriteFilename, 3, self.rect.x, self.rect.y, 250, 270, self.nowScene.loadImageFileDict)
        self.Collision()
        self.AttState(deltatime)

        #if self.hit == True:
        #    self.fadeOut(deltatime, 3)

