# AWS

> Configurar o ambiente AWS.
>>
> `aws {command} wait {subcommand} {parameters}`
>>
> Instalação: `apt install -y awscli` e `yum -y install aws-cli` 
>>
> Atualização: `pip3 install --upgrade awscli`.

- Registrar conta AWS CLI:

`aws configure`

- Usuário que está realizando está chamada:

`aws sts get-caller-identity`