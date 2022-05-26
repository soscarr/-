from word_sequence import WordSequence
from dataset import imdbdataset
import pickle
import os

class creatdict():
    ws = WordSequence()

    def __init__(self):
        dataset = imdbdataset(train=True)
        print( len(dataset) )

        words = []
        for idx in range(len(dataset)):
            (word, label) = dataset.__getitem__(idx)
            words.append(word)

        #print("____________________________________________________________________")

        for word in words:
            self.ws.fit(word)
        self.ws.build_voc(min_count=1)
        self.ws.inverse()
        pickle.dump(self.ws, open("./ws.pkl", "wb"))



if __name__ == "__main__":
    ct = creatdict()
    print(ct.ws.dict)