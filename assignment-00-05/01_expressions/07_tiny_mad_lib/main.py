def main():
    
    SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"
    
    
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")
    
   
    full_sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"
    
   
    print(full_sentence)


if __name__ == "__main__":
    main()
