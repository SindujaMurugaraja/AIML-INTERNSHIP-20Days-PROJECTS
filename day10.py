from langchain_core.prompts import PromptTemplate

# Zero Shot
zero_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms."
)

print("===== ZERO SHOT =====")
print(zero_prompt.format(topic="Machine Learning"))


# Few Shot
few_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
Example 1:
Question: What is AI?
Answer: AI is the simulation of human intelligence by machines.

Example 2:
Question: What is ML?
Answer: Machine Learning is a subset of AI that learns from data.

Question: {question}
Answer:
"""
)

print("\n===== FEW SHOT =====")
print(few_prompt.format(
    question="What is Deep Learning?"
))


# Chain of Thought
cot_prompt = PromptTemplate(
    input_variables=["problem"],
    template="""
Solve the problem step by step.

Problem:
{problem}

Show your reasoning before the final answer.
"""
)

print("\n===== CHAIN OF THOUGHT =====")
print(cot_prompt.format(
    problem="A train travels 120 km in 2 hours. Find the speed."
))