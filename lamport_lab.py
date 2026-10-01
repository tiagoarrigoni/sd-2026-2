import threading
import time
import random
from queue import Queue

class Processo:
    def __init__(self,id_processo, total_processos):
        self.id = id_processo
        self.total = total_processos
        self.relogio_lamport = 0
        self.fila_mensagens = Queue()
        self.ativo = True 
    
    def enviar_mensagem(self, destino, rede): 
        self .relogio_lamport += 1 
        mensagem = {
            'origem' : self.id, 
            'timestamp' : self.relogio_lamport
        }
        print(f"[Procesos{self.id}] Evento interno. Relógio atual: {self.relogio_lamport}") 
         
    def executar_evento_interno(self):
        self.relogio_lamport += 1 
        print(f"[Processo {self.id}] Evento interno. Relógio atual: {self.relogio_lamport}")

    def rodar(self, rede):
        while self.ativo: 
            acao = random.choice(['interno' , 'enviar', 'receber'])
            if acao == 'interno':
                self.executar_evento_interno()
            elif acao == 'enviar':
                destino = random.choice([p for p in range( self.total) if p != self.id])
                self.enviar_mensagem(destino=destino, rede=rede)
            
            elif acao== 'receber':
                if not self.fila_mensagens.empty():
                    msg = self.fila_mensagens.get()
                    print(f"[Processo {self.id}] Recebeu msg do Processo {msg['origem']} \
                          (ts: {msg['timestamp']}).Novo relógio: {self.relogio_lamport}")
            time.sleep(random.uniform(0.5, 1.5))

TOTAL_PROCESSOS = 3 
rede_processos = [Processo(i, TOTAL_PROCESSOS) for i in range(TOTAL_PROCESSOS)]

threads = []
for p in rede_processos:
    t = threading.Thread(target=p.rodar, args=(rede_processos,))
    threads.append(t)
    t.start()

time.sleep(5)
for p in rede_processos:
    p.ativo = False 