'''
  (https://rosalind.info/problems/hamm/)
  
  Problem
         Given two strings s and t of equal length, the Hamming distance between s and t, 
         denoted dH(s,t), is the number of corresponding symbols that differ in s and t. 
  Given: 
          Two DNA strings s and t of equal length
  Return: 
          The Hamming distance dH(s,t).
          
  Sample Dataset:
          GAGCCTACTAACGGGAT
          CATCGTAATGACGGCCT
          
  Sample Output:
          7
'''

def HammingDistance(DNA1, DNA2):
    return int(sum(1 for nucleotide1, nucleotide2 in zip(DNA1, DNA2) if nucleotide1 != nucleotide2))

print(HammingDistance(input(),input())

      
