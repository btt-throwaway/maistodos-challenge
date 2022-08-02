# maistodos-challenge

## Descrição

O projeto foi desenvolvido usando um container Docker, para simplificar a execução em diferentes ambientes e evitar problemas de compatibilidade. 

Pela exiguidade do tempo, optei por uma abordagem mais direta. Como melhorias imediatas nesse código, faria a segmentação do processo em tarefas usando o Apache Airflow para sequenciar cada uma delas. 

Na pasta outputs estão os arquivos parquet gerados pela execução do código. Caso deseje verificar o output em uma execução local, basta apagá-los e executar o código que eles serão recriados. 

## Execução
Para executar o programa, basta executar os comandos a seguir:

```
docker-compose build

docker-compose up
```

O script irá preencher a pasta outputs com os arquivos parquet correspondentes a resposta solicitada. 



