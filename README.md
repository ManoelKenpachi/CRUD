# crud
 
Após clonar a aplicação, é necessário baixar as dependências.
pip install -r requirements.txt

Basta rodar a aplicação:
python app.py

A aplicação vai retorna no IP: http://localhost:5000/

![image](https://user-images.githubusercontent.com/102999346/166204799-73e4eac1-6269-4059-b499-33a8e2bd355c.png)

Para facilitar a vizualização, há filtros de quantidade de páginas e registros por página, é possível ordernar e de pesquisar.

Para editar é possível fazer direto na tabela, e no console fixa um registro da alteração:
![image](https://user-images.githubusercontent.com/102999346/166205370-1466cfa1-64e6-418f-baa1-6de8c9fd4bf8.png)

o endpoint para download do csv: http://localhost:5000/save/data.csv

O gráfico ficou em um serviço a parte:
python dashboard.py

Seu endpoint: http://localhost:8050