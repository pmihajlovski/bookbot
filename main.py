import string
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    split = split_text(text)
    c = count_letters(text)
    count_letters_sorted = sorted(c.items(), key = lambda x:x[1], reverse=True)
    print(f"--- Begin report of {book_path}---")
    print(f"{split} word found in the document")
    for i in count_letters_sorted:
        x,y = i
        print(f"The {x} character was found {y} times")
    
    
    





def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def split_text(testo):
    list_words = testo.split()
    return len(list_words)

def count_letters(testo):
    c = {}
    lowered_text = testo.lower()
    for i in lowered_text:
        if i in c:
            c[i] += 1 
        elif i in list(string.ascii_lowercase):
            c[i] = 1
    return c


        
        

    
    


main()