# Criando-Rotas-Phyton
Desenvolvimento de API para operações CRUD com linguagem Phyton

CONFIGURAÇÃO DO AMBIENTE

FLASK --
Flask é um pequeno framework web escrito em Python. É classificado como um microframework porque não requer ferramentas ou bibliotecas particulares, mantendo um núcleo simples, porém, extensível.
É fundamental que o Python e o Flask estejam devidamente instalados e configurados para que o programa funcione normalmente, sem problemas.
Para verificar se o programa Python foi instalado corretamente devemos ir no CMD do Windows (Prompt de Comando, Windows PowerShell executado como Administrador). Digite o comando 'py' e dê o ENTER. Caso o programa esteja intalado corretamente, aparecerá detalhes da versão instalada.
Após a verificação, é necessário mudar a localização do Prompt para a pasta onde vamos criar o projeto. (Podemos utilizar o comando 'cd' para navegar entre as pastas e o comando 'mkdir' para criar pastas novas)
Quando estiver na pasta do projeto vamos usar o comando 'py -m venv nome-do-ambiente' (ou 'virtualenv nome-do-ambiente')conseguimos criar um ambiente de forma que as bibliotecas e configurações desse projeto não afetem outros ambientes e outros projetos (o nome-do-ambiente pode ser alterado conforme sua necessidade). Após esse comando será criado dentro da pasta do seu projeto uma outra pasta chamada 'nome-do-ambiente', indicando que seu ambiente está configurado para começar a trabalhar.
Agora com o comando 'nome-do-ambiente\Scripts\activate' vamos ativar o ambiente virtual. Assim, o nome do seu ambiente virtual ficará aparecendo entre parênteses na frente do caminho para pasta no Prompt, indicando que a ativação ocorreu com sucesso.
Para instalar o FLASK devemos digitar o comando 'pip install Flask' e aguardar ser executado.
Criamos então um arquivo nomeado como 'app.py' dentro da pasta do projeto. Em seguida, no Prompt devemos digitar o comando 'set FLASK_APP=app'. Esse comando informa para o FLASK qual arquivo ele deve procurar quando iniciar o servidor.
Por fim devemos dar o comando 'flask run' para iniciar o servidor. Nessa hora será disponibilizado o domínio no qual a aplicação irá rodar (no caso o endereço do localhost e a porta).
# Algumas Bibliotecas necessárias, dependendo do projeto a ser criado:
```bash
pip install mysql-connector-python
pip install flask
pip install python-dotenv

```


# Nesse projeto vamos construir uma API - "API significa 'Interface de Programação de Aplicativos'. É um conjunto de regras que permite que diferentes softwares se comuniquem uns com os outros. É um lugar para disponibilizar recursos e/ou funcionalidades. No caso, vamos fazer um CRUD de livros, iniciando com 3 livros cadastrado e depois utilizando o software POSTMAN para realizar as tarefas de CRIAR, LER, ATUALIZAR E DELETAR, para visualizar o correto funcionamento da aplicação.

# 1. OBJETIVO - Criar um API que disponibiliza a consulta, criação, edição e exclusão de livros (Operações CRUD - CRIATE, READ, UPDATE & DELETE).
# 2. URL BASE - localhost (Disponibilizada no momento da ativação do ambiente)
# 3. ENDPOINTS DO PROJETO- 
    - localhost/livros (GET) - listar todos os livros cadastrados
    - localhost/livros/id (GET) - listar o livro de acordo com o índice
    - localhost/livros (POST) - criar mais um registro de livro
    - localhost/livros/id (PUT) - modificar um registo de livro de acordo com o id
    - localhost/livros (DELETE) - deletar um livro de acordo com o id
# 4. BIBLIOTECAS NECESSÁRIAS NESSE PROJETO
    pip install flask
