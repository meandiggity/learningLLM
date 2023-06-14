#!/bin/bash

curl -X POST 'http://127.0.0.1:8000' \
    -H 'Content-Type: application/json' \
    -d '{"message": "- tokenizer = AutoTokenizer.from_pretrained(\"example/ModelName\")\n+ tokenizer = AutoTokenizer.from_pretrained(\"mamiksik/T5-commit-message-generation\")"}'

