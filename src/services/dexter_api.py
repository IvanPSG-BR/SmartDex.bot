from fastapi import FastAPI, HTTPException
from llama_cpp import Llama
from pydantic import BaseModel
import os, queue, time, threading

# Caminho relativo para o modelo
MODEL_PATH = os.path.join(os.path.dirname(__file__), "dexter_ai.gguf")

# Configurações do modelo
N_THREADS = 4  # Ajuste conforme o número de núcleos do seu processador

# Configuração da fila e limitador
request_queue = queue.Queue()
REQUEST_LIMIT = 5  # Requisições por segundo
INTERVAL = 1.0 / REQUEST_LIMIT

# Inicializar o modelo
print("Carregando o modelo...")
llm = Llama(model_path=MODEL_PATH, n_threads=N_THREADS)
print("Modelo carregado!")

# Inicializar o FastAPI
app = FastAPI()

# Definir o schema da requisição
class PromptRequest(BaseModel):
    prompt:str
    max_tokens:int = 1536
    temperature:float = 0.7
    top_p:float = 0.9
    stop:list = ["\n"]

def process_queue():
    while True:
        request = request_queue.get()
        if request is None:
            break
            
        # Processa a requisição
        try:
            output = llm(
                request["prompt"],
                max_tokens=request["max_tokens"],
                temperature=request["temperature"],
                top_p=request["top_p"],
                stop=request["stop"],
                echo=False
            )
            request["response_queue"].put({"response": output['choices'][0]['text']})
        except Exception as e:
            request["response_queue"].put({"error": str(e)})
            
        time.sleep(INTERVAL)

@app.get("/")
def read_root():
    return {"message": "API funcionando!"}

# Rota para gerar texto
@app.post("/generate")
def generate_text(request: PromptRequest):
    try:
        # Cria uma fila para a resposta
        response_queue = queue.Queue()
        
        # Prepara o request para a fila
        request_data = {
            "prompt": request.prompt,
            "max_tokens": request.max_tokens,
            "temperature": request.temperature,
            "top_p": request.top_p,
            "stop": request.stop,
            "response_queue": response_queue
        }
        
        # Adiciona à fila de processamento
        request_queue.put(request_data)
        
        # Espera a resposta (com timeout)
        result = response_queue.get(timeout=30)
        
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
            
        return result
    except queue.Empty:
        raise HTTPException(status_code=408, detail="O comando excedeu o tempo limite. Tente novamente.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Rota de saúde (health check)
@app.get("/health")
def health_check():
    return {"status": "ok"}

processing_thread = threading.Thread(target=process_queue, daemon=True)
processing_thread.start()
