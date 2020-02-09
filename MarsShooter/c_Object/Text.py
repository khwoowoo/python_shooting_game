###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Text:
    def __init__(self, x, y, w, h, text=''):
        #폰트
        self.FONT = pygame.font.Font(None, 80)
        #좌표
        self.rect = pygame.Rect(x, y, w, h)
        #입력했을때 있을 text
        self.text = text
        #화면에 넣어줄 surface
        self.txt_surface = self.FONT.render(text, True, (255,255,255))

    #render
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
