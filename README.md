This is the first line

# Comparação dos codigos - Aula 02
- Codigo servidor_eco.py x cliente_eco.py:

Nesse exemplo o servidor recebe apenas um cliente. Se o cliente enviar uma mensagem, o servidor recebe e envia essa mesma mensagem para o cliente (ex: eco:ola) confirmando o recebimento.

Se o cliente clicar em sair o servidor sai
Se o cliente cliclar Control C ele cai e o servidor também
Se o servidor cliclar Control C, o servidor cai, mas o cliente não é informando, porem o cliente percebe algo diferente pois nãorecebe mais o retorno do servidor na proxima mensagem, e ao tentar enviar uma mensagem novamente (ou seja, duas vezes após o servidor ter caido), o cliente também cai.

- Codigo servidor_eco_multi.py x cliente_eco_multi.py:

Nesse exemplo o servidor recebe mais de um cliente. Se o cliente enviar uma mensagem, o servidor recebe e envia essa mesma mensagem para o cliente (ex: eco:ola) confirmando o recebimento.

Se um cliente cair o servidor recebe a mensagem de Cliente Desconectou, mas o outro continua conectado 
Se o outro clinte sair (ou todos que estiverem conectados sairem) o servidor não cai, e outro cliente pode entrar normalmente

