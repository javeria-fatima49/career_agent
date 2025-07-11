from tools.get_career_roadmap import get_career_roadmap

class SkillAgent:
    def __init__(self, model):
        self.model = model

    def run(self, field: str) -> str:
        gemini_prompt = f"Explain what general skills someone should have to become a {field}."
        gemini_response = self.model.generate_content(gemini_prompt).text.strip()

        tool_skills = get_career_roadmap(field)

        return f"🧠 Gemini says:\n{gemini_response}\n\n🛠 Tool-based Roadmap:\n{tool_skills}"
