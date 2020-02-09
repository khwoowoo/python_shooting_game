###  컴퓨터공학과 1학년 ###  20194107  강현우

import pygame
import sys
import math
import enum
from time import sleep
from pygame.locals import *
import urllib.request
import random
from bs4 import BeautifulSoup
import sqlite3
import ctypes

BACKGROUND_COLOR = (255,255,255)
WINSIZEX = int(1920)  # 화면 사이즈
WINSIZEY = int(1080)
FPS = 60

from c_Object.InputBox import *
from a_Framework.Object import *
from a_Framework.Scene import *
from a_Framework.Effect import *
from c_Object.Stage1Background import *


from c_Object.Text import *
from c_Object.Button import *
from c_Object.Shield import *
from c_Object.Item import *
from c_Object.BossLaser import *
from c_Object.EnemyAtt import *
from c_Object.Boss import *
from c_Object.BossM import *
from c_Object.Number import *
from c_Object.Bullet import *
from c_Object.Add_on import *
from c_Object.Player import *
from c_Object.Cut import *
from c_Object.Player_intro import *
from c_Object.EnemyBase import *
from c_Object.Enemy1 import *

from b_Scene.WinScene import *
from b_Scene.LoseScene import *
from b_Scene.State1 import *
from b_Scene.MainScene import *
from b_Scene.LoginScene import *
from b_Scene.IntroScene import *
from b_Scene.LoadScene import *

#항상 씬은 최하휘에 존재해야됨