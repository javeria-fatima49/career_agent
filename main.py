import chainlit as cl
import google.generativeai as genai
# import os
# from dotenv import load_dotenv
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent


# genai.configure(api_key="YOUR_GEMINI_API_KEY")
# model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-pro"

# load_dotenv()

# 🔐 Get key from environment variable
# api_key = os.getenv("GEMINI_API_KEY")


genai.configure(api_key="AIzaSyCa4pK61Ldy8hIj4L5H5AKo5moMMwd4ju4")


model = genai.GenerativeModel("gemini-1.5-flash")  

career_agent = CareerAgent(model)
skill_agent = SkillAgent(model)
job_agent = JobAgent(model)

@cl.on_chat_start
async def start():
    intro = career_agent.run("")
    await cl.Message(content=intro).send()

@cl.on_message
async def handle_message(msg: cl.Message):
    user_input = msg.content

    career_response = career_agent.run(user_input)
    await cl.Message(content=f"🎓 **CareerAgent:**\n{career_response}").send()

    detected_field = None
    for field in ["Web Developer", "Data Scientist", "AI Engineer", "UX Designer", "Marketing Specialist"]:
        if field.lower() in career_response.lower():
            detected_field = field
            break

    if detected_field:
        skill_response = skill_agent.run(detected_field)
        await cl.Message(content=f"🧠 **SkillAgent for {detected_field}:**\n{skill_response}").send()

        job_response = job_agent.run(detected_field)
        await cl.Message(content=f"💼 **JobAgent for {detected_field}:**\n{job_response}").send()
    else:
        await cl.Message(content="❌ Sorry, I couldn't detect a clear career field. Try being more specific.").send()
