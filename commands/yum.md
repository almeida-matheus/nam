# YUM

> Gerenciador de pacotes das distribuições baseadas em RedHat.

- Atualizar os pacotes:

`yum update -y {package_name}`

- Instalar um pacote ou atualizá-lo para a versão mais recente:

`yum install -y {package_name}`

- Remover um pacote:

`yum remove {package_name}`

- Obter informações de um pacote:

`yum info {package_name}`

- Localizar um pacote específico:

`yum search {package_name}`

- Saber a qual pacote um arquivo pertence:

`yum provides [path/to/dir]`

- Listar os pacotes disponíveis:

`yum list {package_name}`