# Data Science Projects
Repositorio de projetos que estou desenvolvendo




## Pre Requisitos para o Desenvolvimento

O projeto está totalmente encapsulado em containers **Docker**, orquestrados a partir do **docker-compose**, podendo 
então ser executado em qualquer sistema operacional que possua os seguintes recursos instalados:

- Docker
- docker-compose 

---
### Pasta Flask [path](https://github.com/eduardosisti/Data_Science_Projects/tree/main/Flask)
Minima infraestrutura necessário para utilizar um flask app junto com o nginx e uwsgi
<details>
  <summary>Click to expand!</summary>

    1. Faça download com git clone e entre na pasta

    2. Vá para a pasta do Flask
    ```
     cd ./Flask
    ```

    3. Execute o seguinte comando no mesmo diretório que docker-compose.yml para construir os serviços:
    ```bash
    docker-compose up -d --build
    ```
</details>

---

### Pasta flask_dash_nginx_uwsgi [path](https://github.com/eduardosisti/Data_Science_Projects/tree/main/flask_dash_nginx_uwsgi)
Minima infraestrutura necessário para criar um dashboard utilizando o Dash, flask, nginx e uwsgi

<details>
  <summary>Click to expand!</summary>


   1. Faça download com git clone e entre na pasta

   2. Vá para a pasta do Flask
   ```
    cd ./flask_dash_nginx_uwsgi
   ```
   3. Foi adicionado um autenticador para entrar no dash, para alterar o default altere o dockerfile:

   ```
    cd ./flask_dash_nginx_uwsgi/flask_app/Dockerfile

   Parametros default de login e senha:
   login:eduardo
   senha:teste
   ```
   4. Construa seu Dashboard no arquivo:
   ```
   cd ./flask_dash_nginx_uwsgi/flask_app/app_flask/views.py 
   ```
   Se precisar de ajuda vá para:
   [dash_documentation](https://dash.plotly.com/layout)

   5. Execute o seguinte comando no mesmo diretório que docker-compose.yml para construir os serviços:
   ```bash
   docker-compose up -d --build
   ```
   
</details>

---
