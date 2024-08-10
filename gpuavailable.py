import torch

# GPU 사용 가능 여부 확인
if torch.cuda.is_available():
    print(f"GPU is available: {torch.cuda.get_device_name(0)}")
    print(f"GPU memory allocated: {torch.cuda.memory_allocated(0)} bytes")
    print(f"GPU memory cached: {torch.cuda.memory_reserved(0)} bytes")

    # 간단한 연산을 GPU에서 수행하여 검증
    a = torch.tensor([1.0, 2.0, 3.0]).cuda()
    b = torch.tensor([4.0, 5.0, 6.0]).cuda()
    c = a + b
    print(f"Result of tensor addition on GPU: {c}")
    print(f"Is tensor 'c' on GPU: {c.is_cuda}")
else:
    print("GPU is not available, using CPU.")
