def count_words(text):
    return len(text.split())

def count_chars(text):
    count = {}
    for char in text:
        count[char.lower()] = count.get(char.lower(), 0) + 1
    return count

def sort_chars_count(count):
    result = []
    for char, count in count.items():
        result.append({
            "char": char,
            "num": count
        })
    def sort_on(items):
        return items["num"]
    result.sort(reverse=True, key=sort_on)
    return result