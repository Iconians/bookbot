def main():
  link = "books/frankenstein.txt"
  text = get_text(link)
  num_words = count_words(text)
  num_char = count_char(text)
  sort = sort_dict(num_char)
  print_report(num_words, sort)
  
def get_text(link):
    with open(link) as f:
      file_contents = f.read()
    return file_contents
  
def count_words(str):
  words = str.split()
  return len(words)

def count_char(str):
  dict = {}
  lowerCase = str.lower()
  for char in lowerCase:
    if char in dict:
      dict[char] +=1
    else:
      dict[char] = 1
  return dict

def sort_on(d):
    return d["num"]

def sort_dict(dict):
    list = []
    for char in dict:
        list.append({"char": char, "num": dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list

def print_report(num_words, num_char):
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{num_words} words found in the document")
  for char in num_char:
    if not char["char"].isalpha():
      continue
    print(f"The {char['char']} character was found {char['num']} times")
  print("--- End report ---")

main()




