import pymongo
from datetime import datetime

#1. CONEXÃO (PARTINDO DO MongoDB RODANDO LOCALMENTE NA PORTA PADRÃO)
client = pymongo.MongoClient("mongodb://localhost:27017")

#2. CRIAÇÃO DO BANCO DE DADOS E COLEÇÃO
#NO MongoDB, O BANCO E A COLEÇÃO SÓ SÃO REALMENTE CRIADOS QUANDO O PRIMEIRO DADO É INSERIDO
db = client["projeto_iot"]
colecao = db["leituras_sensores"]

#LIMPA A COLEÇÃO PARA A DEMONSTRAÇÃO RODAR LIMPA TODA VEZ
colecao.drop()

print("**---** INICIO DEMONSTRAÇÃO")
#(CREATE) - INSERÇÃO DE DOCUMENTOS

print("1. Inserindo dados (Flexibilidade de Esquema)...")

#DOCUMENTO 1: LEITURA DO DHT22 (TEMPERATURA E UMIDADE)
doc_dht22 = {
    "sensor": "DHT22",
    "local": "Bancada Lab 1",
    "leitura": {
        "temperatura_c": 24.5,
        "umidade_pct": 60
    },
    "timestamp": datetime.now()
}
colecao.insert_one(doc_dht22)

#DOCUMENTO 2: LEITURA DO LDR (LUMINOSIDADE) - ESTRUTURA INTERNA DIFERENTE
doc_ldr = {
    "sensor": "LDR",
    "local": "Janela",
    "leitura": {
        "luminosidade": "Alta",
        "valor_analogico": 850
    },
    "resistor_pullup_ohms": 10000,
    "timestamp": datetime.now()
}
colecao.insert_one(doc_ldr)

print("    -> OBS: Dois documentos com FORMATOS DIFERENTES são inseridos na mesma coleção")
print()

#(READ) - CONSULTAS BÁSICAS
print("2. Buscando leituras apenas do sensor DHT22:")
query = {"sensor": "DHT22"}
resultados = colecao.find(query)

for res in resultados:
    #O MongoDB ADICIONA AUTOMATICAMENTE UM '_id" ÚNICO
    print(f"    -> Encontrado: {res['leitura']} (ID: {res['_id']})")
print()

#(UPDATE) - ATUALIZAÇÃO
print("3. Atualizando o local do sensor LDR")
filtro_update = {"sensor": "LDR"}
novo_valor = {"$set": {"local": "Área Externa (Calibrado)"}}

colecao.update_one(filtro_update, novo_valor)
doc_atualizado = colecao.find_one(filtro_update)
print(f"   -> Novo local: {doc_atualizado['local']}\n")

#(DELETE) - EXCLUSÃO
print("4. Deletando leituras de temperatura...")
colecao.delete_many({"sensor": "DHT22"})

total_restante = colecao.count_documents({})
print(f"   -> Documentos restantes na coleção: {total_restante}")