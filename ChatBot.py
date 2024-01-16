class HealthChatbot:
    def __init__(self):
        self.user_profile = {"age": None, "weight": None, "preferences": []}

    def start_conversation(self):
        return "Hello! I'm your Health Chatbot. I can help you with personalized diet suggestions. May I know your age?"

    def process_input(self, user_input):
        if "age" not in self.user_profile or self.user_profile["age"] is None:
            self.user_profile["age"] = int(user_input)
            return "Great! Now, can you tell me your weight in kilograms?"
        elif "weight" not in self.user_profile or self.user_profile["weight"] is None:
            self.user_profile["weight"] = float(user_input)
            return "Thanks! What are your dietary preferences? (e.g., vegetarian, gluten-free)"

        # Process dietary preferences
        self.user_profile["preferences"] = user_input.lower().split(',')
        
        # Generate personalized diet suggestions (a simplified example)
        diet_suggestions = self.generate_diet_suggestions()

        return f"Based on your information, here are some personalized diet suggestions: {diet_suggestions}. If you have any specific goals or restrictions, let me know!"

    def generate_diet_suggestions(self):
        # Placeholder for a more sophisticated algorithm based on age, weight, and preferences
        # This could involve consulting with a nutritionist or using machine learning models
        return "Balanced meals with a mix of proteins, carbohydrates, and healthy fats."

# Example usage:
chatbot = HealthChatbot()
print(chatbot.start_conversation())

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chatbot.process_input(user_input)
    print(f"Bot: {response}")
