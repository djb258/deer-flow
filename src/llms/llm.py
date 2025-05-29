from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_perplexity import ChatPerplexity  # Ensure this is installed

from src.config import load_yaml_config

_llm_cache = {}

def get_llm_by_type(llm_type: str):
    if llm_type == "basic":
        llm_type = "openai"

    if llm_type in _llm_cache:
        return _llm_cache[llm_type]

    conf = load_yaml_config(str((Path(__file__).parent.parent.parent / "conf.yaml").resolve()))

    if llm_type == "openai":
        llm_conf = conf.get("BASIC_MODEL")
        llm = ChatOpenAI(base_url=llm_conf["base_url"], model=llm_conf["model"], api_key=llm_conf["api_key"])

    elif llm_type == "claude":
        llm_conf = conf.get("CLAUDE_MODEL")
        llm = ChatAnthropic(api_key=llm_conf["api_key"], model=llm_conf["model"])

    elif llm_type == "gemini":
        llm_conf = conf.get("GEMINI_MODEL")
        llm = ChatGoogleGenerativeAI(model=llm_conf["model"], google_api_key=llm_conf["api_key"])

    elif llm_type == "perplexity":
    	llm_conf = conf.get("PERPLEXITY_MODEL")
    	llm = ChatOpenAI(
       	    base_url=llm_conf["base_url"],
       	    model=llm_conf["model"],
            api_key=llm_conf["api_key"]
       )


    else:
        raise ValueError(f"Unsupported LLM type: {llm_type}")

    _llm_cache[llm_type] = llm
    return llm
