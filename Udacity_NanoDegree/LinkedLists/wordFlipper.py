

def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    flip_word = None
    str = our_string.split()

    for word in str:
        if flip_word:
            flip_word += " "
        for i in range(len(word)-1,-1,-1):
            if flip_word == None:
                flip_word = word[i]
            else:
                flip_word += word[i]


    return flip_word



print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")