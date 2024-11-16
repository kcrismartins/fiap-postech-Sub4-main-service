# fiap-postech-Sub4-main-service
# Main Service

O **Main Service** é o serviço principal de gerenciamento de veículos para venda. Ele é responsável por:
- Cadastro de novos veículos.
- Edição de informações de veículos existentes.
- Integração com outros serviços por meio de webhooks.

Este microserviço é desenvolvido em **FastAPI**, utiliza **PostgreSQL** como banco de dados e é preparado para ser executado em containers **Docker**.

---

## 🚀 Tecnologias

Este projeto utiliza as seguintes tecnologias e bibliotecas:

- **FastAPI**: Framework para criação de APIs em Python.
- **SQLAlchemy**: ORM (Object-Relational Mapping) para manipulação do banco de dados.
- **PostgreSQL**: Banco de dados relacional.
- **Docker**: Para containerização do ambiente.
- **Pytest**: Framework de testes para Python.
- **Coverage**: Ferramenta para medir cobertura de testes.

---

## 📦 Estrutura do Projeto

```plaintext
main-service/
│
├── src/
│   ├── main.py                # Arquivo principal que inicia o serviço
│   ├── models.py              # Modelos do banco de dados
│   ├── schemas.py             # Esquemas Pydantic para validação
│   ├── database.py            # Configuração e conexão com o banco de dados
│   ├── services/              # Contém a lógica de negócios
│   │   ├── create_edit.py     # Funções para criar e editar veículos
│   │   ├── webhook.py         # Integração com webhooks externos
│   └── tests/                 # Testes automatizados
│       ├── test_create_edit.py # Testes de criação e edição de veículos
│       ├── test_webhook.py    # Testes de integração com webhooks
│
├── requirements.txt           # Lista de dependências do projeto
├── Dockerfile                 # Configuração do container Docker
├── docker-compose.yml         # Configuração de ambiente com Docker Compose
└── README.md                  # Documentação do projeto
```

## 🛠️ Configuração e Execução

### Pré-requisitos
- Python 3.9+
- Docker e Docker Compose
- PostgreSQL

### Como Rodar o Projeto Localmente

  1. Clone o repositório:
     ```bash
     git clone <https://github.com/kcrismartins/fiap-postech-Sub4-main-service.git>
     cd main-service
     
 2. Instale as dependências:
     ```bash
     pip install -r requirements.txt
     
 3. Configure o banco de dados:
    - Edite o arquivo src/database.py para configurar as credenciais de acesso ao banco de dados.
      
 4. Execute o serviço:
    ```bash
    uvicorn src.main:app --reload


###  Usando Docker 🐳

1. Configure o .env com as variáveis necessárias (caso aplicável).
2. Inicie o ambiente com Docker Compose:
   ```bash
   docker-compose up --build

---

## 🧪 Testes Automatizados

O projeto inclui uma suíte de testes automatizados para validar a lógica e a integração dos endpoints.

1. Instale as dependências de teste:
   ```bash
   pip install pytest pytest-asyncio coverage

2. Execute os testes:
   ```bash
   pytest

3. Gere um relatório de cobertura:
   ```bash
   coverage run -m pytest
   coverage report -m

4. Opcional: Gere um relatório em HTML:
   ```bash
   coverage html
   
O relatório estará disponível no diretório htmlcov/.

---

## 📂 Endpoints Principais

### Cadastro de Veículos

- POST /vehicles
- Descrição: Cadastra um novo veículo.
- Body:
    ```json
    {
    "brand": "Ford",
    "model": "Fiesta",
    "year": 2022,
    "color": "Blue",
    "price": 15000
    }
    ```
- Resposta:
    ```json
    {
  "message": "Vehicle created successfully",
  "vehicle_id": 1
  }
  ```
    

  ### Edição de Veículos

- PUT /vehicles/{vehicle_id}
- Descrição: Atualiza as informações de um veículo existente.
- Body:
    ```json
    {
  "price": 14000,
  "color": "Red"
  }
   ```
- Resposta:
    ```json
   {
  "message": "Vehicle updated successfully"
  }
  ```

 ### Webhook

- POST /webhook
- Descrição: Processa notificações de terceiros (exemplo: pagamentos).
- Body: Depende da integração configurada.

---

## 📝 Licença

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

---

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para a sua feature (git checkout -b minha-feature).
3. Commit suas mudanças (git commit -m 'Adicionei uma nova feature').
4. Submeta sua branch (git push origin minha-feature).
5. Abra um Pull Request.
   ```javascript
   Esse `README.md` fornece uma visão geral completa do repositório, com explicações detalhadas sobre configuração, execução e testes. Se precisar de mais ajustes ou algo adicional, é só avisar!
