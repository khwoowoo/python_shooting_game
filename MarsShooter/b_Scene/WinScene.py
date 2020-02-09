###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class WinScene(Scene):
    def __init__(self, imageLoadFile, sceneManager):
        super().__init__()
        self.loadImageFileDict = imageLoadFile
        self.sceneManager = sceneManager

    def newScene(self):
        return WinScene(self.loadImageFileDict, self.sceneManager)

    def init(self, ID, score, health):
        self.ID = ID
        #Sound
        self.music = pygame.mixer.music.load("resource/town.mid")
        pygame.mixer.music.set_volume(0.10)  # 1 ~ 0.1
        pygame.mixer.music.play(-1)

        self.background = self.loadImageFileDict['resource/ingame/mainscreen222.png']

        self.score = Number(790, 340, 'Number', self)
        self.score.score = score

        self.spriteGroup = []
        self.spriteGroup = pygame.sprite.RenderPlain(*self.spriteGroup)

        self.gameClear = Object()
        self.gameClear.imageSetUp(self.loadImageFileDict['resource/ingame/clear.png'], 1920, 1080, 0, 0)
        self.gameClear.tag = 'gameClear'
        self.spriteGroup.add(self.gameClear)

        self.Button1 = Button('resource/ingame/again.png', 1420, 810, 512, 256, 'return', self)
        self.spriteGroup.add(self.Button1)

        rankFame = 0
        if health > 900:
            rankFame = 0
        elif health > 800:
            rankFame = 1
        elif health > 700:
            rankFame = 2
        elif health > 600:
            rankFame = 3
        elif health > 500:
            rankFame = 4
        elif health > 400:
            rankFame = 5
        elif health > 300:
            rankFame = 6

        self.rank = Object()
        self.rank.imageSetUp(self.loadImageFileDict['resource/ingame/rank_.png'], 146, 256, 0, rankFame)
        self.rank.tag = 'rank'
        self.rank.rect.x = 895
        self.rank.rect.y = 540
        self.spriteGroup.add(self.rank)


    def render(self, screen):
        screen.blit(self.background, (0, 0))
        if len(self.spriteGroup) != 0:
            self.spriteGroup.draw(screen)
        self.score.render(screen)

    def key(self, event):
        # self.player.key(event)
        if len(self.spriteGroup) != 0:
            for i in self.spriteGroup:
                if i.tag == 'return':
                    i.key(event)

    def update(self, deltatime):
        self.spriteGroup.update(deltatime)

        if len(self.spriteGroup) != 0:
            for i in self.spriteGroup:
                if i.tag == 'return':
                    if i.active == True:
                        self.sceneManager['MainScene'] = self.sceneManager['MainScene'].newScene()
                        temp = self.sceneManager['MainScene']
                        temp.init(self.ID)
                        self.nextScene = temp

    def remove(self):
        for i in self.spriteGroup:
            self.spriteGroup.remove(i)