import torch
from pathlib import Path
import math

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

# 이미지 폴더 경로 설정
image_folder = Path('images')

# 이미지 파일 리스트 설정
image_files = list(image_folder.glob('*.jpg'))

# 배치 사이즈 설정
batch_size = 100

# 총 배치 수 계산
num_batches = math.ceil(len(image_files) / batch_size)

for i in range(num_batches):
    # 배치에 해당하는 이미지 파일 리스트 추출
    batch_files = image_files[i * batch_size:(i + 1) * batch_size]
    image_paths = [str(image_file) for image_file in batch_files]

    # 이미지에 대해 예측 수행
    results = model(image_paths)

    # 결과를 저장 (각 배치 결과를 별도 폴더에 저장)
    results.save(save_dir=str(image_folder / f'results_batch_{i+1}'))
    print(f'Batch {i+1}/{num_batches} processed.')
