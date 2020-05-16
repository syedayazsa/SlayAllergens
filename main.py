#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:03:31 2019

@author: ayaz
"""

print("Welcome to SlayAllergens! Your Diet Recommendation Helper!")


inp = int(input("""Press:\n
      1.Sign In\n
      2.Sign Up\n"""))
if inp == 2:
    import signup
if inp == 1:
    import signin
