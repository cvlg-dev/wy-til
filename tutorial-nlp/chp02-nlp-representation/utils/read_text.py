def read_text(path):
    f = open(path, "r")
    text = list()
    while True:
        line = f.readline()
        if not line: break
        text.append(line)
    f.close()
    return ' '.join(text)