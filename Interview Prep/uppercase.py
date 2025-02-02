def process_text(text):
    new_text = ""
    for char in text:
        if char.isalpha():
            new_text += char.upper()
        else:
            continue
    print(f"Processed Text: {new_text}")

process_text("Happy Coding, Friends!")