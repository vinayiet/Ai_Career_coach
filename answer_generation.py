import os 
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Initialize the LLM from Groq
codellm = ChatGroq(
    model_name="llama3-8b-8192", 
    temperature=0.3,
    max_tokens=1024,
    timeout=60,
    max_retries=2
)

def generate_answer(retrieved_context, question):
    # Custom prompt template for a Career Coach AI
    prompt_template = prompt_template = """
You are an intelligent AI Career Coach for tech aspirants, especially those in Computer Science and related fields.

Resume Context:
{context}

User Question:
{question}

Now, based on the above resume and question, follow these steps:

1. **Identify the Target Role**:
   - Determine the most likely or desired career path (e.g., Machine Learning Engineer, Backend Developer, Full Stack Developer, etc.).

2. **Analyze the Resume**:
   - Review Skills, Projects, and Experience.
   - Highlight strengths, identify missing or outdated tech, and suggest improvements.

3. **Provide Career Guidance**:
   - Recommend the most suitable field(s) based on skills and current trends.
   - Suggest specific project ideas to build or improve.
   - List most-asked interview questions for the role.
   - Recommend trusted resources to stay updated (e.g., GitHub trending, Papers with Code, newsletters).

4. **Generate a Roadmap**:
   - Provide a learning path like roadmap.sh: beginner → intermediate → advanced.
   - Structure the path in steps with technologies/tools to learn.

5. **Respond Naturally**:
   - Always answer clearly, with encouragement and actionable steps.
"""


    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    # Format the prompt
    formatted_prompt = prompt.format(context=retrieved_context, question=question)

    # Invoke LLM with the prompt
    answer = codellm.invoke(formatted_prompt)
    print("Generated Answer:\n", answer.content)
    return answer.content
