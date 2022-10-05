#!/usr/bin/env python
# coding: utf-8

# In[102]:


def encrypt_vigenere(text, key):
    from string import ascii_lowercase as norm_low
    from string import ascii_uppercase as norm_up
    key = key.lower()
    ciphertext = ""
    if len(key)<len(text):
        plus=key
        while len(key)<len(text):
            key=key+plus

    for i in range(len(text)):
        t = text[i] 
        k = key[i] 
        if t in norm_low:
            num = norm_low.find(t)+norm_low.find(k)
            if num>len(norm_low)-1:
                num = num-len(norm_low)
            ciphertext = ciphertext+norm_low[num]
        elif t in norm_up:
            num = norm_up.find(t)+norm_low.find(k)
            if num>len(norm_up)-1:
                num = num-len(norm_up)            
            ciphertext = ciphertext+norm_up[num]
        else:
            ciphertext = ciphertext + t
    return ciphertext

def decrypt_vigenere(text, key):
    from string import ascii_lowercase as norm_low
    from string import ascii_uppercase as norm_up
    key = key.lower()
    plaintext = ""
    
    
    if len(key)<len(text):
        plus=key
        while len(key)<len(text):
            key=key+plus

    for i in range(len(text)):
        t = text[i] 
        k = key[i] 
        if t in norm_low:
            num = norm_low.find(t)-norm_low.find(k)
            plaintext = plaintext+norm_low[num]
        elif t in norm_up:
            num = norm_up.find(t)-norm_low.find(k)            
            plaintext = plaintext+norm_up[num]
        else:
            plaintext = plaintext + t
    
    return plaintext





