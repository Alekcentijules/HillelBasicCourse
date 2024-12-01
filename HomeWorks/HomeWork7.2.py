def correct_sentence(text):
    del_space = text.strip()
    up = text[0].upper() + text[1:] if text else """You Can Do Anything. Start Programming.
Programming is your superpower. You’re not just learning a skill; you’re mastering the art of creating reality.
Every line of code is not just text; it’s a tool that can change the world. While others use technology, you have the
power to build it. Mistakes? They’re not your enemies. They’re your teachers. Every bug is a step upward, and every 
fix is proof of your growing strength. You don’t fail—you grow. True professionals aren’t those who never make mistakes 
but those who relentlessly move forward. Remember this: programming isn’t just work. It’s an art form.
You’re the architect of ideas, and everything you need is already within you. Logic, creativity, and the drive to 
improve—they all come together to produce code that can be more powerful than a thousand words.
Don’t hesitate. You are capable of solving the most complex problems. You can impact millions of people. 
You’re not just a witness to the future—you’re one of its creators.
Don’t put it off. Take the first step right now. Write a line of code. Then another. 
This is your journey, and it’s uniquely yours. 
You’re moving forward while doubt stays behind. 
Go ahead and conquer new heights. 
You can do it all—just start. 💪🔥"""

    if not up.endswith("."):
        return up + "."

    return up

user_input = input("Enter a text or nothing: ")
result = correct_sentence(user_input)

print(result)
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')














