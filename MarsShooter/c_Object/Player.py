###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *
from b_Scene.LoseScene import *

class WeaponState(enum.Enum):
    EBASIC_GUN = 0
    EPRESS_GUN = 1
    ETHREE_WAY = 2

class Player(Object):
    def __init__(self, scene):
        super().__init__()
        # press key를 만들기 위하여 사용
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False
        # 스피드 값
        self.speed = 0
        #이미지 설정
        self.imageSetUp(scene.loadImageFileDict['resource/player/_player (3).png'], 128, 240, 0, 0)
        # nowScene
        self.nowScene = scene
        #체력
        self.health = 1000
        self.score = 0
        #보스등장하기 위한 카운드
        self.bossCount = 0
        #애니메이션 설정
        self.curSpriteImageFile = 3
        self.spriteFilename = []
        for i in range(5):
            self.spriteFilename.append('resource/player/_player (' + str(i + 1) + ').png')
        #이미지 알파값
        self.colorAlphaTime = 0
        #enum
        self.eWeaponState = WeaponState.EBASIC_GUN
        self.spacePress = False
        self.attackTime = 0.1
        self.curWeaponState = 0
        #sound
        self.bulletSound = pygame.mixer.Sound("resource/laser.wav")
        self.bulletSound.set_volume(0.5)
        #실드
        self.isShield = False
        #에드온 개수
        self.add_on_Count = 0
        #무적
        self.isInvincibility = False

    # key
    def key(self, event):
        if event.type in [pygame.KEYDOWN]:
            #move
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.moveLeft = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.moveRight = True
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.moveUp = True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.moveDown = True
            if event.key == pygame.K_SPACE:
                self.spacePress = True
                # 일반 공격이라면
                if self.eWeaponState == WeaponState.EBASIC_GUN:
                    self.nowScene.spriteBulletGroup.add(Bullet('resource/bullet/player bullet_1.png', 7, 66, self.rect.x + 57, self.rect.y - 100, [0, -100], 'Bullet', self.nowScene))
                    self.bulletSound.play()
                elif self.eWeaponState == WeaponState.ETHREE_WAY:
                    self.nowScene.spriteBulletGroup.add(Bullet('resource/bullet/player bullet_1.png', 7, 66, self.rect.x + 57 - 20, self.rect.y - 100, [-20, -100], 'Bullet', self.nowScene))
                    self.nowScene.spriteBulletGroup.add(Bullet('resource/bullet/player bullet_1.png', 7, 66, self.rect.x + 57, self.rect.y - 100, [0, -100], 'Bullet', self.nowScene))
                    self.nowScene.spriteBulletGroup.add(Bullet('resource/bullet/player bullet_1.png', 7, 66, self.rect.x + 57 + 20, self.rect.y - 100, [20, -100], 'Bullet', self.nowScene))
                    self.bulletSound.play()

            #치트키
            #회복
            if event.key == event.key == ord('y'):
                self.health += 100
            #무기 전환
            if event.key == event.key == ord('u'):
                self.curWeaponState += 1

                if self.curWeaponState > len(WeaponState) - 1:
                    self.curWeaponState = 0

                self.eWeaponState = WeaponState(self.curWeaponState)
            #무적 활성화 비 활성화
            if event.key == event.key == ord('i'):
                self.isInvincibility = self.isInvincibility == False
            if event.key == event.key == ord('o'):
                self.bossCount = 50


        elif event.type in [pygame.KEYUP]:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.moveLeft = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.moveRight = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.moveUp = False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.moveDown = False
            if event.key == pygame.K_SPACE:
                self.spacePress = False

    #무기
    def weapon(self):
        if self.eWeaponState == WeaponState.EPRESS_GUN:
            self.attackTime -= 0.012

            if self.spacePress == True and self.attackTime < 0:
                self.attackTime = 0.1
                self.nowScene.spriteBulletGroup.add(Bullet('resource/bullet/player bullet_1.png', 7, 66, self.rect.x + 57, self.rect.y - 100, [0, -100], 'Bullet', self.nowScene))
                self.bulletSound.play()

    # position, speed 설정
    def setUp(self, _posX, _posy, _speed, tag):
        self.rect.x = _posX
        self.rect.y = _posy
        self.speed = _speed
        self.tag = tag

    # 이동
    def move(self, deltatime):
        if self.moveLeft == True:
            self.rect.x -= self.speed * deltatime
        if self.moveRight == True:
            self.rect.x += self.speed * deltatime
        if self.moveUp == True:
            self.rect.y -= self.speed * deltatime
        if self.moveDown == True:
            self.rect.y += self.speed * deltatime

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WINSIZEX:
            self.rect.x = WINSIZEX
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > WINSIZEY:
            self.rect.y = WINSIZEY

    def fadeOut(self, deltatime, delay):
        self.colorAlphaTime += deltatime / delay
        temp = self.lerp(255, 0, self.colorAlphaTime)
        #self.spriteSheet.fill((255, 0, 0, temp), None, pygame.BLEND_RGBA_MULT)
        self.image.set_alpha(self.lerp(0, 255, self.colorAlphaTime))

    #애니메이션
    def animation(self, deltatime):
        posX = self.rect.x
        posY = self.rect.y

        if self.moveLeft == True or self.moveRight == True:
            self.animationTime += deltatime

            if self.animationTime > 0.4:
                if self.curSpriteImageFile < 0:
                    self.curSpriteImageFile = 0
                if self.curSpriteImageFile > 4:
                    self.curSpriteImageFile = 4;

                self.imageSetUpAM(self.nowScene.loadImageFileDict[self.spriteFilename[self.curSpriteImageFile]], 128, 240, 0, 0)
                self.rect.x = posX
                self.rect.y = posY
                if self.moveLeft == True:
                    self.curSpriteImageFile -= 1
                elif self.moveRight == True:
                    self.curSpriteImageFile += 1
                self.animationTime = 0
        else:
            self.curSpriteImageFile = 2
            self.imageSetUpAM(self.nowScene.loadImageFileDict[self.spriteFilename[self.curSpriteImageFile]], 128, 240, 0, 0)
            self.rect.x = posX
            self.rect.y = posY

    #체력바
    def updateHealthbar(self):
        #pygame.draw.rect(self.nowScene.screen, (255,0,0), (190, 850, self.health, 100), 0)
        if self.health > 0:
            self.healthbar = pygame.Surface((self.health, 100), pygame.SRCALPHA).convert_alpha()  # per-pixel alpha
            self.healthbar.fill((255, 0, 0, 128))
            self.nowScene.screen.blit(self.healthbar, (0, 900))


    # 업데이트
    def update(self, deltatime):
        self.nowScene.score.score = self.score
        self.weapon()
        self.move(deltatime)
        self.animation(deltatime)
        self.updateHealthbar()
        self.Collision()
        self.fadeOut(deltatime, 3.0)

    #충돌
    def Collision(self):
        #몬스터 충돌
        if self.isInvincibility == False and len(self.nowScene.spriteEnemyGroup):
            for i in self.nowScene.spriteEnemyGroup:
                if self.rect.colliderect(i.rect) and i.tag != 'Boss' and i.tag != 'BossM':

                    if self.isShield == False and i.die == False:
                        i.die = True
                        self.nowScene.spriteEnemyGroup.remove(i)
                        self.health -= 100
                        temp = Effect('resource/damage.png', 1920, 1080, 0, self.nowScene,
                                      0, 0, False)
                        temp.bFadeOut = True
                        temp.fadeOutDelay = 3.0
                        self.nowScene.spriteEffectGroup.add(temp)
                        print('Player: Enemy 충돌')

                    #실드가 있으면
                    elif self.isShield == True and i.die == False:
                        if len(self.nowScene.spriteGroup):
                            for j in self.nowScene.spriteGroup:
                                if j.tag == 'Shield':
                                    self.nowScene.spriteGroup.remove(j)
                                    self.isShield = False
                        i.die = True
                        self.nowScene.spriteEnemyGroup.remove(i)
                        print('Player: 실드  hit')

        #총알 충돌
        if self.isInvincibility == False and len(self.nowScene.spriteBulletGroup):
            for i in self.nowScene.spriteBulletGroup:
                if (i.tag == 'EnemyAtt' or i.tag == 'EnemyStone') and self.rect.colliderect(i.rect):

                    #실드가 없으며
                    if self. isShield == False and i.die == False:
                        i.die = True
                        self.nowScene.spriteBulletGroup.remove(i)
                        temp = Effect('resource/effect/effect_5.png',512, 512,5, self.nowScene, self.rect.x + random.randint(0, 256) - 128 , self.rect.y + random.randint(0, 256) , True)
                        self.health -= 100
                        temp = Effect('resource/damage.png', 1920, 1080, 0, self.nowScene,
                                      0, 0, False)
                        temp.bFadeOut = True
                        temp.fadeOutDelay = 3.0
                        self.nowScene.spriteEffectGroup.add(temp)
                        print('Player: Boss총알 hit')

                    #실드가 있으면
                    if self.isShield == True and i.die == False:
                        if len(self.nowScene.spriteGroup):
                            for j in self.nowScene.spriteGroup:
                                if j.tag == 'Shield':
                                    self.nowScene.spriteGroup.remove(j)
                                    self.isShield = False
                        i.die = True
                        self.nowScene.spriteBulletGroup.remove(i)
                        print('Player: 실드  hit')
        #아이템 처리
        if len(self.nowScene.spriteItemGroup):
            for i in self.nowScene.spriteItemGroup:
                if self.rect.colliderect(i.rect) and i.die == False:
                    i.die = True
                    #에드온
                    if i.eType == ItemState.EADD_ON:
                        if self.add_on_Count <  4:
                            self.nowScene.spriteGroup.add(Add_on(self.nowScene, self, self.add_on_Count))
                            self.add_on_Count += 1
                    #무기
                    elif i.eType == ItemState.EBULLET:
                        self.curWeaponState += 1

                        if self.curWeaponState > len(WeaponState) - 1:
                            self.curWeaponState = 0

                        self.eWeaponState = WeaponState(self.curWeaponState)
                    #회복
                    elif i.eType == ItemState.ELIFE:
                        self.health += 100
                    #실드
                    elif i.eType == ItemState.ESHIELD:
                        if self.isShield == False:
                            self.isShield = True
                            self.nowScene.spriteGroup.add(Shield(self.nowScene, self))
                    #스피드
                    elif i.eType == ItemState.ESPEED:
                        self.speed += 10

                        if self.speed > 300:
                            self.speed = 300

                    #이펙트 생성
                    temp = Effect('resource/effect/item_effect.png', 512, 512, 5, self.nowScene,
                                  i.rect.x - i.spriteWidth / 2, i.rect.y , True)
                    self.nowScene.spriteEffectGroup.add(temp)
                    #아이템 삭제
                    self.nowScene.spriteItemGroup.remove(i)

        #체력이 없으면
        if self.health < 0 and self.die == False:
            self.die = True
            self.nowScene.spriteGroup.remove(self)
            conn = sqlite3.connect('resource/MarsShooterScore.db')
            cursor = conn.cursor()
            cursor.execute('insert into info (ID, SCORE) values (?, ?)', (self.nowScene.ID, self.score))
            conn.commit()

            self.nowScene.sceneManager['LoseScene'] = self.nowScene.sceneManager['LoseScene'].newScene()
            temp = self.nowScene.sceneManager['LoseScene']
            temp.init(self.nowScene.ID)
            self.nowScene.nextScene = temp
