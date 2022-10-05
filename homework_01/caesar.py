#!/usr/bin/env python
# coding: utf-8

# In[1]:


def encrypt_caesar(txt,shift):
    from string import ascii_lowercase as norm_low
    from string import ascii_uppercase as norm_up
    new_low = norm_low[shift:] + norm_low[:shift]
    new_up = norm_up[shift:] + norm_up[:shift]
    ces = txt.maketrans(norm_up+norm_low, new_up+new_low)
   
    ciphertext = txt.translate(ces)
    return ciphertext

def decrypt_caesar(txt,shift):
    from string import ascii_lowercase as norm_low
    from string import ascii_uppercase as norm_up
    new_low = norm_low[shift:] + norm_low[:shift]
    new_up = norm_up[shift:] + norm_up[:shift]
    ces_back = txt.maketrans(new_up+new_low, norm_up+norm_low)
   
    plaintext = txt.translate(ces_back)
    return plaintext

