###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class Scene:
    def __init__(self):
        self.nextScene = self

    # tag로 스프라이트 객체 가져오기
    def getSprite(self, group, spriteTag):
        for i in group:
            if i.tag == spriteTag:
                return i
        return None

    def init(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def key(self, event):
        pass

    def update(self, deltatime):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError
#raise NotImplementedError 오류 일부러 발생시키기