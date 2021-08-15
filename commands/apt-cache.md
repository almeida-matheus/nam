# apt-cache

> Buscador de pacotes para distribuições baseadas no Debian.

- Buscar pacotes, no cache de pacotes APT, correspondentes ao critério de busca:

`apt-cache search {search_name}`

- Exibir informações sobre um pacote:

`apt-cache show {package_name}`

- Informar a situação de um pacote, se ele está instalado e atualizado:

`apt-cache policy {package_name}`

- Exibir as dependências de um pacote:

`apt-cache depends {package_name}`

- Exibir pacotes dependentes de um determinado pacote:

`apt-cache rdepends {package_name}`