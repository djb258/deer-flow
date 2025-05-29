# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

from typing import Any, Dict

from langchain_core.runnables import Runnable
from langchain_core.tools import Tool

from src.tools.search import get_web_search_tool
from src.tools.base_tools import get_all_base_tools
from src.tools.mcp_tools import get_mcp_tools
from src.tools.tavily_search.tavily_search_results_with_images import TavilySearchResultsWithImages

from langchain.agents import Tool as LangchainTool
from langchain.agents import create_openai_functions_agent

# Map logical agent types to actual LLM types
AGENT_LLM_MAP: Dict[str, str] = {
    "coordinator": "openai",
    "planner": "openai",
    "researcher": "perplexity",
    "coder": "gemini",
    "reporter": "basic",
    "podcast_script_writer": "basic",
    "ppt_composer": "basic",
    "prose_writer": "basic",
}

# Create an agent with the appropriate LLM and tools
def create_agent(name: str, mcp_settings: dict = None) -> Runnable:
    agent_config = {
    "name": name,
    "system_message": f"You are a helpful {name} agent.",
}


    llm_type = AGENT_LLM_MAP.get(name, "basic")
    llm = get_llm_by_type(llm_type)

    tools: list[Tool] = []

    # Load base tools
    tools.extend(get_all_base_tools(agent_config))

    # Add Tavily web search tool
    search_tool = LangchainTool.from_function(get_web_search_tool(3))
    tools.append(search_tool)

    # Add MCP tools if any
    if mcp_settings:
        tools.extend(get_mcp_tools(agent_config, mcp_settings))

    return create_openai_functions_agent(llm, tools, agent_config.system_message)

