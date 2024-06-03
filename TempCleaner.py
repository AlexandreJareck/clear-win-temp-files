import os
import shutil
import logging

def configurar_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def obter_pasta_temp():
    return os.path.join('C:/Users', os.getlogin(), 'AppData/Local/Temp')

def deletar_conteudo_temp(pasta):
    contador_arquivos_deletados = 0
    contador_pastas_deletadas = 0

    for item in os.listdir(pasta):
        caminho_item = os.path.join(pasta, item)
        try:
            if os.path.isfile(caminho_item):
                os.unlink(caminho_item)
                logging.info(f'{item} arquivo deletado')
                contador_arquivos_deletados += 1
            elif os.path.isdir(caminho_item):
                if 'chocolatey' in caminho_item:
                    continue
                shutil.rmtree(caminho_item)
                logging.info(f'{item} pasta deletada')
                contador_pastas_deletadas += 1
        except Exception as e:
            logging.error(f'Acesso Negado ou Ocorreu um Erro com {item}: {e}')

    logging.info(f'{contador_arquivos_deletados} arquivos e {contador_pastas_deletadas} pastas deletadas.')

def principal():
    configurar_logging()
    pasta_temp = obter_pasta_temp()
    deletar_conteudo_temp(pasta_temp)
    input('Pressione <Enter> para Sair')

if __name__ == "__main__":
    principal()