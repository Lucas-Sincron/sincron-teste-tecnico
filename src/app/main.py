# Importando Bibliotecas necessárias
from flask import *
from routes import *

# Criando o app Flask
app = Flask(__name__)

from routes import *

# Garante que ele só será executado quando for rodado com código principal
if __name__ == "__main__":
    app.run()

# Passo a passo

# Baixar o Flask Pelo Terminal
# $ pip install flask

# Selecione no terminal do vscode: Powershell

# Verifique em que pasta você está com o código
# $ pwd

# Se estiver na pasta src
# $ python app/main.py

# Se estiver na pasta principal
# $ python src/app/main.py

# Desde modo, aparecerá a porta que o código vai rodar
# Aperte Ctrl e clique nessa porta

# Assim abrirá uma tela com o código rodando