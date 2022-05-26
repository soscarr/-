from torch.utils.data import DataLoader, Dataset
import torch
import os
import config
from config import ws
from division import seqdiv
from word_sequence import WordSequence



class imdbdataset(Dataset):
    def __init__(self, train):
        super(imdbdataset, self).__init__()
        data_path = r".\data"
        data_path += r"\train" if train else r"\test"
        self.total_path = []
        for path in [r"\pos", r"\neg"]:
            midpath = data_path + path
            print(midpath)
            for i in os.listdir(midpath):
                if i.endswith(".txt"):
                    self.total_path.append(midpath + "\\" + i)


        #print(self.total_path)

    def __getitem__(self, index):

        file = self.total_path[index]
        #words = seqdiv(open(file, encoding="windows-1252").read())
        words = seqdiv(open(file, encoding="utf8").read())
        label = int(file.split("_")[-1].split(".")[0])
        label = 0 if label < 5 else 1
        #print(words, label)
        return words, label

    def __len__(self):
        return len(self.total_path)

def getbatch(batch):
    words, labels = zip(*batch)
    #print(words)
    #print("____________________________________________________________________")
    # ws = WordSequence()
    # for word in words:
    #     ws.fit(word)
    # ws.build_voc(min_count=1)
    # ws.inverse()
    # #print(ws.dict)
    word_maths=[]
    for word in words:
        word = ws.transform(sentence=word, max_len=50)
        word_maths.append(word)
    #print(word_maths)
    words = torch.LongTensor(word_maths)
    labels = torch.LongTensor(labels)
    return words, labels



def get_dataloader(train=True):
    dataset = imdbdataset(train)
    #print(dataset)
    batch_size = config.train_batch_size if train else config.test_batch_size
    #print(batch_size)
    dataloader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, collate_fn=getbatch)

    return dataloader

if __name__ == '__main__':
    for idx, (review, label) in enumerate(get_dataloader(train=True)):
        print(idx)
        print(review)
        print(label)

