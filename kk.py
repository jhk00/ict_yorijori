import torch
from pathlib import Path

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

# 이미지 폴더 경로 설정
image_folder = Path('images')

# 이미지 파일 리스트 설정 (임의로 5개 파일을 선택)
image_files = list(image_folder.glob('*.jpg'))[:5]

# 이미지 경로 설정
image_paths = [str(image_file) for image_file in image_files]

# 이미지에 대해 예측 수행
results = model(image_paths)

# 결과를 이미지 폴더 내 'results' 폴더에 저장
results.save(save_dir=str(image_folder / 'results'))
