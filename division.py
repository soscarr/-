import re

def seqdiv(sentence):
    fileters = ['!', '"', '#', '$', '%', '&', '\(', '\)', '\*', '\+', ',', '-', '\.', '/', ':', ';', '<', '=', '>',
                '\?', '@', '\[', '\\', '\]', '^', '_', '`', '\{', '\|', '\}', '~', '\t', '\n', '\x97', '\x96', '”',
                '“', ]
    sentence = sentence.lower()
    sentence = re.sub("<br />", " ", sentence)
    sentence = re.sub("I'm", "I am", sentence)
    sentence = re.sub("it's", "it is", sentence)
    sentence = re.sub("Let's", "Let us", sentence)
    sentence = re.sub("let's", "let us", sentence)
    sentence = re.sub("isn't", "is not", sentence)
    sentence = re.sub("|".join(fileters), " ", sentence)
    result = [i for i in sentence.split(" ") if len(i)>0]

    return result

if __name__=="__main__":
    print(seqdiv("It's my great hornor to have an opportunity to stand here, and introduce myself to you. "))