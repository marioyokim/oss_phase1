import pygame
import random

# 초기 설정
pygame.init()
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption('AimLab')
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 이미지 로드
target_image = pygame.image.load('target_image.png')
pointer_image = pygame.image.load('pointer_image.png')

# 포인터 이미지 크기 조절
pointer_image = pygame.transform.scale(pointer_image, (23, 23))

# 마우스 포인터를 숨기기
pygame.mouse.set_visible(False)

# 난이도 설정
difficulty_levels = {
    'easy': {'spawn_interval': 2000, 'min_lifetime': 2000, 'max_lifetime': 4000},
    'medium': {'spawn_interval': 1000, 'min_lifetime': 1000, 'max_lifetime': 2000},
    'hard': {'spawn_interval': 500, 'min_lifetime': 500, 'max_lifetime': 1000}
}