import pickle
import torch
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print("torch.cuda.is_available() = " + str(torch.cuda.is_available()))
print("process unit = " + str(device))
train_batch_size = 512
test_batch_size = 500

ws = pickle.load(open("./ws.pkl","rb"))






max_len = 50