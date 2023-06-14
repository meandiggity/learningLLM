#!/bin/bash
(
    cd $(dirname $0)
    uvicorn daemon:app --reload
)

