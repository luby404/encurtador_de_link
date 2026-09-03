# Encurtador de Links

Projeto simples de encurtador de links em Python.

Este repositório contém a lógica mínima para cadastrar URLs originas e gerar links encurtados que redirecionam para o destino.

**Principais componentes**
- API / lógica: diretório `app`
- Core da aplicação (servidor e banco): `app/core`
- Arquivo de banco embarcado: `banco.db`

Estrutura do projeto (resumida):

```
.
├── app
│   ├── contollers.py
│   ├── core
│   │   ├── database.py
│   │   ├── schema.py
│   │   └── server.py
│   ├── __init__.py
│   ├── models.py
│   ├── utils.py
│   └── views.py
├── banco.db
├── pyproject.toml
├── README.md
└── uv.lock
```

Requisitos
- Python 3.10+ (recomendado)
- Dependências listadas em `pyproject.toml` (use `poetry install` ou instale manualmente com `pip`)

Instalação rápida

1. Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Instale dependências (se você usa Poetry):

```bash
poetry install
```

Ou instale com pip caso não use Poetry (se houver `requirements.txt`):

```bash
python -m pip install -r requirements.txt
```

Executando localmente

- Inicie o servidor (verifique `app/core/server.py` para detalhes de execução e variáveis de ambiente):

```bash
python -m app.core.server
```

- O servidor expõe endpoints para criar um link encurtado e para redirecionamento. Ajuste a porta/host conforme o código em `app/core/server.py`.

Banco de dados
- O projeto já contém um arquivo SQLite `banco.db` para desenvolvimento local. A inicialização do esquema é feita em `app/core/schema.py` / `app/core/database.py`.

Exemplos de uso (genéricos)

- Criar um link encurtado (exemplo usando curl):

```bash
curl -X POST http://localhost:8000/shorten -d '{"url":"https://example.com"}' -H "Content-Type: application/json"
```

- Acessar um link encurtado:

```bash
curl -i http://localhost:8000/<codigo_encurtado>
```

Desenvolvimento
- Verifique e rode os módulos em `app/` para entender as rotas e a lógica.
- Arquivos de interesse: `app/contollers.py`, `app/models.py`, `app/views.py`, `app/utils.py`.

Contribuição
- Abra uma issue descrevendo o que deseja melhorar.
- Envie PRs com mudanças pequenas e testes quando possível.

Problemas ou dúvidas
- Consulte os arquivos em `app/core` para detalhes de execução ou me pergunte se quiser que eu escreva instruções mais precisas de execução (por exemplo, comandos exatos dependendo do framework usado no `server.py`).


