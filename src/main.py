from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY
# from prompts.base_prompt import * 

def main():

    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name="gpt-4o",
        temperature=0.9
        )
    prompt = "Write a poem about python and AI"
    print(llm.invoke(prompt))


if __name__ == "__main__":
    main()
