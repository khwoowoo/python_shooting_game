###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Stage1(Scene):
    def __init__(self, imageLoadFile, sceneManager):
        super().__init__()
        self.loadImageFileDict = imageLoadFile
        self.sceneManager = sceneManager

    def newScene(self):
        return Stage1(self.loadImageFileDict, self.sceneManager)

    def init(self, ID):
        self.ID = ID

        #Sound
        self.music = pygame.mixer.music.load("resource/town.mid")
        pygame.mixer.music.set_volume(0.5)  # 1 ~ 0.1
        pygame.mixer.music.play(-1)

        self.background2 = Stage1Background(0, -5400, 50, 'Background2', self, -5300)
        self.background1 = Stage1Background(0, -2160 ,50, 'Background1', self, -5300)
        self.backgroundImageChange = False

        self.score = Number(1300, 100, 'Number', self)

        #게임 오브젝트 생성
        self.player = Player(self)
        self.player.setUp(960, 900, 200, 'Player')
        self.spriteGroup = [self.player]
        self.spriteGroup = pygame.sprite.RenderPlain(*self.spriteGroup)

        self.spriteEffectGroup = []
        self.spriteEffectGroup = pygame.sprite.RenderPlain(*self.spriteEffectGroup)
        self.MonsterCreativeTime = 0
        self.isBoss = False
        self.isBossDie = False
        self.isBossM = False
        self.isBossMDie = False

        #Boss(WINSIZEX / 2 - 128, 0, 'Boss', self)
        #BossM(WINSIZEX / 2 - 128, -1024, 'BossM', self)
        self.spriteEnemyGroup = []
        self.spriteEnemyGroup = pygame.sprite.RenderPlain(*self.spriteEnemyGroup)

        self.spriteBulletGroup = []
        self.spriteBulletGroup = pygame.sprite.RenderPlain(*self.spriteBulletGroup)

        self.spriteItemGroup = []
        self.spriteItemGroup = pygame.sprite.RenderPlain(*self.spriteItemGroup)

        #RenderPlain클래스는 여러개의 스프라이트를 묶어주는 역활

    def render(self, screen):
        self.screen = screen
        self.background1.render(screen)
        self.background2.render(screen)
        self.score.render(screen)

        if len(self.spriteBulletGroup) != 0:
            self.spriteBulletGroup.draw(screen)
        if len(self.spriteEnemyGroup) != 0:
            self.spriteEnemyGroup.draw(screen)
        if len(self.spriteGroup) != 0:
            self.spriteGroup.draw(screen)
        if len(self.spriteEffectGroup) != 0:
            self.spriteEffectGroup.draw(screen)
        if len(self.spriteItemGroup) != 0:
            self.spriteItemGroup.draw(screen)

    def key(self, event):
        # self.player.key(event)
        for i in self.spriteGroup:
            if i.tag == 'Player':
                i.key(event)

    def update(self, deltatime):
        #몬스터 생성
        self.MonsterCreativeTime += deltatime

        if self.MonsterCreativeTime > 7.0 and (self.isBossM == False or self.isBossMDie == True) and (self.isBoss == False or self.isBossDie == True):
            self.MonsterCreativeTime = 0
            if self.isBossMDie == False:
                self.spriteEnemyGroup.add(Enemy1(random.randint(200, 1720), 100 ,random.randint(10, 30), 'Enemy1', random.randint(0,1), 100, self, 1))
            else:
                self.spriteEnemyGroup.add(
                    Enemy1(random.randint(200, 1720), 100, random.randint(10, 30), 'Enemy1', random.randint(0, 1), 100,
                           self, 2))

        if self.player.die == False and self.player.bossCount >= 50 and self.isBossM == False:
            self.isBossM = True
            self.spriteEnemyGroup.add(BossM(WINSIZEX / 2 - 128, -1024, 'BossM', self))
        elif self.player.die == False and self.player.bossCount >= 50 and self.isBoss == False and self.isBossMDie == True:
            self.isBoss = True
            self.spriteEnemyGroup.add(Boss(WINSIZEX / 2 - 128, -1024, 'Boss', self))

        if self.isBossMDie == True and self.backgroundImageChange == False:
            self.backgroundImageChange = True
            self.background2.imageChange('resource/background/background_a2.png', self.background2.rect.x, self.background2.rect.y)
            self.background1.imageChange('resource/background/background_a2.png', self.background1.rect.x, self.background1.rect.y)


        #모든 스프라이트 생성
        self.background1.update(deltatime)
        self.background2.update(deltatime)
        self.spriteGroup.update(deltatime)
        self.spriteBulletGroup.update(deltatime)
        self.spriteEnemyGroup.update(deltatime)
        self.spriteEffectGroup.update(deltatime)
        self.spriteItemGroup.update(deltatime)

    def remove(self):
        for i in self.spriteGroup:
            self.spriteGroup.remove(i)
        for i in self.spriteBulletGroup:
            self.spriteBulletGroup.remove(i)
        for i in self.spriteEnemyGroup:
            self.spriteEnemyGroup.remove(i)
        for i in self.spriteEffectGroup:
            self.spriteEffectGroup.remove(i)
        for i in self.spriteItemGroup:
            self.spriteItemGroup.remove(i)