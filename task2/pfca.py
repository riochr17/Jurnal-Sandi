
bestQuadgram = [ "TION", "OTHE", "THEM",
"NTHE", "TTHE", "RTHE",
"THER", "DTHE", "THEP",
"THAT", "INGT", "FROM",
"OFTH", "ETHE", "THIS",
"FTHE", "SAND", "TING",
"THES", "STHE", "THEI",
"WITH", "HERE", "NGTH",
"INTH", "THEC", "IONS",
"ATIO", "MENT", "ANDT"]

print bestQuadgram

'''
1. Generate a random key, called the 'parent', decipher the ciphertext 
    using this key. 
2. Rate the fitness of the deciphered text, store the result.
3. for(TEMP = 10;TEMP >= 0; TEMP = TEMP - STEP) 
      for (count = 50,000; count>0; count--)
         Change the parent key slightly (e.g. swap two characters in the 
           key at random) to get child key, 
         Measure the fitness of the deciphered text using the child key
         set dF = (fitness of child - fitness of parent)
         If dF > 0 (fitness of child is higher than parent key), 
             set parent = child
         If dF < 0 (fitness of child is worse than parent), 
             set parent = child with probability e^(dF/T). 
'''

