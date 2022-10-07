"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    
    frequencies = {}
    for i in items:
        if str(i) not in frequencies:
            frequencies.update({str(i) : 1})
        else:
            frequencies[i] +=1
            
            
    # Your code goes here
    return frequencies
