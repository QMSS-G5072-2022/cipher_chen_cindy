def cipher(text, shift, encrypt=True):

    """
    Enciphers or deciphers a string based on shifting letters by a fixed number of positions in the alphabet.

    Parameters 
    ----------
    text : str
        A string input.

    shift : int
        An integer for the fixed number of positions to shift the letters.

    encrypt : bool
        Boolean to decide whether or not the function should encrypt your input string.

    Returns
    -------
    str
        The encrypted or decrypted string.

    Examples
    -------
    >>> text = "kangaroo"
    >>> shift = 26
    >>> cipher_cjc2279.cipher(text, shift, encrypt = True)
    "KANGAROO"

    >>> text2 = "bcd"
    >>> shift2 = 1
    >>> cipher_cjc2279.cipher(text2, shift2, encrypt = False)
    "abc"

    """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text