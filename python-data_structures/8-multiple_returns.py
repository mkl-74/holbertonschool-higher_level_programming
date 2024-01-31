def multiple_returns(sentence):
    if sentence and sentence[0].isalpha():
        return len(sentence), f"First character: {sentence[0]}"
    else:
        return 0, "Empty string or non-alphabetic first character"
