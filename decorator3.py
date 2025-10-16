from decorator2 import decorator


@decorator
def function(sentence):
    sentence = sentence.title()
    print(sentence)
    return sentence


function("nice bags!")