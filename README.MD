Here we are starting out. to build a chatbot-platfrom.
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

chatbot-platform/
│
├── api/
│   ├── main.py
│   ├── routers/
│   │   ├── bots.py
│   │   ├── workflows.py
│   │   ├── pipeline.py
│   │   └── __init__.py   <-- yes
│   ├── __init__.py       <-- yes
│   └── .venv/
│
├── orchestrator/
│   ├── app.py
│   ├── engine/
│   │   ├── orchestrator.py
│   │   ├── pipeline.py
│   │   ├── bot_manager.py
│   │   └── __init__.py   <-- yes
│   ├── __init__.py       <-- yes
│   └── .venv/
│
├── bots/
│   ├── pso_bot.py
│   ├── __init__.py       <-- optional unless importing
│   └── .venv/
│
├── services/
│   ├── stt/
│   │   ├── whisper_service.py
│   │   └── __init__.py   <-- yes
│   ├── tts/
│   │   ├── elevenlabs_service.py
│   │   └── __init__.py   <-- yes
│   ├── llm/
│   │   ├── openai_service.py
│   │   └── __init__.py   <-- yes
│   └── __init__.py       <-- yes
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json       
│
│
└── chat/                     <-- NEW
    ├── discord_gateway.py    <-- Discord bot interface
    ├── mumble_gateway.py     <-- Mumble voice interface
    ├── __init__.py
    └── .venv/