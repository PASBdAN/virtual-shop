# virtual-shop
 Mock site of a virtual-shop implemented with django and react.

# BACKEND:

## 1. Configurando o ambiente do backend (Django):
 - <backend_dir> = diretório onde ficará os módulos e dependências do projeto
 - Utilizar Ubuntu 20.04 (já com python3.8 + venv instalado)
 - Criar ambiente virtual python numa pasta oculta: python3 -m venv <backend_dir>/.venv
 - Ativar o venv criado: source <backend_dir>/.venv/bin/activate
 - Instalar as libraries necessárias: pip install django djangorestframework django-cors-headers pillow
     - djangorestframework: lib que adiciona os recursos para criação de rotas, viewsets e serializers ao Django.
     - django-cors-headers: lib para criar CORS whitelist de dominios externos para requisição dos recursos do backend
     - pillow: adiciona recursos de processamento de imagens para o interpretador Python
 - Instalar outras libs auxiliares: pip install coverage
     - coverage: lib para relatórios de testes

## 2. Recursos utilizados:
 ### As variáveis de ambiente do django são declaradas no arquivo settings.py, dentre as mais importantes são:
     - BASE_DIR: caminho para a raiz do projeto do django
     - INSTALLED_APPS: Lista dos apps instalados, tais como o rest_framework, corsheaders, etc.
     - MIDDLEWARE: Lista dos middlewares utilizados, tal como o CorsMiddleware
     - DEBUG: Necessário alterar de "True" para "False" antes de entrar em produção.
     - DATABASES: Dicionário com as configuração de acesso ao banco de dados.
     - CORS_ORIGIN_WHITELIST: Lista com os domínios permitidos para requisitar recursos da aplicação django com o CORS.

 ### Helpers:
     - Diretório onde são definidas classes abstratas com atributos e métodos reutilizáveis.
     - Exemplo: TrackingModel, classe que herda models e tem como atributos timestamps para criação e update, e ordenação por data.

 ### Atualizar models e db com migrations do Django:
     - python manage.py makemigrations
     - python manage.py migrate <app_name> zero
     - python manage.py migrate --run-syncdb

 ### Uso de serializers
     - transforma objeto para json.
     - neste projeto foram utilizados os serializers nativos do rest_framework

 ### Uso de views:
     - toda função view precisa retornar uma respota http. 
     - neste projeto foram utilizadas apenas as viewsets nativas do rest_framework

 ### Sobre a feature de segurança CORS:
     - Na prática, quando um recurso em um domínio envia uma requisição para outro recurso em outro domínio, o próprio browser tenta verificar se o domínio destinatário pode aceitar a requisição do remetente.
     - É necessário usar o middleware cors-headers para se ter um handeling de erros causados pela interação de recursos em diferentes domínios. Ex: Um frontend na porta 3000 enviando requisições para o backend na porta 8000 (portas diferentes são considerados domínios diferentes).
     - No nosso caso, iremos adicionar na whitelist do cors do backend (django) o domínio do nosso frontend (react) utilizando a lib django-cors-headers (localhost:3000).
     - Lembrar de declarar o middleware cors-headers no settings.py antes de outros middlewares que podem interferir no funcionamento do middleware.

## 3. Deployment com docker:
 ### Instalar docker:
     - sudo apt update
     - sudo apt upgrade
     - sudo apt install docker.io
 ### Montar imagem, criar e rodar container da imagem (estando dentro do diretório do projeto Django):
     - sudo docker build -t django_app .
     - sudo docker run --name django_app -p 8000:8000 -i -t django_app


# FRONTEND (não concluído):

## 1. Configurando o ambiente do frontend (React):
 - <frontend_dir> = diretório onde ficará os módulos e dependências do projeto
 - Instalar npm (node package manager): sudo apt install npm
 - Criar projeto: npx create-react-app <frontend_dir>
 - Instalar bootstrap e reactstrap: npm install bootstrap@4.6.0 reactstrap@8.9.0 --legacy-peer-deps
 - usando a opção --legacy-peer-deps é necessário para evitar erros de dependência causados por módulos depreciados, dependendo das versões do react, bootstrap e reactstrap.

## OBS:
 - npx: ao contrário do npm, ele procura o pacote na node_modules tanto do projeto quanto do global antes de procurar na internet. É um package manager voltado para gerenciamento de pacotes local/por projeto. Ideal para criar projetos react.



# EXTRAS:

### Mudando a resolução do Ubuntu com Hyper-V:
 - no terminal: sudo nano /etc/default/grub
 - encontre a linha GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
 - mude para: GRUB_CMDLINE_LINUX_DEFAULT="quiet splash video=hyperv_fb:1680x1050"
 - salve e saia
 - no terminal: sudo update-grub
 - restarte a máquina virtual
