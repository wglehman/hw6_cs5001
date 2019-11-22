def get_wordlist():
    ''' Function get-wordlist
        Params: nothoing
        Returns: a list of strings
        Does: retrieves a list of dictionary words from the built-in
              unix dictionary, which has been copied over.
    '''
    try:
        infile = open('wordlist.txt', 'r')
        lines = infile.readlines()
        infile.close()
    except OSError:
        return []

    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
        lines[i] = lines[i].upper()
        if ' ' in lines[i]:
            lines[i] = lines[i].strip(' ')
    return lines
