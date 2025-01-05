def sort_scores(unsorted_scores):
    # implement this
    sorted_scores = sorted(unsorted_scores.items(), key=lambda x : x[1], reverse=True)
    return sorted_scores
    pass

print(sort_scores({'Lora': 97, 'Jason': 99, 'Apple': 64}))
print(sort_scores({'Vanguard': 220, 'Origin': 100, 'Eternal': 150, 'Reaper': 180}))
print(sort_scores({'Charlie': 45, 'Tango': 70, 'Delta': 35}))