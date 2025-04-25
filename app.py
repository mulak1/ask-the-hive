import gradio as gr
import asyncio
from agents import (
    get_legal_response,
    get_finance_response,
    get_tech_response,
    get_marketing_response,
    get_creative_response,
    run_followup,
)
from synthesizer import synthesize_responses

agent_names = ["LegalBot", "FinanceBot", "TechBot", "MarketingBot", "CreativeBot"]

# Core logic
async def gather_responses(user_question):
    results = await asyncio.gather(
        get_legal_response(user_question),
        get_finance_response(user_question),
        get_tech_response(user_question),
        get_marketing_response(user_question),
        get_creative_response(user_question),
    )
    return dict(zip(agent_names, results))

def ask_the_hive(user_question):
    try:
        responses = asyncio.run(gather_responses(user_question))
        summary = synthesize_responses(user_question, responses)
    except Exception as e:
        print("❌ Error:", e)
        return ["Error"] * (len(agent_names) + 1)

    outputs = [responses[agent] for agent in agent_names]
    outputs.append(f"### 🧠 Executive Summary\n{summary}")
    return outputs

def handle_followup(agent_name, followup_question):
    try:
        response = asyncio.run(run_followup(agent_name, followup_question))
        return response
    except Exception as e:
        print(f"❌ Error in {agent_name} follow-up:", e)
        return "Error during follow-up."

# Build UI
with gr.Blocks() as demo:
    gr.Markdown("""
    # 🐝 Ask the Hive
    Enter a complex, multi-domain question to receive input from AI domain experts and a synthesized summary.
    """)

    question_input = gr.Textbox(label="Your Question", placeholder="e.g., I want to start a subscription box company in California.")
    ask_btn = gr.Button("Ask the Hive")

    agent_outputs = []
    follow_inputs = []
    follow_buttons = []

    for agent in agent_names:
        gr.Markdown(f"## 🤖 {agent}")
        response_md = gr.Markdown()
        follow_input = gr.Textbox(placeholder=f"Follow-up for {agent}")
        follow_button = gr.Button(f"Send to {agent}")
        follow_button.click(
            fn=lambda followup_question, agent=agent: handle_followup(agent, followup_question),
            inputs=follow_input,
            outputs=response_md
        )
        agent_outputs.append(response_md)
        follow_inputs.append(follow_input)
        follow_buttons.append(follow_button)

    summary_output = gr.Markdown(label="Executive Summary")

    ask_btn.click(ask_the_hive, inputs=question_input, outputs=agent_outputs + [summary_output])

if __name__ == "__main__":
    print("🚀 Launching Hive with fallback UI...")
    demo.launch()
