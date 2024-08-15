def respond(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! How can I help you?"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Bot:", respond(user_input))
