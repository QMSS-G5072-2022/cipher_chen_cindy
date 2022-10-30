from cipher_cjc2279 import cipher_cjc2279

def test_cipher_function():
    
    assert cipher_cjc2279.cipher("wallaby", 26) == "WALLABY"

