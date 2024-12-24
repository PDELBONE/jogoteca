from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["jogoteca"]
collection = db["jogos"]

from views_game import *
from views_user import *

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10000)





# Anotações

#app.run(host='0.0.0.0', port=8080)
# Nem sempre queremos rodar nossa aplicação na porta 5000 ou mesmo deixar o nosso endereço como 127.0.0.1.
# Se eu quiser usar a porta 8080 para aplicação ou até mesmo permitir acessos externos à aplicação definindo o host como 0.0.0.0, como devo proceder?
# Quando executamos nossa aplicação Flask utilizamos uma instância do Flask e chamamos o método run. Perceba que quando fazemos isto no vídeo não passamos nenhum
# parâmetro para este método.
# Para definir a porta como 8080 e o host como 0.0.0.0 devemos chamar o run da seguinte maneira.

# upper: colocar os caracteres em caixa alta;
# round: arredondar números;
# trim: remover espaços do início e do fim do texto;
# default('texto exibido por padrão') - quando queremos mostrar algo, caso a variável esteja vazia ou nula.

# Tipos de Delimitadores do Jinja2:
# {%....%}: usado para inserir estruturas Python dentro de um arquivo html;
# {{....}}: usado para facilitar a exibição de código python como um output em um template HTML. Alternativa: {% print(....) %};
# {#....#}: usado para adicionar comentários que não serão exibidos no output do template HTML.

# Quando a aplicação oferece algum upload (imagens, pdf, vídeos etc) normalmente nos vem a questão: qual é o melhor lugar para guardar esses arquivos, no banco de dados ou no disco (algum storage)?
# Resposta rápida: O custo de espaço em banco de dados costuma ser mais caro que o custo de disco. Então, o ideal é que você use o disco para armazenar grandes volumes de arquivos e o banco de dados relacional
# para armazenar dados estruturados.
# Agora, pensando numa resposta mais elaborada, apesar da maioria das pessoas que desenvolvem preferir separar os dados binários dos dados estruturados, há também um aumento de complexidade nessa abordagem.
# É preciso sincronizar o storage com o banco de dados. Por exemplo, se apagarmos um jogo da aplicação, também é preciso apagar a imagem para não ficar um item "órfão". Também vamos precisar de mais um backup do
# banco e agora também do disco. Assim, mais um recurso na infraestrutura pode falhar e ter problemas de capacidade e precisamos considerá-lo no deploy.
# Colocando tudo no banco temos garantias transacionais e apenas um backup para ser feito. No entanto, quando os dados crescem, a velocidade e escalabilidade podem sofrer, além do custo alto já mencionado.
# Na Alura, os dados binários são separados dos dados da aplicação no banco. Todas as imagens vêm do storage na nuvem, o Amazon S3. Todos os dados estruturados vem do banco MySQL (também hospedado na Amazon).
