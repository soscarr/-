import torch
import torch.nn as nn
import config
from config import ws
import torch.nn.functional as F




class imdbmodel(nn.Module):
    def __init__(self):
        super(imdbmodel,self).__init__()
        self.embedding = nn.Embedding(num_embeddings=len(ws), embedding_dim=200, padding_idx=ws.PAD)
        self.lstm = nn.LSTM(input_size=200, hidden_size=64, num_layers=2, batch_first=True, bidirectional=True, dropout=0.5)
        self.fc1 = nn.Linear(64*2, 64)
        self.fc2 = nn.Linear(64, 2)

    def forward(self, input):
        embeded = self.embedding(input)
        output, (h_n, c_n) = self.lstm(embeded)

        # out :[batch_size,hidden_size*2]
        out = torch.cat([h_n[-1, :, :], h_n[-2, :, :]], dim=-1)  # 拼接正向最后一个输出和反向最后一个输出

        # 进行全连接
        out_fc1 = self.fc1(out)
        # 进行relu
        out_fc1_relu = F.relu(out_fc1)

        # 全连接
        out_fc2 = self.fc2(out_fc1_relu)  # out :[batch_size,2]
        return F.log_softmax(out_fc2, dim=-1)