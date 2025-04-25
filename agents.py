import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def call_openai_agent(system_prompt, user_question):
    response = await client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ],
        temperature=0.7,
        max_tokens=400
    )
    return response.choices[0].message.content.strip()

async def get_legal_response(question):
    return await call_openai_agent(
        "You are LegalBot. Summarize your advice in 5 concise bullet points. Focus on high-impact legal considerations.",
        question)

async def get_finance_response(question):
    return await call_openai_agent(
        "You are FinanceBot. Give 5 sharp, actionable finance bullet points relevant to the question.",
        question)

async def get_tech_response(question):
    return await call_openai_agent(
        "You are TechBot. Offer 5 key technical recommendations in bullet-point format.",
        question)

async def get_marketing_response(question):
    return await call_openai_agent(
        "You are MarketingBot. Provide 5 precise marketing strategy bullet points.",
        question)

async def get_creative_response(question):
    return await call_openai_agent(
        "You are CreativeBot. List 5 imaginative, unconventional ideas in bullet-point format.",
        question)

agent_lookup = {
    "LegalBot": get_legal_response,
    "FinanceBot": get_finance_response,
    "TechBot": get_tech_response,
    "MarketingBot": get_marketing_response,
    "CreativeBot": get_creative_response,
}

async def run_followup(agent_name, followup_question):
    func = agent_lookup.get(agent_name)
    if func:
        return await func(followup_question)
    return "Unknown agent."
