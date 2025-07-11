from tools.get_job_roles import get_job_roles

class JobAgent:
    def __init__(self, model):
        self.model = model

    def run(self, field: str) -> str:
        gemini_prompt = f"Tell me what kinds of companies usually hire {field}s."
        gemini_response = self.model.generate_content(gemini_prompt).text.strip()

        tool_jobs = get_job_roles(field)

        return f"📈 Gemini Insight:\n{gemini_response}\n\n📋 Tool-based Jobs:\n{tool_jobs}"
