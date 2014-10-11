# Return counts of top 10 repeated words in a file
def top10(file_path):
    ''' file --> list of top 10 words'''
    file_name = open(file_path, 'r')
    content = file_name.read()
    content = content.lower().replace('.', '').replace(',', '')
    words = content.split()
    word_dict = {}
    for dummy in words:
        if dummy in word_dict.keys():
            word_dict[dummy] += 1
        else:
            word_dict[dummy] = 1
    tally = sorted(word_dict, key=word_dict.__getitem__)
    return word_dict
    # return list(reversed(tally[-10:]))
