from langchain.llms import OpenAI


def get_llm(OPENAI_API_KEY):
    
    llm = OpenAI(
        model_name="gpt-4o",
        temperature=0.7
        )
    prompt = "Write a poem about python and AI"
    print(llm(prompt))

