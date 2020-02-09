###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class LoseScene(Scene):
    def __init__(self, imageLoadFile, sceneManager):
        super().__init__()
        self.loadImageFileDict = imageLoadFile
        self.sceneManager = sceneManager

    def newScene(self):
        return LoseScene(self.loadImageFileDict, self.sceneManager)

    def init(self, ID):
        self.ID = ID
        #Sound
        self.music = pygame.mixer.music.load("resource/town.mid")
        pygame.mixer.music.set_volume(0.10)  # 1 ~ 0.1
        pygame.mixer.music.play(-1)

        self.background = self.loadImageFileDict['resource/ingame/mainscreen222.png']

        self.spriteGroup = []
        self.spriteGroup = pygame.sprite.RenderPlain(*self.spriteGroup)

        self.gameOver = Object()
        self.gameOver.imageSetUp(self.loadImageFileDict['resource/ingame/GameOver.png'], 1920, 1080, 0, 0)
        self.gameOver.tag = 'GameOver'
        self.spriteGroup.add(self.gameOver)

        self.Button1 = Button('resource/ingame/x.png', 600, 500, 256, 256, 'Exit', self)
        self.spriteGroup.add(self.Button1)

        self.Button1 = Button('resource/ingame/re.png', 1070, 500, 256, 256, 'reGame', self)
        self.spriteGroup.add(self.Button1)




    def render(self, screen):
        screen.blit(self.background, (0, 0))
        if len(self.spriteGroup) != 0:
            self.spriteGroup.draw(screen)

    def key(self, event):
        # self.player.key(event)
        if len(self.spriteGroup) != 0:
            for i in self.spriteGroup:
                if i.tag == 'Exit' or i.tag == 'reGame':
                    i.key(event)

    def update(self, deltatime):
        self.spriteGroup.update(deltatime)

        if len(self.spriteGroup) != 0:
            for i in self.spriteGroup:
                if i.tag == 'reGame':
                    if i.active == True:
                        self.sceneManager['Stage1'] = self.sceneManager['Stage1'].newScene()
                        temp = self.sceneManager['Stage1']
                        temp.init(self.ID)
                        self.nextScene = temp
                elif i.tag == 'Exit':
                    if i.active == True:
                        self.sceneManager['MainScene'] = self.sceneManager['MainScene'].newScene()
                        temp = self.sceneManager['MainScene']
                        temp.init(self.ID)
                        self.nextScene = temp

    def remove(self):
        for i in self.spriteGroup:
            self.spriteGroup.remove(i)