class CareerAgent:
    def __init__(self, model):
        self.model = model
        self.introduced = False

    def run(self, user_input: str) -> str:
        if not self.introduced:
            self.introduced = True
            return (
                "👋 Hi! I'm your Career Mentor Agent.\n"
                "🧠 I specialize in helping you explore career paths based on your interests.\n"
                "💼 Tell me what you love doing, your goals, or skills — and I’ll guide you!"
            )
        if user_input.strip().lower() in ["thank you", "thanks", "shukriya"]:
            return "You're welcome! 😊 Let me know if you want more help!"

        if len(user_input.strip()) < 10:
            return "❗ Please share more details — like your passion, subjects you love, or dream job."

        prompt = (
            "You are a professional career advisor. Based on the user's interest, recommend ONE best-fit career.\n"
            "Only choose from: Web Developer, Data Scientist, AI Engineer, UX Designer, Marketing Specialist.\n"
            "Clearly explain:\n"
            "1. Why it's a good fit\n"
            "2. What skills are needed\n"
            "3. How to get started\n\n"
            f"User: {user_input}"
        )

        response = self.model.generate_content(prompt)
        return response.text.strip()
