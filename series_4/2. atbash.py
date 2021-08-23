line = int(input())
for i in range(1,line+1):
	sentence = str(input())
	translator = str.maketrans('AaBbCcDdEeFfGgHhIiJjKkLlMmZzYyXxWwVvUuTtSsRrQqPpOoNn', 'ZzYyXxWwVvUuTtSsRrQqPpOoNnAaBbCcDdEeFfGgHhIiJjKkLlMm')
	print(str(sentence).translate(translator))