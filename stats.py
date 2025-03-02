
def num_words(text: str) -> int:
    text = text.split()
    return len(text)

def num_chars(text: str) -> dict:

    chars = {}
    for char in text:
        key = char.lower()
        if key in chars:
            chars[key] += 1
        
        else:
            chars[key] = 1
            
    return chars

