Here we are starting out to build a chatbot-platform.
    goals: 
        - operate local LLM: never messed with these.
        - text to speech
        - speech to text
        - an engine to orchestrate 
        - pso bots to provide in game support


Architecture:
    main repo for whole project
        -sub dir for each service w/ .venv untracked through .gitignore.
        -docker-compose.yml and a docker file in each service
            each service will have:
                    - .venv
                    - requriemnts
                    - Dockerfile
            this will allow the docker to be pulled and built on site. 
            for development we will use vscode and the requirments.txt that is generated. 


TODO: add docker files to each service along with the scripts to run said service.

# small comment just for a commit. Project structure feels nice and clean great skeleton for starting

# will be going with postgreSQL 

# things are shapping up nicely time to define some things

Overview of the platform:

        -core-engine     --responsible for orchestration of services

        - stt            -- Speech to Text

        - tts            -- Text to Speech

        - models         -- This will contain many local LLMs

        - pso-bot-client -- a bot to login, move, play, chat, etc

        - api            -- REST or RPC leaning towards rpc for internal

        - frontend/react -- dashboard, cpu , ram, spin up bots

        - chat server    -- muble or discord cordinated with this service

        - data layer     -- going with postgreSQL

chatbot-platform/
├── docker-compose.yml          # The Orchestrator for all containers
├── .dockerignore               # Vital: Ignore local .venv, __pycache__, and .env
├── .gitignore                  # updated to reflect Docker
├── .venv
├── api/
│   ├── Dockerfile              # Service-specific build logic
│   ├── requirements.txt        # FastAPI, SQLAlchemy, etc.
│   ├── main.py
│   └── routers/
├── chat/                       # NEW GATEWAY SERVICE
│   ├── Dockerfile
│   ├── requirements.txt        # Discord.py, etc.
│   ├── discord_gateway.py
│   └── mumble_gateway.py
├── database/                   # SHARED LAYER (Injected into containers via Dockerfile)
│   ├── __init__.py
│   ├── base.py
│   ├── connection.py
│   ├── models.pyv
│   ├── crud/
│   └── migrations/             # Alembic lives here
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── src/
│   └── public/
├── orchestrator/
│   ├── Dockerfile              # Engine-specific build logic
│   ├── requirements.txt        # Websockets, special bot libs
│   ├── app.py
│   ├── engine/
│   └── bots/                   # pso_bot lives here now (moved for context)
└── services/
    ├── stt/
    │   ├── Dockerfile          # Uses a CUDA/PyTorch base image
    │   ├── requirements.txt    # openai-whisper, torch
    │   └── whisper_service.py
    ├── tts/
    │   ├── Dockerfile          # Uses a slim Python base image
    │   ├── requirements.txt    # elevenlabs, requests
    │   └── elevenlabs_service.py
    └──── llm/
            ├── openai/
            │   ├── Dockerfile       # Light: just hits the API
            │   ├── requirements.txt # openai, pydantic
            │   └── service.py
            ├── local_llama/
            │   ├── Dockerfile       # Heavy: GPU/CUDA based
            │   ├── requirements.txt # llama-cpp-python or vllm
            │   └── service.py
            └── custom_model/
                ├── Dockerfile
                ├── requirements.txt
                └── service.py


