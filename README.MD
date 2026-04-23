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