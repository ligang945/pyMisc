import cPickle as pickle

runtime = '''asd
as
da
s
'''
with open('aaa.txt', 'w') as f:
	r = pickle.dump(runtime, f)

with open('aaa.txt', 'r') as d:
	t = pickle.load(d)
	print(t)
