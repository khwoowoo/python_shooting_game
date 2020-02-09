###  컴퓨터공학과 1학년 ###  20194107  강현우
from Header import *

class WeaponState(enum.Enum):
    EBASIC_Att = 0
    EPRESS_Att = 1

class EnemyBase(Object):
    def __init__(self):
        super().__init__()
        # 스피드 값
        self.speed = 0
        # nowScene
        self.nowScene = 0
        self.health = 0
        #이미지 알파값
        self.colorAlphaTime = 0
        self.eWeaponState = WeaponState.EBASIC_Att
        self.hit = False
        self.nowScene = 0
        self.attTime = 0

    def weapon(self):
        pass

    def fadeOut(self, deltatime, delay):
        self.colorAlphaTime += deltatime / delay
        #self.image.set_alpha(self.lerp(0, 255, self.colorAlphaTime))
        temp = self.lerp(255, 0, self.colorAlphaTime)

        if temp < 10:
            self.spriteSheet.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_ADD)
            self.hit = False
            return
        self.spriteSheet.fill((255, 255, 255, temp), None, pygame.BLEND_RGBA_MULT)

    def updateHealthbar(self):
        if self.health > 0:
            # pygame.draw.rect(self.nowScene.screen, (255,0,0), (190, 850, self.health, 100), 0)
            self.healthbar = pygame.Surface((self.health, 10), pygame.SRCALPHA).convert_alpha()  # per-pixel alpha
            self.healthbar.fill((255, 0, 0, 128))
            self.nowScene.screen.blit(self.healthbar, (self.rect.x + self.spriteWidth / 3, self.rect.y))

    def AttState(self, deltatime):
        if self.eWeaponState == WeaponState.EPRESS_Att:
            self.attTime += deltatime
            if self.attTime >= 3:
                self.attTime = 0
                self.nowScene.spriteBulletGroup.add(
                    EnemyAtt('resource/enemy/enemy bullet_2.png', 47, 47, self.rect.x + self.spriteWidth / 2, self.rect.y,[0, 100],'EnemyAtt', self.nowScene))