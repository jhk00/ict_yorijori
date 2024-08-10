yaml_content = """
train: ./images  # Test 이미지를 사용하여 추가 학습
val:  # Validation 데이터셋 없이 학습
test:  # Test 데이터셋 없이 학습

nc: 9
names: ['양배추/채소류', '닭가슴살/식육가공품 및 포장육', '오이/채소류', '달걀/난류', '고추/채소류', '대파/채소류', '양파/채소류', '돼지고기/육류', '토마토/채소류']
"""

# 현재 디렉토리(~/ict/yolov5)에 'dataset.yaml' 파일 생성 및 작성
with open('dataset.yaml', 'w') as f:
    f.write(yaml_content)
