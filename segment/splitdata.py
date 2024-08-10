import os
import random
import shutil

# 경로 설정
dataset_dir = 'dataset/images'  # 전체 이미지가 있는 디렉토리
labels_dir = 'dataset/labels'   # 라벨이 있는 디렉토리
train_dir = 'dataset/train'     # 학습용 이미지가 저장될 디렉토리
val_dir = 'dataset/val'         # 검증용 이미지가 저장될 디렉토리

# 학습-검증 데이터 비율 설정
train_ratio = 0.8  # 학습 데이터 비율

# 학습/검증 폴더가 없다면 생성
os.makedirs(os.path.join(train_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'labels'), exist_ok=True)
os.makedirs(os.path.join(val_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(val_dir, 'labels'), exist_ok=True)

# 이미지 파일 리스트 가져오기
images = os.listdir(dataset_dir)
random.shuffle(images)  # 랜덤하게 섞기

# 나누기
train_count = int(len(images) * train_ratio)
train_images = images[:train_count]
val_images = images[train_count:]

def move_files(image_list, target_dir):
    for image in image_list:
        image_path = os.path.join(dataset_dir, image)
        label_path = os.path.join(labels_dir, image.replace('.jpg', '.txt'))  # 라벨 파일 이름

        # 이미지와 라벨을 각각의 디렉토리로 이동
        if os.path.exists(image_path):
            shutil.move(image_path, os.path.join(target_dir, 'images', image))
        if os.path.exists(label_path):
            shutil.move(label_path, os.path.join(target_dir, 'labels', os.path.basename(label_path)))

# 파일 이동
move_files(train_images, train_dir)
move_files(val_images, val_dir)

print("Train/Val 데이터셋 분리가 완료되었습니다.")
