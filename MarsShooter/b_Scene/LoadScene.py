###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class LoadScene(Scene):
    def __init__(self):
        super().__init__()

    def init(self):
        self.loadImageFileDict = {}

        self.imageLoad('resource/background/mainscreen.png')
        self.imageLoad('resource/bullet/player bullet_1.png')
        self.imageLoad('resource/bullet/player_bullet_2.png')
        self.imageLoad('resource/background/background_a1.png')
        self.imageLoad('resource/background/background_a2.png')
        self.imageLoad('resource/damage.png')
        self.imageLoad('resource/player/player.png')
        self.imageLoad('resource/help.png')
        self.imageLoad('resource/intro.png')
        self.imageLoad('resource/rank.png')
        self.imageLoad('resource/cut.png')
        self.imageLoad('resource/enemy/enemy_boss_1_2.png')
        self.imageLoad('resource/effect/effect_1.png')
        self.imageLoad('resource/effect/effect_5.png')
        self.imageLoad('resource/effect/Boom.png')
        self.imageLoad('resource/effect/effect_4.png')
        self.imageLoad('resource/effect/add-on_effect.png')
        self.imageLoad('resource/effect/shield.png')
        self.imageLoad('resource/effect/item_effect.png')
        self.imageLoad('resource/enemy/enemy_bullet_4.png')
        self.imageLoad('resource/enemy/enemy_bullet_3.png')
        self.imageLoad('resource/enemy/enemy bullet_2.png')
        self.imageLoad('resource/enemy/enemy_boss_3.png')
        self.imageLoad('resource/enemy/stone.png')
        self.imageLoad('resource/item/add-on.png')
        self.imageLoad('resource/item/bullet.png')
        self.imageLoad('resource/item/life.png')
        self.imageLoad('resource/item/shield.png')
        self.imageLoad('resource/item/speed up.png')
        self.imageLoad('resource/player/add-on.png')
        self.imageLoad('resource/ingame/GameOver.png')
        self.imageLoad('resource/ingame/mainscreen222.png')
        self.imageLoad('resource/ingame/x.png')
        self.imageLoad('resource/ingame/re.png')
        self.imageLoad('resource/ingame/exit.png')
        self.imageLoad('resource/ingame/help.png')
        self.imageLoad('resource/ingame/intro.png')
        self.imageLoad('resource/ingame/play.png')
        self.imageLoad('resource/ingame/rank.png')
        self.imageLoad('resource/ingame/rank_.png')
        self.imageLoad('resource/ingame/clear.png')
        self.imageLoad('resource/ingame/again.png')
        for i in range(3):
            self.imageLoad('resource/enemy/enemy1 (' + str(i + 1) + ').png')

        for i in range(3):
            self.imageLoad('resource/enemy/enemy2 (' + str(i + 1) + ').png')

        for i in range(3):
            self.imageLoad('resource/enemy/enemy3 (' + str(i + 1) + ').png')

        for i in range(3):
            self.imageLoad('resource/enemy/enemy4 (' + str(i + 1) + ').png')

        for i in range(5):
            self.imageLoad('resource/player/_player (' + str(i + 1) + ').png')

        for i in range(10):
            self.imageLoad('resource/number/' + str(i) + '.png')


        self.sceneManager = {}

        temp = IntroScene(self.loadImageFileDict, self.sceneManager)
        self.sceneManager['IntroScene'] = temp

        temp = Login(self.loadImageFileDict, self.sceneManager)
        self.sceneManager['Login'] = temp

        temp = MainScene(self.loadImageFileDict, self.sceneManager)
        self.sceneManager['MainScene'] = temp

        temp = Stage1(self.loadImageFileDict, self.sceneManager)
        self.sceneManager['Stage1'] = temp

        temp = LoseScene(self.loadImageFileDict, self.sceneManager)
        self.sceneManager['LoseScene'] = temp

        temp = WinScene(self.loadImageFileDict, self.sceneManager)
        self.sceneManager['WinScene'] = temp


        self.sceneManager['IntroScene'].init()
        self.nextScene = self.sceneManager['IntroScene']


    def render(self, screen):
        return

    def key(self, event):
        return

    def update(self, deltatime):
        return

    def remove(self):
        return

    def imageLoad(self, filename):
        self.loadImageFileDict[filename] = pygame.image.load(filename).convert_alpha()