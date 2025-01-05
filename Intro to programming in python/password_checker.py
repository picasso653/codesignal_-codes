def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"
    
    criterion_list = []
    
    for password in passwords:
        criterion = {
        "length" : False,
        "digit" : False,
        "uppercase" : False,
        "lowercase" : False,
        "special_char" : False
        }
    
        if len(password) >= 8:
            criterion["length"] = True
        for char in password:
            if char.isdigit():
                criterion["digit"] = True
            elif char.isupper():
                criterion["uppercase"] = True
            elif char.islower():
                criterion["lowercase"] = True
            elif char in special_characters:
                criterion["special_char"] = True
        criterion_list.append(criterion)
    return criterion_list
    # implement this
    pass

passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}