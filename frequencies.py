"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    
    frequencies = {}
    for i in items:
        if i not in frequencies:
            frequencies.update({i : 1})
        else:
            frequencies[i] +=1
            
            
    # Your code goes here
    return frequencies
