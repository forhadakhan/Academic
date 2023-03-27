'''
  (http://rosalind.info/problems/revc/)
  
  Problem
          In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

          The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, 
          then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

  Given: 
          A DNA string s of length at most 1000 base pairs.

  Return: 
          The reverse complement s^c of s.

  Sample Dataset:
          AAAACCCGGT
          
  Sample Output:
          ACCGGGTTTT
'''


def ReverseComplement(DNA):
    translation_tab = DNA.maketrans("AGCTagct", "TCGAtcga")
    complement_dna = DNA.translate(translation_tab)
    reverse = complement_dna[::-1]
    return reverse

print(ReverseComplement(input()))

