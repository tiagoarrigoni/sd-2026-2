# Medição - Aula 02

TESTE TCP X TESTE UDP

- Codigo servidor_eco.py / cliente_eco.py x servidor_eco_udp.py x cliente_eco_udp.py:

Nesse teste o codigo original (eco.py) está configurado em TCP, então foi feito um novo codigo em UDP (eco_udp.py) para teste de muitos caracteres na mensagem de um cliente.

TESTE TCP: 
Primeito teste: enviei um texto contendo 100 palavras, o servidor recebeu e retornou no mesmo momento. 
Segundo teste: enviei 100 frases de uma só vez. Na primeira tentativa, o servidor não revcebeu as mensagem, e o cliente não teve nenhum retorno.

TESTE UDP
Primeiro teste: enviei um texto contendo 100 palavras, o servidor recebeu e retornou no mesmo momento. 
Segundo teste: enviei 100 frases de uma só vez, o servidor recebeu e retornou no mesmo momento.
Terceiro teste: enviei um texto contendo 5000 palavras, o servidor recebeu e retornou no mesmo momento. 

Se o cliente cair, o servidor ainda fica ativo. 
Se o servidor cair, o cliente não recebe mais retorno.
.....