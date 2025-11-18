import random
import re

# ---- same logic as before ----
greetings = ["hello", "hi", "hey", "good morning", "good evening", "namaste"]
greeting_responses = [
    "Hello! How can I help you today?",
    "Hi there! What can I assist you with?",
    "Hey! How can I make your telecom experience better?"
]

responses = {
    r"(recharge|top[- ]?up)": [
        "You can recharge your number using our official app or website.",
        "We have special recharge offers! Visit: www.telecomexample.com/recharge",
        "Would you like to know the best recharge plans available?"
    ],
    r"(data|internet|4g|5g|balance)": [
        "You can check your data balance by dialing *121#.",
        "To get more data, visit: www.telecomexample.com/datapacks",
        "Would you like me to list our current data offers?"
    ],
    r"(network|signal|coverage|no service)": [
        "I'm sorry to hear that you're facing network issues.",
        "Please try restarting your phone or switching to airplane mode for a few seconds.",
        "Can you share your area pincode so we can check coverage?"
    ],
    r"(plan|offer|pack|tariff)": [
        "We offer unlimited calling and data plans starting at ₹199/month.",
        "Visit www.telecomexample.com/plans for the latest offers.",
        "Would you like prepaid or postpaid plan details?"
    ],
    r"(complaint|issue|problem|report)": [
        "I'm sorry for the inconvenience. You can file a complaint by calling 198 (toll-free).",
        "Can you describe the issue briefly so I can help you better?",
        "We’ve noted your concern. Our support team will get back to you shortly."
    ],
    r"(port|change|sim|number)": [
        "You can port your number easily. Just send an SMS ‘PORT <your_number>’ to 1900.",
        "Visit your nearest telecom store with your ID proof to change SIM.",
        "Would you like details on the porting process?"
    ],
    r"(bye|exit|quit|thank)": [
        "Thank you for contacting us! Have a great day!",
        "Goodbye! We're here whenever you need help.",
        "Thanks for chatting! Stay connected with us."
    ]
}

def get_response(user_input):
    """Return a chatbot response based on user message."""
    user_input = user_input.lower().strip()

    # Greetings
    if any(word in user_input for word in greetings):
        return random.choice(greeting_responses)

    # Keyword match
    for pattern, reply_list in responses.items():
        if re.search(pattern, user_input):
            return random.choice(reply_list)

    # Fallback
    return "I'm not sure I understand. Could you please rephrase that?"
