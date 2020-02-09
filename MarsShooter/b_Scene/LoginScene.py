###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Login(Scene):
    def __init__(self, imageLoadFile, sceneManager):
        super().__init__()
        self.loadImageFileDict = imageLoadFile
        self.sceneManager = sceneManager

    def init(self):
        #Sound
        self.music = pygame.mixer.music.load("resource/onestop.mid")
        pygame.mixer.music.set_volume(0.5)  # 1 ~ 0.1
        pygame.mixer.music.play(-1)

        #배경 설정
        self.background = self.loadImageFileDict['resource/background/mainscreen.png']

        self.text = Text(700, 950, 100, 1000, '<Login Please!>')

        self.box = InputBox(540, 540, 0, 100, "")
        self.pinNumber = ''

        #pin_number get
        with open("resource/url_pin.txt", "r") as file:
            page = urllib.request.urlopen(file.read()).read()
            soup = BeautifulSoup(page, 'html.parser')  # 뷰티풀 수프 객체 생성

            table = soup.find('div', {'class': 'se-module se-module-text'})
            for i in table.find_all('p'):
                for i in i.find_all('span'):
                    self.pinNumber = i.text
                    start = self.pinNumber.find('= ') + 2
                    self.pinNumber = self.pinNumber[start: len(self.pinNumber)]


    def render(self, screen):
        screen.blit(self.background, (0, 0))
        # screen.blit(pygame.transform.scale(self.background, (int(1920* 0.7), int(1080 * 0.7))), (0, 0))

        self.box.draw(screen)
        self.text.draw(screen)

    def key(self, event):
        self.box.key(event)
        if event.type in [pygame.KEYDOWN]:
            #씬 전환
            if event.key == pygame.K_F1:
                temp = self.sceneManager['MainScene']
                temp.init('noName')
                self.nextScene = temp

    def update(self, deltatime):
        self.box.update()

        if self.box.enterCount == 2:
            conn = sqlite3.connect('resource/MarsShooter.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('select * from Info')
            rows = cursor.fetchall()

            for row in rows:
                if row['PIN'] == self.pinNumber and row['ID'] == self.box.getTextList()[0] and row['PS'] == self.box.getTextList()[1]:
                    self.sceneManager['MainScene'] = self.sceneManager['MainScene'].newScene()
                    temp = self.sceneManager['MainScene']
                    temp.init(self.box.getTextList()[0])
                    self.nextScene = temp
                    return


    def remove(self):
        return