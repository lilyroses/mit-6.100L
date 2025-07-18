def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    frequencies = {}
    if isinstance(input_iterable, str):
        for char in input_iterable:
            if char not in frequencies:
                frequencies[char] = 1
            else:
                frequencies[char] += 1
    elif isinstance(input_iterable, list):
        for item in input_iterable:
            if item not in frequencies:
                frequencies[item] = 1
            else:
                frequencies[item] += 1
    return frequencies


if __name__ == "__main__":
    print(get_frequencies(["h", "e", "l", "l", "o"]))
    print(get_frequencies(["hello", "world", "hello"]))