__author__ = 'dileep'
# Implementing Boyer Moore string matching
def boyer_moore(text, pattern):
	pat_len = len(pattern)
	ind = []
	flag = 0
	i = 1
	while ind + pat_len <= len(text) and i <= pat_len:
		if pattern[-i] in text[ind:ind+pat_len]:
			ind += text[ind:ind+pat_len] - i