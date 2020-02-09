###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class IntroScene(Scene):
    def __init__(self, imageLoadFile, sceneManager):
        super().__init__()
        self.loadImageFileDict = imageLoadFile
        self.sceneManager = sceneManager

    def init(self):
        #Sound
        self.music = pygame.mixer.music.load("resource/flourish.mid")
        pygame.mixer.music.set_volume(0.10)  # 1 ~ 0.1
        pygame.mixer.music.play(-1)

        self.background2 = Stage1Background(0, -5400, 50, 'Background2', self, -5300)
        self.background1 = Stage1Background(0, -2160 ,50, 'Background1', self, -5300)
        self.backgroundImageChange = False


        #게임 오브젝트 생성
        self.spriteGroup = []
        self.spriteGroup = pygame.sprite.RenderPlain(*self.spriteGroup)

        self.player = Player_intro(self)
        self.spriteGroup.add(self.player)

        self.spriteGroup.add(Cut(self, self.player))

        self.text1 = Text(800,00, 100, 1000, '<introScene>')
        self.text = Text(700, 950, 100, 1000, '<Press the spacebar!!>')

        self.spaceCount = 0


    def render(self, screen):
        self.screen = screen
        self.background1.render(screen)
        self.background2.render(screen)

        if len(self.spriteGroup) != 0:
            self.spriteGroup.draw(screen)

        self.text.draw(screen)
        self.text1.draw(screen)

    def key(self, event):
        if event.type in [pygame.KEYDOWN]:
            if event.key == pygame.K_SPACE:
                self.spaceCount += 1

        # self.player.key(event)
        for i in self.spriteGroup:
            if i.tag == 'Player_intro':
                i.key(event)

    def update(self, deltatime):
        if self.spaceCount >= 4:
            self.sceneManager['Login'].init()
            self.nextScene = self.sceneManager['Login']
            return

        #모든 스프라이트 생성
        self.background1.update(deltatime)
        self.background2.update(deltatime)
        self.spriteGroup.update(deltatime)

    def remove(self):
        for i in self.spriteGroup:
            self.spriteGroup.remove(i)