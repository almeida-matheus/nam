# OPENSSL

> Ferramenta que realiza diversas funções criptográficas.

## Gerar

- Gerar chave RSA:

`openssl genrsa -out {private.key} 2048`

- Gerar uma requisição CSR com chave privada existente:

`openssl req -out {request.csr} -key {private.key} -new`

- Gerar uma requisição CSR com uma nova chave privada:

`openssl req -out {request.csr} -new -newkey rsa:2048 -nodes -keyout {private.key}`

- Gerar uma requisição CSR com uma nova chave privada sem o prompt interativo:

` openssl req -out {request.csr} -newkey rsa:2048 -nodes -keyout {private.key} -subj {"/C=BR/ST=MG/L=BH/O=Security/OU=IT Department/CN=example.com"}`

- Gerar uma requisição CSR com uma nova chave privada com base em arquivo de configuração do CSR:

`openssl req -config {csr.conf} -new -newkey rsa:2048 -nodes -keyout {private.key} -out {request.csr}`

## Exibir

- Exibir informações da requisição CSR:

`openssl req -in {request.csr} -text -noout`

- Exibir informações do certificado em formato texto

`openssl x509 -inform PEM -in {certificate.pem} -text`

- Extrair fingerprint do certificado:

`openssl x509 -noout -fingerprint -sha256 -inform pem -in {certificate.cer} | sed 's/://g' | tr '[:upper:]' '[:lower:]' | sed 's/sha256 fingerprint=//g'`

## Converter

- Converter DER [binário] para PEM [base64]:

`openssl x509 -in {certificate.cer} -inform der -out {certificate.pem} -outform pem`

- Converter PEM - [base64] para DER [binário]:

`openssl x509 -in {certificate.pem} -inform pem -out {certificate.cer} -outform der`

- Converter PEM(público + privado + cadeia) para PFX:

`openssl pkcs12 -export -out {certificate.pfx} -inkey {private.key} -in {certificate.cer} -certfile {chain.crt} -passout file:{password_pfx.txt}`

- Converter PEM(público + privado) para PFX:

`openssl pkcs12 -export -out {certificate.pfx} -inkey {private.key} -in {certificate.cer} -passout file:{password_pfx.txt}`

## Criptografia

- Descriptografar chave privada:
`openssl rsa -in [Encrypted.key] -out [Decrypted.key]`

- Criptografar chave privada usando AES-256 - requer senha:
`openssl rsa -in [Decrypted.key] -out [Encrypted.key] -aes256`

- Criptografar chave privada usando AES-256 - requer senha:
`openssl rsa -in [Decrypted.key] -out [Encrypted.key] -des3Tri`