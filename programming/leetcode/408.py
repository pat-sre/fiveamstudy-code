import re 

def validWordAbbreviation(word: str, abbr: str) -> bool:
    p1 = 0
    p2 = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # word len is at most 20 so if number n > 20 then its not valid
    while p1 < len(word) or p2 < len(abbr):
        pass
    return True
            
def split_by_numbers(string):
    split = re.findall(r"\D+|\d+", string)
    print(split)


word = "fiveamstudy"
abbr = "5amstudy"
#print(validWordAbbreviation(word, abbr))
print(split_by_numbers(abbr))
word = "kubernetes"
abbr = "k8s"
#print(validWordAbbreviation(word, abbr))
print(split_by_numbers(abbr))
abbr = "5amst15udy"

print(split_by_numbers(abbr))
