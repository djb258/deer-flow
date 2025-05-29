from src.llms.llm import get_llm_by_type

print(">>> Testing OpenAI Basic:")
print(get_llm_by_type("basic").invoke("Say hi as OpenAI basic."))

print(">>> Testing Claude:")
print(get_llm_by_type("claude").invoke("Say hi as Claude."))

print(">>> Testing Gemini:")
print(get_llm_by_type("gemini").invoke("Say hi as Gemini."))
