# DPKG

> Gerenciador de pacotes Debian.

- Instalar um pacote:

`dpkg -i [file.deb]`

- Remover um pacote:

`dpkg -r {package_name}`

- Exibir os pacotes correspondentes ao critério de busca:

`dpkg -l {search_name}`

- Exibe o conteúdo do pacote:

`dpkg -L {package_name}`

- Exibir o conteúdo do arquivo de um pacote:

`dpkg -c [file.deb]`

- Apresentar o pacote proprietário de um determinado arquivo:

`dpkg -S {package_name}`