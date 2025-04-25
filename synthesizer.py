import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def synthesize_responses(user_question, agent_responses):
    panel_summary = "\n\n".join([f"{agent}: {response}" for agent, response in agent_responses.items()])

    synthesis_prompt = (
        "You are SynthesisBot. Based on the expert responses below, return:\n"
        "1. A single executive summary sentence.\n"
        "2. Followed by exactly 5 key bullet points — one per expert (LegalBot, FinanceBot, TechBot, MarketingBot, CreativeBot).\n\n"
        f"User Question: {user_question}\n\n"
        f"Expert Responses:\n{panel_summary}"
    )

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You synthesize expert inputs into sharp, executive-style briefings."},
            {"role": "user", "content": synthesis_prompt}
        ],
        temperature=0.5,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()
