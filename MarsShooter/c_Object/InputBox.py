###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        #기본 로그인 박스 색 설정
        self.COLOR_INACTIVE = pygame.Color('lightskyblue3')
        #클릭했을때 박스 색 설정
        self.COLOR_ACTIVE = pygame.Color('dodgerblue2')
        #폰트
        self.FONT = pygame.font.Font(None, 32)
        #좌표
        self.rect = pygame.Rect(x, y, w, h)
        #current color(현재 색)
        self.color = self.COLOR_INACTIVE
        #입력했을때 있을 text
        self.text = text
        #화면에 넣어줄 surface
        self.txt_surface = self.FONT.render(text, True, self.color)
        #눌렸을떄
        self.active = False
        #enter했을때 text를  넣어주는
        self.textData = []
        #enter횟수
        self.enterCount = 0

    def key(self, event):
        #마우스 클릭
        if event.type == pygame.MOUSEBUTTONDOWN:
            # rect충돌 마우스와 충돌 했을 경우
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                #상태 클릭마다 바꿔주기
                self.active = not self.active
            else:
                self.active = False

            #만약 클릭이 활성화가 되지 않으면 활성화가 되지 않은 색으로
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE

         #key 입력
        if event.type == pygame.KEYDOWN:
            #활성화가 되었을 경우
            if self.active:
                #enter했을 경우
                if event.key == pygame.K_RETURN:
                    self.textData.append(self.text)
                    self.enterCount += 1
                    print(self.text)
                    self.text = ''
                #지우기
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                #입력
                else:
                    self.text += event.unicode
                #render
                # Re-render the text.
                self.txt_surface = self.FONT.render(self.text, True, self.color)

    #update
    def update(self):
        #크기
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    #render
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    #나중에 로그인할때 검사할때 필요해서 가져오기
    def getTextList(self):
        return  self.textData