# Data Science Projects
Repositorio de projetos que estou desenvolvendo




## Pre Requisitos para o Desenvolvimento

O projeto está totalmente encapsulado em containers **Docker**, orquestrados a partir do **docker-compose**, podendo 
então ser executado em qualquer sistema operacional que possua os seguintes recursos instalados:

- Docker
- docker-compose 


### Pasta Flask [path](https://github.com/eduardosisti/Data_Science_Projects/tree/main/Flask)
Minima infraestrutura necessário para utilizar um flask app junto com o nginx e uwsgi

1. Faça download com git clone e entre na pasta

2. Vá para a pasta do Flask
```
 cd ./Flask
```

3. Execute o seguinte comando no mesmo diretório que docker-compose.yml para construir os serviços:
```bash
docker-compose up -d --build
```

