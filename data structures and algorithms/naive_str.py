__author__ = 'dileep'
# Naive string matching
def naive_str(text, pattern) -> list:
	"""Naive string matching
	:param text: Str
	:param pattern: Str
	returns indices of matches"""
	pat_len = len(pattern)
	indices = []
	for ind, val1 in enumerate(text):
		if text[ind:ind + pat_len] == pattern:
			indices += [ind]
	if not indices:
		return ['Pattern not present in text']
	return indices


if __name__ == '__main__':
	print(naive_str('ATCGCTAGCTAGTAGCT', "TAG"))
