
# Create develop env for docker desktop for Windows
1. Install nvidia toolkit to Windows

    See: https://developer.nvidia.com/cuda-toolkit

2. Install docker desktop for Windows
3. Install Ubuntu 22.04.2 LTS distribution on WSL2
4. Update WSL
    ```
    PS > wsl --update
    ```
    reason: update the linux kernel on WSL2
5. Install nvidia toolkit to Ubuntu

    See: https://developer.nvidia.com/cuda-toolkit

6. config docker desktop

    Open: a Docker Desktop for Windows App. And Configuration > Resources > WSL integration
    Change disable: Enable integration with my default WSL distro
    Change enable: Enable integration with additional distros > Ubuntu22.04

7. Setting a container

$ cp docker/.env.dev docker/.env
edit docker/.env
    workspace=your working dir

8. Start Container
    docker-compose -f repository/docker/docker-compose.yml up -d


