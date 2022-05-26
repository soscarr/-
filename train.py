import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import config
from config import device
from dataset import imdbdataset
import dataset
from model import imdbmodel
from tqdm import tqdm
from text import test

model = imdbmodel().to(device)
optimizer = torch.optim.Adam(model.parameters())

loss_list = []

def train(epoch):
    dataloader = dataset.get_dataloader(train=True)
    bar = tqdm(dataloader, total=len(dataloader))

    for index, (input, target) in enumerate(bar):
        input = input.to(device)
        target = target.to(device)
        optimizer.zero_grad()
        output = model.forward(input).to(device)
        loss = F.nll_loss(output, target)
        loss.backward()
        loss_list.append(loss.item())
        optimizer.step()
        bar.set_description("epcoh:{}  idx:{}   loss:{:.6f}".format(epoch, index, np.mean(loss_list)))

        if index%10 == 0:
            torch.save(model.state_dict(), "./models/model.pkl")
            torch.save(optimizer.state_dict(), "./models/optimizer.pkl")

if __name__ == "__main__":
    for i in range(10):
        train(epoch=i)
        test()