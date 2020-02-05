
import torch


def predict(width: int, height: int, bytes: []) -> int:
    print(width, height, bytes)
    data = torch.Tensor()
    model = torch.load('qmnist_cnn.pt')
    model.eval()
    output = model(data)
    pred = output.argmax(dim=1, keepdim=True) 
    return pred
