# Stone Tech

O teste foi dividido em duas partes, sendo a parte de banco de dados e a parte de programação.

## Banco de dados

Primeiro foi criado um novo database chamado "stone_bank". Dentro desse database foram criados três tabelas para a aplicação bancária (stonke_bank), sendo as seguintes:
## Tabela account

| Campo          | Descrição           |
|----------------|---------------------|
| id             | ID interno da conta |
| agency         | Agencia da conta    |
| account_number | Número da conta     |
| name           | Nome do cliente     |
| cpf            | CPF do cliente      |

Sendo que nenhum valor pode ser nulo, pois não faria sentido ter algum desses valores nulos.

Os indices criados para essa tabela foi nos campos:

* cpf
* agency & account_number

Tendo em vista que seriam os campos mais prováveis de ser utilizado para procurar uma conta.

Por fim, foi adicionado uma UNIQUE CONSTRAINT no cpf para garantir exista uma lógica de 1 pra 1 (uma conta para um cpf).

Com isso, as informações diretamente da tabela é a seguinte:

![image](https://user-images.githubusercontent.com/61243580/181960390-d8087c74-b32f-4802-ac16-02fa0794d237.png)


## Tabela transaction_type

| Campo          | Descrição           |
|----------------|---------------------|
| id             | ID interno          |
| description    | Tipo de transação   |

Essa tabela é onde fica armazenado os tipos de transações possíveis, para ficar melhor organizado e deixando os dados mais confiáveis.

Sendo que nenhum valor pode ser nulo, pois não faria sentido ter algum desses valores nulos.

Nessa tabela não foi criado indice.

Com isso, as informações diretamente da tabela é a seguinte:

![image](https://user-images.githubusercontent.com/61243580/181987236-5d41ac01-510f-4b8a-a944-3189b6b8f7e1.png)


## Tabela transaction

| Campo                   | Descrição               |
|-------------------------|-------------------------|
| id                      | ID interno              |
| amount                  | Valor da transação      |
| ref_date                | Data de referência      |
| external_agency         | Agencia banco externo   |
| external_account_number | Número da conta do banco externo |
| internal_account        | ID da conta interna     |
| transaction_type_id     | ID do tipo da transação |

Essa tabela é onde fica armazenado todas as transações realizadas, na qual referencia as duas tabelas anteriores, a partir da conta interna e o tipo da transação.

Nessa tabela, os únicos campos que podem ser nulos são os referentes a conta bancária externa, pois em caso de pagamento de boleto, saque e depósito não existiria uma conta externa para cadastro.

Para essa tabela, foi criado o indice do ref_date e do internal_account_id, tendo em vista que seriam os campos mais prováveis a serem utilizados em pesquisas.

Com isso, as informações diretamente da tabela é a seguinte:

![image](https://user-images.githubusercontent.com/61243580/181994531-76d734d3-a7dc-4462-8057-93ee713ddbef.png)

---

Foram criados dados fakes para testar o banco, estando no arquivo "insert_data.sql", e testar a query solicitada.

A query para retornar o valor total de pagamento de boletos do ano atual está no arquivo "select.sql", retornando o seguinte para os dados fakes criados:

<p align="center"> <img src="https://user-images.githubusercontent.com/61243580/181994710-f9e67cea-2f21-4748-bf76-1967b866de0b.png" /> </p>

Finalizando então a parte do SQL.

---

## Programação

As estruturas das listas são as seguintes:

<p align="center"> <img src="https://user-images.githubusercontent.com/61243580/181995323-095d479d-42e8-4e2b-b3df-944f715d266f.png" /> </p>

Foi criado uma classe com as funções requeridas, sendo elas as seguintes:

* Validação de email --> (validate_duplicate_email)

Foi criado a função de validação de emails duplicados no qual apenas retorna erro caso exista, porém pensei no caso de o usuário querer saber quais emails estão duplicados, então também foram criados as funções "validate_duplicate_email_v2" e "validate_duplicate_email_v3" no qual retorna o primeiro email duplicado que achar e todos os emails duplicados encontrados na lista, respectivamente.
Também foi criado a função para realizar o filtro desses emails duplicados e nulos. Nenhuma dessas funções foram utilizadas, porém estão dentro da classe para o caso de ter algum interesse em utilizar.

* Validação de lista vazia --> (validate_empty_list)

Para a função de validação de lista vazia, basicamente retorna caso venha a lista vazia.

* Validação de valores negativos --> (validate_qnt_price)

Foi considerado que sempre irá ser passado os dados na estrutura padrão, com isso, apenas foi validado se o valor passado é menor que zero.

* Soma total dos valores --> (price_all_items)

Retorna o preço total da compra.

* Valor que cada um deverá pagar --> (split_bill)

Retorna um dicionário com email -> valor, sendo que os primeiros da lista serão os que irão receber o valor a mais caso exista resto na divisão.

* Função principal --> (split)

Função na qual roda todas as validações e retorna o dicionário com os valores que cada um deve pagar.

---

## Rodando o código

Para rodar o código, deve-se editar as listas no arquivo list.py, e no terminal rodar o seguinte:

```bash
python3 programming/run.py
```

No arquivo run.py foi criado um exemplo com um FOR para retornar de forma melhor o resultado, sendo um exemplo com 100 dividindo em 3, resulta no seguinte:

![image](https://user-images.githubusercontent.com/61243580/181995985-fd2f6b2b-cf17-4586-b39f-03e8a5bf530d.png)

---

Após feito tudo, temos os teste unitários, no qual estão na pasta programming/test/

Para rodar os testes temos o seguinte:

#### Rodar apenas um teste

```bash
python3 -m unittest programming/test/NOME_TESTE.py -v
```

#### Rodar todos os testes

```bash
python3 -m unittest discover programming/test/ -v
```

O "-v" (verbose) serve para mostrar teste a teste e não só o resultado final.

Rodando todos os teste, resulta no seguinte:

![image](https://user-images.githubusercontent.com/61243580/181995837-6860c7ab-e76b-4429-b362-86175b387bde.png)