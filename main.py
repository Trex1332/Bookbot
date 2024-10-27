with open("books/frankenstein.txt") as f:
    book =f.read()
words = book.split()
letter_counts = {chr(i): 0 for i in range(97, 123)}
for i in book.lower():
    
    if i in letter_counts:
        letter_counts[i]+=1


letter_list = [{'letter': letter, 'count': count} for letter, count in letter_counts.items()]


letter_list.sort(key=lambda item: item['count'], reverse=True)


for entry in letter_list:
    print(f"The '{entry['letter']}' character was found {entry['count']} times")