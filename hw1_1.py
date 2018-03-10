def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    if not word:
        return False

    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            if len(word[i:])>=6:
                if word[i+2:i+6:2]==word[i+3:i+7:2]:
                    return True   
    return False
            

word='0012bbaavv'
print(trifeca(word))
