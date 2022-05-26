
class WordSequence:
    UNK_TAG = "<UNK>"
    PAD_TAG = "<PAD>"
    PAD = 0
    UNK = 1

    def __init__(self):
        self.dict = {self.UNK_TAG:self.UNK,
                    self.PAD_TAG:self.PAD}
        self.count = {}

    def fit(self, sequence):
        for word in sequence:
            self.count[word] = self.count.get(word, 0) + 1

    def build_voc(self, min_count=5, max_count=None):
        if min_count is not None:
            self.count = {word:count for word, count in self.count.items() if count >= min_count}
        if max_count is not None:
            self.count = {word:count for word, count in self.count.items() if count <= max_count}
        for word in self.count:
            self.dict[word] = len(self.dict)


        #print(self.dict)

    def inverse(self):
        temp = zip(self.dict.values(), self.dict.keys())
        self.inverse_dict = dict(temp)
        #print(self.inverse_dict)

    def transform(self, sentence, max_len=None):
        if len(sentence) > max_len:
            sentence = sentence[:max_len]
        elif len(sentence) < max_len:
            sentence = sentence + [self.PAD_TAG] * (max_len - len(sentence))
        list = [self.dict.get(i, 1) for i in sentence]
        return list
        #print(list)

    def __len__(self):
        return len(self.dict)

if __name__ == '__main__':
    sentences  = [["他妈的","天气","很","好"],
                 ["今天","去","吃","好"]]
    ws = WordSequence()
    for sentence in sentences:
        ws.fit(sentence)
    ws.build_voc(min_count=1)
    ws.inverse()
    #print(ws.dict)
    ret = ws.transform(["好","好","好","好","好","好","好","热","呀"],max_len=10)
    pass
