import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        return x_exp / torch.sum(x_exp)


class MySoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        max_x = torch.max(x)
        x_exp = torch.exp(x - max_x)
        return x_exp / torch.sum(x_exp)


# test softmax
softmax = MySoftmax()
data = torch.Tensor([1, 2, 300000000])
output = softmax(data)
print(output)

# test softmax stable
softmax_stable = MySoftmaxStable()
data_stable = torch.Tensor([1, 2, 3])
output_stable = softmax_stable(data_stable)
print(output_stable)
