# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
import yaml
import re
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file before anything else
load_dotenv()

def substitute_env_variables(obj):
    """
    Recursively substitute environment variables in a nested dictionary
    formatted as ${VAR_NAME}
    """
    if isinstance(obj, dict):
        return {k: substitute_env_variables(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [substitute_env_variables(i) for i in obj]
    elif isinstance(obj, str):
        pattern = re.compile(r"\$\{(\w+)\}")
        match = pattern.findall(obj)
        for var in match:
            env_val = os.getenv(var)
            if env_val:
                obj = obj.replace(f"${{{var}}}", env_val)
        return obj
    else:
        return obj

def load_yaml_config(path: str) -> dict:
    """
    Load YAML config and substitute any ${ENV_VAR} with actual environment variables
    """
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return substitute_env_variables(config)

if __name__ == "__main__":
    config_path = Path(__file__).parent.parent / "conf.yaml"
    parsed = load_yaml_config(str(config_path.resolve()))
    print(parsed)

