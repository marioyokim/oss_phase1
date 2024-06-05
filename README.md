# oss_phase1 : AimLab
AimLab은 무작위로 생성되는 표적을 최대한 많이 맞춰서 점수를 얻는 게임입니다.

# Reference
https://github.com/pygame/pygame 

# 지원 OS
Windows

# 실행 방법
1. Python 설치
2. pygame 설치
3. 이미지 파일들을 shoot.py와 같은 경로에 저장
4. shoot.py 실행

# 실행 예시
![AimLabUbuntu2024-06-0521-09-05-ezgif com-video-to-gif-converter](https://github.com/marioyokim/oss_phase1/assets/164159203/dd6654e6-6f2d-4fa0-b639-b16f89afae6c)

# 코드 설명
* 코드가 있는 shoot.py과 과녁 이미지인 target_image.png, 마우스 포인터 이미지인 pointer_image.png로 구성
* Target class : 과녁에 대한 클래스. 난이도에 따라 생성 인터벌과 수명이 달라짐.
* main_game : 메인 게임을 수행하는 코드. 표적을 창 내에 무작위로 생성하며, 맞출 시 점수 1점을 얻고, 못 맞출 시 점수 1점을 잃는다.

# TO DO
* 점수를 서버에 저장하여 랭킹 구현
* 정해진 과녁 수를 최대한 빠른 시간 안에 맞추는 모드 구현
* 맞추면 점수를 더 많이 주지만 못 맞출 시 점수를 더 많이 잃는 스페셜 과녁 구현

