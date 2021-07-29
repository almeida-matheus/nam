# TAR

> Ferramenta de compactação e descompactação de arquivos .tar
>>
> Utilizado com metodos de compressão como o de gzip ou bzip2

- Compartar arquivos em um arquivo tar:

`tar -cvf [file.tar] [file1] [file2] [file3]`

- Compactar arquivos em arquivo gzip:

`tar -czvf [file.tar.gz] [file1] [file2] [file3]`

- Compactar arquivos em arquivo gzip:

`tar -cjvf [file.tar.bz2] [file1] [file2] [file3]`

- Extrair arquivos de um arquivo compactado tar:

`tar -xvf [file.tar]`

- Extrair arquivos de um arquivo compactado tar gzip:

`tar -xzvf [file.tar.gz]`

- Extrair arquivos de um arquivo compactado tar bzip:

`tar -xjvf [file.tar.bz2]`

- Extrair arquivos de um arquivo compactado para um diretório específico:

`tar -xvf [file.tar] -C [path/to/dir]`

- Listar arquivos de um arquivo tar:

`tar -tvf [fil.tar]`