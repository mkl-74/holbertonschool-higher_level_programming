#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        if 'a' <= sentence[0].lower() <= 'z':
            return len(sentence), f"First character: {sentence[0]}"
        else:
            return len(sentence), "Non-alphabetic first character"
    else:
        return 0, "Empty string"