# PIP

> Gerenciador de pacotes do Python.

- Instalar o pip:

`apt-get install python3-pip`

- Atualizar o pip:

`python3 -m pip install --upgrade pip`

- Instalar um pacote:

`pip install {package}`

- Atualizar um pacote:

`pip install —upgrade {package}`

- Desinstalar um pacote:

`pip uninstall {package}`

- Reinstalar um pacote:

`sudo pip install {package} --force-reinstall`

- Atualizar um pacote:

`pip install {package} --upgrade`

- Fazer download do pacote no diretório atual:

`pip install {package} -t .`

- Listar os pacotes que o se ambiente possui instalado:

`pip freeze`
`pip list`

- Instalar pacotes com base em um arquivo:

`pip install -r {requeriments.txt}`

- Listar todos pacotes utilizados no projeto e redirecionar para o requeriments.txt:

`pipreqs [path/to/dir]`