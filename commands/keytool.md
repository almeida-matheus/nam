# KEYTOOL

> Ferramenta para gerenciar certificados digitais

## Exibir

- Obter informações do certificado JKS KEYSTORE:

`keytool -list -v -keystore [Certificate.jks] -storepass {private_passwd_jks}`

## Converter

- Converter PKCS12 [PFX ou P12] para JKS ou KEYSTORE interativamente:

`keytool -importkeystore -srckeystore [Certificate.pfx] -srcstoretype pkcs12 -destkeystore [Certificate.jks] -deststoretype JKS`

- Converter PKCS12 [PFX ou P12] para JKS KEYSTORE passando senha diretamente:

`keytool -importkeystore -srckeystore [Certificate.pfx] -srcstoretype pkcs12 -srcalias 1 -destkeystore [Certificate.jks] -deststoretype jks -destalias {new_alias} -deststorepass {password_jks} -srcstorepass {password_pfx}`

- Converter PKCS12 [PFX ou P12] para JKS KEYSTORE passando arquivo com senha:

`keytool -importkeystore -srckeystore [Certificate.pfx] -srcstoretype pkcs12 -srcalias 1 -destkeystore [Certificate.jks] -deststoretype jks -destalias {new_alias} -deststorepass:file [password_jks.txt] -srcstorepass:file [password_pfx.txt]`

- Converter JKS KEYSTORE para PKCS12 [PFX ou P12]:

`keytool -importkeystore -srckeystore [Certificate.jks] -srcstoretype JKS -destkeystore [Certificate.pfx] -deststoretype PKCS12`

- Converter PEM - [base64] para JKS KEYSTORE:

`keytool -import -trustcacerts -alias {new_alias} -file [Certificate.cer] -keystore [Certificate.jks]`

## Alterar

- Alterar JKS alias:

`keytool -keystore [Certificate.jks] -changealias -alias {old_alias} -destalias {new_alias}`

