# KEYTOOL

> Ferramenta para gerenciar certificados digitais

- Converter .PFX para .JKS ou KEYSTORE:

`keytool -importkeystore -srckeystore [Certificate.pfx] -srcstoretype pkcs12 -destkeystore [Certificate.jks] -deststoretype JKS`

- Converter .PFX para .JKS ou KEYSTORE passando senha diretamente:

`keytool -importkeystore -srckeystore [Certificate.pfx] -srcstoretype pkcs12 -srcalias 1 -destkeystore [Certificate.jks] -deststoretype jks -deststorepass {private_passwd_jks} -destalias {new_alias}`

- Converter .CER para .JKS:

`keytool -import -trustcacerts -alias {new_alias} -file [Certificate.cer] -keystore [Certificate.jks]`

- Converter .JKS para .PFX:

`keytool -importkeystore -srckeystore [Certificate.jks] -srcstoretype JKS -destkeystore [Certificate.pfx] -deststoretype PKCS12`

- Verificar JKS Alias:

`keytool -list -v -keystore [Certificate.jks] | grep "Alias"`

- Alterar JKS Alias:

`keytool -keystore [Certificate.jks] -changealias -alias {old_alias} -destalias {new_alias}`