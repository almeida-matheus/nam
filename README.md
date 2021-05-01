

<h1 align="center"><img src="./assets/nam-icon.png" alt="nam icon"></h1>

<p align="center">
  <a href="#about-the-project">About the project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#how-to-use">How to use</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#installation">Installation</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contributing">Contributing</a>
</p>

<br>

## About the project
### `In progress`

Nam is an interface for viewing terminal commands with their main parameters
<!--<img src="./assets/nam-example.png" alt="nam example">-->
```
APT-CACHE

Buscador de pacotes para distribuições baseadas no Debian.

- Buscar pacotes no cache de pacotes APT:
  apt-cache search criterio_de_busca

- Exibir informações sobre um pacote:
  apt-cache show nome_do_pacote

- Informar a situação de um pacote, se ele está instalado e atualizado:
  apt-cache policy nome_do_pacote

- Exibir as dependências de um pacote:
  apt-cache depends nome_do_pacote

- Exibir pacotes dependentes de um determinado pacote:
  apt-cache rdepends nome_do_pacote
```

<!-- USAGE -->
## How to use
Type nam followed by the command name

Example:
```
nam tar
```
For more options type `nam --help`

Output:
```
                            NAM
------------------------------------------------------------
| how to use: nam command                                  |
------------------------------------------------------------
| -h, --help   | display this help text                    |
| -l, --list   | show all commands of nam                  |
| -a, --att    | update to add new commands                |
------------------------------------------------------------
                                              version: 0.01
```

<!-- INSTALATION -->
## Installation
#### 1. Install Python
```
sudo apt install python3
```

#### 2. Clone git repository
```
git clone "https://github.com/almeida-matheus/nam"
```

#### 3. Execute install.sh
```
cd nam/
chmod +x install.sh
./install.sh
```

<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Clone this project (`https://github.com/almeida-matheus/nam`)
3. Create your Feature Branch (`git checkout -b nameBranch`)
4. Add your Changes (`git add .`)
5. Commit your Changes (`git commit -m 'Add some feature'`)
6. Push to the Branch (`git push origin nameBranch`)
7. Open a Pull Request
