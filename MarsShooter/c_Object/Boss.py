###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Boss(Object):
    def __init__(self, _posX, _posy, _tag, scene):
        super().__init__()
        # 이미지 설정
        self.imageSetUp(scene.loadImageFileDict['resource/enemy/enemy_boss_1_2.png'], 512, 512, 19,0)
        self.rect.x = _posX
        self.rect.y = _posy
        self.tag = _tag
        self.nowScene = scene
        self.health = 1000
        self.point = 500
        self.attTime = 0.0
        self.laserTime = 0.0
        self.isAtt = False
        self.isAppear = False
        self.moveDir = 1

    def Collision(self):
        if len(self.nowScene.spriteBulletGroup):
            for i in self.nowScene.spriteBulletGroup:
                if (i.tag == 'Bullet' or i.tag == 'Bullet_Add_on') and self.rect.colliderect(i.rect):
                    if i.die == False:
                        self.health -= 5
                        self.hit = True
                        self.nowScene.spriteBulletGroup.remove(i)
                        filename = ''

                        if i.tag == 'Bullet_Add_on':
                            filename = 'resource/effect/add-on_effect.png'
                        else:
                            filename = 'resource/effect/Boom.png'

                        temp = Effect(filename,512, 512,5, self.nowScene, self.rect.x + random.randint(0, 256) - 128 , self.rect.y + random.randint(0, 256) , True)
                        self.nowScene.spriteEffectGroup.add(temp)
                        print('Boss: 총알 hit')

        if self.health  < 0 and self.die == False:
            self.die = True
            if self.nowScene.player.die == False:
                self.nowScene.player.score += self.point
            self.nowScene.isBossDie = True
            self.nowScene.spriteEnemyGroup.remove(self)

            conn = sqlite3.connect('resource/MarsShooterScore.db')
            cursor = conn.cursor()
            cursor.execute('insert into info (ID, SCORE) values (?, ?)', (self.nowScene.ID, self.nowScene.player.score))
            conn.commit()

            self.nowScene.sceneManager['WinScene'] = self.nowScene.sceneManager['WinScene'].newScene()
            temp = self.nowScene.sceneManager['WinScene']
            temp.init(self.nowScene.ID, self.nowScene.score.score + self.point, self.nowScene.player.health)
            self.nowScene.nextScene = temp



    def updateHealthbar(self):
        if self.health > 0:
            self.healthbar = pygame.Surface((self.health , 50), pygame.SRCALPHA).convert_alpha()  # per-pixel alpha
            self.healthbar.fill((255, 0, 0, 128))
            self.nowScene.screen.blit(self.healthbar, (self.rect.x - self.spriteWidth / 2, self.rect.y + 50))

    def attck(self, deltatime):
        self.laserTime += deltatime

        if self.currentFrame == 11 and self.isAtt == False:
            self.isAtt = True
            for i in range(7):
                if i % 2 == 0:
                    self.nowScene.spriteBulletGroup.add(EnemyAtt('resource/enemy/enemy_bullet_4.png', 47, 47, self.rect.x + self.spriteWidth / 2, self.rect.y, [i * 20, 100], 'EnemyAtt', self.nowScene))
                else:
                    self.nowScene.spriteBulletGroup.add(
                        EnemyAtt('resource/enemy/enemy_bullet_4.png', 47, 47, self.rect.x + self.spriteWidth / 2, self.rect.y, [i * -20, 100],
                                 'EnemyAtt', self.nowScene))
        elif self.currentFrame == 19:
            self.isAtt = False

        if self.laserTime >= 10.0:
            self.laserTime = 0.0
            self.nowScene.spriteBulletGroup.add(BossLaser('resource/enemy/enemy_bullet_3.png', 1024, 1024,'BossLaser', self.nowScene, self))

    # 업데이트
    def update(self, deltatime):

        if self.isAppear == True:
            self.updateHealthbar()
            self.Collision()
            self.Animation(deltatime, self.rect.x, self.rect.y)
            self.attck(deltatime)

            self.rect.x += 30 * deltatime * self.moveDir
            self.rect.y += 10 * deltatime * self.moveDir

            if self .rect.x < self.spriteWidth:
                self.moveDir= 1
            elif self.rect.x > WINSIZEX - self.spriteWidth:
                self.moveDir = -1

        else:
            self.rect.y += 50 * deltatime

            if self.rect.y > 0:
                self.isAppear = True


