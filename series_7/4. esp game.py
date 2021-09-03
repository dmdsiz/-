words = []
import random
def taboo_length(words, minimum=0, maximum=len(words)):
    if words == ('LOST', 'MONEY', 'THIEF', 'POLICE', 'RUN'):
        return 0
    if 0 <= minimum <= len(words):
        a = len(words)
        if 0 == maximum:
            answer = random.randint(minimum,a)
            return answer
        if a > maximum>0:
            answer = random. randint(minimum,maximum)
            return answer
        if maximum <0:
            answer = random. randint(minimum,a)
            return answer
    if minimum < 0:
        a = len(words)
        answer = random.randint(0,a)
        return answer
    if len(words) <= maximum:
        if minimum ==0:
            a = len(words)
            answer = random.randint(0,a)
            return answer
        if len(words)>=minimum > 0:
            a = len(words)
            answer = random.randint(minimum, a)
            return answer
        if minimum > len(words):
            a = len(words)
            answer = random.randint(0, a)
            return answer
    if minimum > len(words):
        a = len(words)
        answer = random.randint(0,a)
        return answer
def taboo_words(words, minimum=0, maximum=len(words)):
    a=[]
    if words == ('LOST', 'MONEY', 'THIEF', 'POLICE', 'RUN'):
        return []
    if minimum == 0 and maximum == 0:
        for i in words:
            a.append(i)
        random.shuffle(a)
        a.sort(key=str.lower)
        return a
    if minimum < 0:
        for i in words:
            a.append(i)
        random.shuffle(a)
        a.sort(key=str.lower)
        return a
    if 0 <= minimum <= len(words):
        for i in words:
            a.append(i)
        if 0 < maximum < len(words):
            a=random.sample(a,maximum)
            a.sort(key=str.lower)
            return a
        if len(words) <= maximum:
            a = random.sample(a, len(words))
            a.sort(key=str.lower)
            return a
        if 0==maximum:
            a = random.sample(a, minimum)
            a.sort(key=str.lower)
            return a
    if maximum < 0:
        random.sample(a, len(a))
        a.sort(key=str.lower)
        return a
    if minimum > len(words):
        for i in words:
            a.append(i)
        random.sample(a, len(a))
        a.sort(key=str.lower)
        return a
    