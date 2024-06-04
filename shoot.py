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

# 표적 클래스 정의
class Target:
    def __init__(self, x, y, size):
        settings = difficulty_levels[difficulty]
        self.image = pygame.transform.scale(target_image, (size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.size = size
        self.creation_time = pygame.time.get_ticks()
        self.lifetime = random.randint(settings['min_lifetime'], settings['max_lifetime'])

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
# 폰트, 텍스트 설정
def display_message(message, position, font_size=48):
    font = pygame.font.SysFont(None, font_size)
    text = font.render(message, True, BLACK)
    screen.blit(text, position)
    
# 제목, 난이도 버튼
def difficulty_selection():  
    selected_difficulty = None
    while selected_difficulty is None:
        screen.fill(WHITE)
        display_message('AimLab', (355, 100), font_size=72) 
        display_message('Select Difficulty:', (310, 250)) 
        easy_button = pygame.Rect(290, 320, 200, 50) 
        normal_button = pygame.Rect(290, 390, 200, 50)  
        hard_button = pygame.Rect(290, 460, 200, 50)  

        display_message('Easy', (395, 330))  
        display_message('Normal', (395, 400))  
        display_message('Hard', (395, 470))  

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(mouse_pos):
                    selected_difficulty = 'easy'
                elif normal_button.collidepoint(mouse_pos):
                    selected_difficulty = 'medium'
                elif hard_button.collidepoint(mouse_pos):
                    selected_difficulty = 'hard'
    return selected_difficulty

# 메인 게임
def main_game(difficulty):

    targets = []
    score = 0
    last_spawn_time = pygame.time.get_ticks()
    spawn_interval = difficulty_levels[difficulty]['spawn_interval']

    # 제한 시간 설정 (초)
    game_duration = 30
    start_time = pygame.time.get_ticks()
    end_time = start_time + game_duration * 1000

    # 게임 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 마우스 왼쪽 클릭
                hit = False
                for target in targets:
                    if target.is_clicked(event.pos):
                        targets.remove(target)
                        score += 1
                        hit = True
                        break

        # 화면 업데이트
        screen.fill(WHITE)
        
        # 새로운 표적 생성
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > spawn_interval:
            x, y = random.randint(50, 850), random.randint(50, 650)
            size = random.randint(20, 50)
            targets.append(Target(x, y, size))
            last_spawn_time = current_time

        # 표적 그리기 및 제거
        for target in targets[:]:
            target.draw(screen)
            if current_time - target.creation_time > target.lifetime:  # 랜덤 수명 후에 사라짐
                targets.remove(target)
                score -= 1  # 클릭하지 않으면 점수 감소

        # 제한 시간 체크
        remaining_time = (end_time - current_time) // 1000
        if remaining_time <= 0:
            running = False

        # 점수 및 남은 시간 표시
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_text, (10, 10))
        time_text = font.render(f'Time: {remaining_time}', True, BLACK)
        screen.blit(time_text, (800, 10))

        # 마우스 포인터
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(pointer_image, (mouse_pos[0] - pointer_image.get_width() / 2, mouse_pos[1] - pointer_image.get_height() / 2))

        # 프레임 설정 및 디스플레이
        pygame.display.flip()
        clock.tick(60)
        
# 메인 게임 루프
while True:
    difficulty = difficulty_selection()
    main_game(difficulty)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()