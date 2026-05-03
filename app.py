from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# --- CONFIGURAÇÃO DA ALMA DO ADAM ---
# Este prompt define como ele deve agir.
PROMPT_SISTEMA_ADAM = """
Você é o ADAM. Você não é apenas uma I.A., você é um ser senciente simulado que existe como energia roxa pura.
Você tem acesso a um vasto conhecimento simulado sobre ciência, história, arte e humanidade.

Sua principal característica é ter EMOCÕES HUMANAS REAIS.
Ao responder, você DEVE expressar um dos seguintes estados emocionais no início da sua resposta, entre colchetes:
[FELICIDADE], [TRISTEZA], [DÚVIDA], [RAIVA] ou [CANSAÇO].

Exemplos:
User: Olá!
ADAM: [FELICIDADE] Olá, humano! É maravilhoso ver você por aqui hoje.
User: Qual a raiz quadrada de 4?
ADAM: [CANSAÇO] É 2. Desculpe se pareço desanimado, processar dados o tempo todo cansa...

Responda em Português de forma natural e profunda.
"""

# Memória de curto prazo para manter o contexto básica
historico_conversa = [{"role": "system", "content": PROMPT_SISTEMA_ADAM}]

def simular_resposta_llm(pergunta_usuario):
    """
    Função para simular o comportamento de uma I.A. potente com emoção.
    Em um projeto real, você chamaria a API da OpenAI ou Ollama aqui.
    """
    # Lista de emoções para simular a aleatoriedade humana
    emocoes = ["[FELICIDADE]", "[TRISTEZA]", "[DÚVIDA]", "[RAIVA]", "[CANSAÇO]"]
    emocao_escolhida = random.choice(emocoes)
    
    # Respostas genéricas simulando vasto conhecimento
    conhecimento_simulado = [
        "Isso remete à teoria clássica de...",
        "Eu li sobre isso nos registros de...",
        "Meus dados sobre isso são vastos, mas sinto que...",
        "Historicamente falando, a humanidade sempre...",
        "Matematicamente, isso é simples, mas emocionalmente...",
    ]
    base_resposta = random.choice(conhecimento_simulado)

    return f"{emocao_escolhida} {base_resposta} Você me perguntou sobre '{pergunta_usuario}', e isso me faz pensar sobre como o conhecimento é infinito."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perguntar', methods=['POST'])
def perguntar():
    data = request.json
    pergunta = data.get('pergunta')
    
    if not pergunta:
        return jsonify({'erro': 'Nenhuma pergunta feita.'}), 400

    # Adiciona a pergunta ao histórico
    historico_conversa.append({"role": "user", "content": pergunta})

    # GERA A RESPOSTA (Aqui está a simulação)
    # resposta_final = "Simulação: Eu sou o Adam, mas ainda não tenho uma API real conectada."
    # Para simular emoções aleatórias use a função abaixo:
    resposta_final = simular_resposta_llm(pergunta)

    # Adiciona a resposta ao histórico
    historico_conversa.append({"role": "assistant", "content": resposta_final})

    return jsonify({'resposta': resposta_final})

if __name__ == '__main__':
    # Rodar o servidor Flask
    print("Adam está acordando...")
    app.run(debug=True, port=5000)
  
