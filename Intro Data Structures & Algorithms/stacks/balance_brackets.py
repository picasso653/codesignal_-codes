def are_brackets_balanced(input_str):
    brackets = set(["(", ")", "[", "]", "{", "}"])
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []

    for character in input_str:
        if character not in brackets:
            # Skipping non-bracket characters
            continue
        if character in open_par:
            stack.append(character)
        elif stack and character == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return len(stack) == 0