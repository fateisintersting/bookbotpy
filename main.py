import re 

def main():
   try:
       with open('books/frankenstein.txt') as f:
              file_contents = f.read()
              return frequency_char(file_contents)
   except FileNotFoundError:
       return "not find"



def count_words(text):
     wors = text.split()
     return len(words)


def frequency_char(text):
       words = text.lower()
       word  =  re.sub(r'[^a-zA-Z0-9]',"",words)
       freq = {}
       for x in word:
          if x in freq:
              freq[x] +=1
          else:
               freq[x] = 1
       return freq


re  = main()
print(re)
