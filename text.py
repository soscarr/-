import config
from config import device
from model import imdbmodel
from dataset import get_dataloader
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from tqdm import tqdm





def test():
    model = imdbmodel().to(device)
    model.load_state_dict(torch.load("./models/model.pkl"))
    test_dataloader = get_dataloader(train=False)
    loss_list = []
    acc_list = []
    bar = tqdm(test_dataloader, total=len(test_dataloader))
    print(device)
    print(torch.cuda.get_device_name(0))
    with torch.no_grad():

        for index, (input, target) in enumerate(bar):

            input = input.to(device)
            target = target.to(device)
            output = model(input).to(device)
            loss = F.nll_loss(output, target)
            loss_list.append(loss.item())
            pred = output.max(dim=-1)[-1]
            acc_list.append(pred.eq(target).cpu().float().mean())
    bar.set_description("loss mean:{},acc mean:{}".format(np.mean(loss_list), np.mean(acc_list)))

if __name__ == "__main__":
    test()

