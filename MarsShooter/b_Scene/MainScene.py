###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class MainScene(Scene):
    def __init__(self, imageLoadFile, sceneManager):
        super().__init__()
        self.loadImageFileDict = imageLoadFile
        self.sceneManager = sceneManager

    def newScene(self):
        return MainScene(self.loadImageFileDict, self.sceneManager)

    def init(self , ID):
        #Sound
        self.ID = ID

        self.music = pygame.mixer.music.load("resource/town.mid")
        pygame.mixer.music.set_volume(0.10)  # 1 ~ 0.1
        pygame.mixer.music.play(-1)

        self.background = self.loadImageFileDict['resource/background/mainscreen.png']

        self.spriteGroup = []
        self.spriteGroup = pygame.sprite.RenderPlain(*self.spriteGroup)



        self.Button1 = Button('resource/ingame/play.png', 500, 500, 256, 128, 'play', self)
        self.spriteGroup.add(self.Button1)

        self.Button2 = Button('resource/ingame/intro.png', 800, 500, 300, 128, 'intro', self)
        self.spriteGroup.add(self.Button2)

        self.Button3 = Button('resource/ingame/rank.png', 1200, 500, 256, 128, 'rank', self)
        self.spriteGroup.add(self.Button3)

        self.Button4 = Button('resource/ingame/help.png', 500, 800, 256, 128, 'help', self)
        self.spriteGroup.add(self.Button4)

        self.Button5 = Button('resource/ingame/exit.png', 800, 800, 256, 128, 'exit', self)
        self.spriteGroup.add(self.Button5)

        self.introWindow = Object()
        self.introWindow.imageSetUp(self.loadImageFileDict['resource/intro.png'], 1920, 1080, 0, 0)
        self.introWindow.rect.y = -1080
        self.introWindow.rect.x = 0
        self.introWindow.tag = 'introWindow'
        self.spriteGroup.add(self.introWindow)

        self.healWindow = Object()
        self.healWindow.imageSetUp(self.loadImageFileDict['resource/help.png'], 1920, 1080, 0, 0)
        self.healWindow.rect.y = -1080
        self.healWindow.rect.x = 0
        self.healWindow.tag = 'healWindow'
        self.spriteGroup.add(self.healWindow)

        self.rankWindow = Object()
        self.rankWindow.imageSetUp(self.loadImageFileDict['resource/rank.png'], 1920, 1080, 0, 0)
        self.rankWindow.rect.y = -1080
        self.rankWindow.rect.x = 0
        self.rankWindow.tag = 'rankWindow'
        self.spriteGroup.add(self.rankWindow)

        #데이터 가져오기
        conn = sqlite3.connect('resource/MarsShooterScore.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('select * from info')
        rows = cursor.fetchall()

        self.randText = []
        self.rankDict = {}

        for i in rows:
            self.rankDict[i['SCORE']] = i['ID']

        count = 0
        for i in sorted(self.rankDict.keys(), reverse=True):
            if count == 6:
                break
                #760
            self.randText.append(Text(-1000, (110 * count) + 300, 100, 1000, str(self.rankDict[i]) + ' ' + str(i)))
            count += 1

        self.mainButton = Button('resource/ingame/x.png', 1500, -500, 256, 256, 'main', self)
        self.spriteGroup.add(self.mainButton)


        self.isDefferent = False


    def render(self, screen):
        screen.blit(self.background, (0, 0))
        if len(self.spriteGroup) != 0:
            self.spriteGroup.draw(screen)

        for i in self.randText:
            i.draw(screen)

    def key(self, event):
        # self.player.key(event)
        if len(self.spriteGroup) != 0:
            for i in self.spriteGroup:
                if i.tag == 'play' or i.tag == 'intro' or i.tag == 'rank' or i.tag == 'help' or i.tag == 'exit' or i.tag == 'main' :
                    i.key(event)

    def update(self, deltatime):
        self.spriteGroup.update(deltatime)

        if len(self.spriteGroup) != 0:
            for i in self.spriteGroup:
                if i.tag == 'play' and self.isDefferent == False:
                    if i.active == True:
                        self.isDefferent = True
                        self.sceneManager['Stage1'] =  self.sceneManager['Stage1'].newScene()
                        temp = self.sceneManager['Stage1']
                        temp.init(self.ID)
                        self.nextScene = temp
                elif i.tag == 'exit' and self.isDefferent == False:
                    if i.active == True:
                        pygame.quit()
                        sys.exit()
                elif i.tag == 'help' and self.isDefferent == False:
                    if i.active == True:
                        self.isDefferent = True
                        self.healWindow.rect.y = 0
                        self.mainButton.originPosY = 300
                elif i.tag == 'intro' and self.isDefferent == False:
                    if i.active == True:
                        self.isDefferent = True
                        self.introWindow.rect.y = 0
                        self.mainButton.originPosY = 300
                elif i.tag == 'rank' and self.isDefferent == False:
                    if i.active == True:
                        self.isDefferent = True
                        self.rankWindow.rect.y = 0
                        self.mainButton.originPosY = 300
                        for i in self.randText:
                            i.rect.x = 760
                elif i.tag == 'main':
                    if i.active == True and self.isDefferent== True:
                        self.isDefferent = False
                        self.rankWindow.rect.y = -1080
                        self.healWindow.rect.y = -1080
                        self.introWindow.rect.y = -1080
                        for i in self.randText:
                            i.rect.x = -1000
                        self.mainButton.originPosY = -500



    def remove(self):
        for i in self.spriteGroup:
            self.spriteGroup.remove(i)