import torch
import torch.nn as nn

criterion = nn.MSELoss()


def build_model(in_size):
    n = nn.Sequential(nn.Linear(in_size, in_size * 2),
                      nn.ReLU(),
                      nn.Linear(in_size * 2, in_size * 2),
                      nn.ReLU(),
                      nn.Linear(in_size * 2, in_size),
                      nn.Sigmoid()
                      )

    optimizer = torch.optim.Adam(n.parameters(), 0.00005)  # attenzione!
    return n, optimizer


def generate(model, seed, training):
    seed = torch.tensor(seed, dtype=torch.float32)
    output = model(seed)
    return output if training else output.tolist()


def train(model, optimizer, input_, target):
    output = generate(model, input_, True)
    target = torch.tensor(target, dtype=torch.float32)
    loss = criterion(output, target)
    print(loss)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    return output.tolist()


def save(model):
    torch.save(model.parameters, '\storto.pt')
    print('done')


def load(model):
    model.parameters = torch.load('\storto.pt')
    save(model)
    print(model.parameters)

