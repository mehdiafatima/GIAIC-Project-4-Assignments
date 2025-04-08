
PROMPT = "What do you want? if you want a joke, type 'Joke': "
JOKE = """Here is a joke for you! 
Why do programmers prefer dark mode? 
Because the light attracts bugs!"""
SORRY = "Sorry I only tell jokes"


user_input = input(PROMPT)


if user_input == "Joke":
    print(JOKE)  
else:
    print(SORRY) 
