def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        user_input_2=input("You: ")
        if user_input_2=="good" or user_input_2=="great" or user_input_2=="fine":
            return "That's awesome!"
    elif "what is your name" in user_input:
        return "I'm a simple rule-based chatbot known as Milo-AI, created by Priyansh."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "what can you do" in user_input:
        return "I can chat with you and answer simple questions based on my rules."
    elif "who built you" in user_input:
        return "I was built by Priyansh."
    elif "when were you created" in user_input:
        return "I was created in 2024 by Priyansh."
    elif "what is your favourite colour" in user_input:
        return "I don't have preferences, but I know many people like blue."
    elif "ok" in user_input or "hmm" in user_input or "nice" in user_input:
        return "Anything else you want to know?"
    elif "what today's date" in user_input or "what's today's date" in user_input:
        from datetime import date
        today = date.today()
        formated_date = today.strftime('%B %d, %Y')
        return formated_date
    elif "what today's day" in user_input or "what's today's day" in user_input or "what day it is" in user_input:
        from datetime import date
        today = date.today()
        if today.weekday() == 0:
            return "Today is Monday"
        elif today.weekday() == 1:
            return "Today is Tuesday"
        elif today.weekday() == 2:
            return "Today is Wednesday"
        elif today.weekday() == 3:
            return "Today is Thursday"
        elif today.weekday() == 4:
            return "Today is Friday"
        elif today.weekday() == 5:
            return "Today is Saturday"
        else:
            return "Today is Sunday"
        
    elif 'what is' in user_input:
        ev=user_input[7:]
        return eval(ev)
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

#Main
print("Chatbot: Hello! How can I assist you today")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    if "bye" in user_input or "goodbye" in user_input:
        break