#!/bin/bash

curl -X POST http://127.0.0.1:8000/fire \
  -H "Content-Type: application/json" \
  -d '{
    "quote_input": "What is a good healthcare quote for Acme Inc?",
    "source": "bash_local"
  }'

