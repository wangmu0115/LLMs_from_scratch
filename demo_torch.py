import torch

# print(torch.__version__)
# print(torch.cuda.is_available())
# print(torch.backends.mps.is_available())
print(torch.tensor(1))
print(torch.tensor([1, 2, 3], dtype=torch.float32))
print(torch.tensor([[1, 2, 3], [4, 5, 6]]))
print(torch.tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]]))

float_vec = torch.tensor([11.0, 12.2, 13.0])
print(float_vec)
print(float_vec.dtype)
float_vec = float_vec.to(torch.int32)
print(float_vec.dtype)
print(float_vec)
