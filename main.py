

def main():
  book_path="books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = count_words(text)
  char_dic = count_character(text)



  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the document")
  print()

  for i in char_dic:
    print(f"The '{i}' character was found {char_dic[i]} times")
  
  print()
  print("--- End report ---")
  

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  words=text.split()
  return len(words)


def count_character(string):
  lowered_string = string.lower()
  letters ="abcdefghijklmnopqrstuvwxyz"
  string_list = []
  letters_list=[]
  string_list.extend(lowered_string)
  letters_list.extend(letters)
  count_dic={}

  for i in letters_list:
    count_dic[i]=0

  for i in string_list:
    if i in count_dic:
      count_dic[i]+=1
  
  return count_dic
  

main()
