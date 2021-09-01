# ALIAS

> Cria palavras que são substituídas por um comando.

- Criar um apelido:

`alias {alias}="{command}"`

- Visualizar o comando associado a um determinado apelido:

`alias {alias}`

- Remover um apelido:

`unalias {alias}`

- Exibir todos os apelidos definidos:

`alias -p`

- Tornar o comando `rm` interativo:

`alias {rm}="{rm -i}"`

- Criar o apelido `la` como um atalho para `ls -a`:

`alias {la}="{ls -a}"`