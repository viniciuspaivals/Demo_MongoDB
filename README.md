# Demo_MongoDB
## Pré-requisitos

Antes de executar o script, você precisará ter o seguinte instalado em sua máquina:

*   **Python 3.7+**
*   **MongoDB Community Server** rodando localmente na porta padrão (`27017`). 
    *   *Alternativa:* Caso use o MongoDB Atlas (nuvem), você precisará alterar a string de conexão no arquivo `demo_mongodb.py`.

## Instalação e Configuração

1. **Clone o repositório (ou acesse a pasta do script):**
   ```bash
   cd caminho/para/a/pasta/do/projeto
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   * **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   * **Windows:**
     ```bash
     venv\Scripts\activate
     ```

4. **Instale a dependência do driver do MongoDB:**
   ```bash
   pip install pymongo
   ```

## Como Executar

Com o serviço do MongoDB em execução no background, rode o script principal:

```bash
python demo_mongodb.py
```

## O que o script faz?

O script executa um fluxo completo de **CRUD** (Create, Read, Update, Delete) de forma didática e imprimindo os resultados no terminal:

1. **Conexão:** Conecta-se ao banco local e limpa a coleção `leituras_sensores` para garantir uma demonstração limpa.
2. **Create (Inserção Flexível):** Insere dois documentos na mesma coleção. O primeiro simula um sensor de temperatura (DHT22) e o segundo simula um sensor de luz (LDR). **Note que os campos e estruturas internas são diferentes**, demonstrando a natureza *schema-less* do NoSQL.
3. **Read (Busca):** Realiza uma consulta simples para buscar apenas os registros gerados pelo sensor `DHT22`.
4. **Update (Atualização):** Encontra o documento do sensor `LDR` e atualiza o seu campo `local` usando o operador `$set`.
5. **Delete (Exclusão):** Deleta permanentemente as leituras de temperatura (`DHT22`) do banco de dados e conta os documentos restantes.

---
