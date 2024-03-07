def cut(s):
    if type(s) != type("hf"):
        raise TypeError
    s=s.replace('\n', ' ')
    s=s.strip()
    while s.count("  ")>0:
        s=s.replace('  ', ' ')
    return s.split(' ')

if __name__=="__main__":
    print("What in the holy McFuck is this")
