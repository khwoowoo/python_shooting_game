###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

# pygame framework
class framework:
    #start Scene get
    def __init__(self, startScene):
        self.nowScene = startScene

    # pygame 초기화
    def initGame(self):
        pygame.init()
        pygame.mixer.init()

        ctypes.windll.user32.SetProcessDPIAware()
        true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
        '''
        pygame.FULLSCREEN
        pygame.DOUBLEBUF
        pygame.HWSURFACE 
        pygame.OPENGL
        pygame.RESIZABLE
        pygame.NOFRAME
        pygame.SCALED
        '''
        self.screen = pygame.display.set_mode(true_res, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE )  # 화면 사이즈 설정
        pygame.display.set_caption('Shooting')  # 게임이름
        self.clock = pygame.time.Clock()  # 시간
        self.startTime = 0
        self.deltatime = 0
        self.lastTime = 0

    #오브젝트 삭제
    def remove(self):
        self.nowScene.remove()

    #pygame update
    def RunGame(self):
        self.init()                                     #초기화

        while self.nowScene != None:                    #현재씬이 있을 경우까지
            for event in pygame.event.get():
                if event.type in [pygame.QUIT]:
                    pygame.quit()
                    sys.exit()
                    self.remove()                       #마지막 삭제
                else:
                    if event.type in [pygame.KEYDOWN]:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

                    self.nowScene.key(event)            #키값 가져오기

            self.screen.fill(BACKGROUND_COLOR)          # 배경색 설정
            self.Render()                               # 이미지 랜더
            self.Update()                               # 업데이트
            self.nowScene = self.nowScene.nextScene     #다음씬이 생기면 다음씬으로

            self.clock.tick(FPS)                        #프레임 설정
            pygame.display.flip()
            #pygame.display.update()                     #화면 다시 그리기


        pygame.quit()

    #initialize
    def init(self):
        self.deltatime = 0  # 시간
        self.nowScene.init()

    #Rendder
    def Render(self):
        self.nowScene.render(self.screen)

    #update
    def Update(self):
        self.startTime = pygame.time.get_ticks()
        self.deltatime = (self.startTime - self.lastTime) / 200.0
        self.lastTime = self.startTime

        self.nowScene.update(self.deltatime)


#보다 안전하게 실행하기 위하여
if __name__ == "__main__":
    mainScene = LoadScene()
    #mainScene = Stage1('noName')
    game = framework(mainScene)

    game.initGame()
    game.RunGame()
