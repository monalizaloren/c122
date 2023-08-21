from flask import Flask, render_template, url_for, request, jsonify
from model_prediction import * 
from predict_response import *
 
app = Flask(__name__)

predicted_emotion=""
predicted_emotion_img_url=""

@app.route('/')
def index():
    entries = show_entry()
    return render_template("index.html", entries=entries)
 
@app.route('/predict-emotion', methods=["POST"])
#Passo 1
    
    # Obtenha a entrada de texto da requisição POST
    

    
    if not input_text:
        # Resposta a enviar se input_text não for definida
       
     
     
     
        
        # Resposta a enviar se input_text for definida
       



     

        # Enviar resposta         
        

     


@app.route("/save-entry", methods=["POST"])
def save_entry():

    # Obtenha a data, a emoção prevista e o texto digitado pelo usuário para salvar a entrada
    


 

    save_text = save_text.replace("\n", " ")

    # Entrada CSV
    entry = f'"{date}","{save_text}","{emotion}"\n'  

    with open("./static/assets/data_files/data_entry.csv", "a") as f:
        f.write(entry)
    return jsonify("Success")


@app.route("/bot-response", methods=["POST"])
def bot():
    # Obtenha a entrada do usuário
    input_text = request.json.get("user_bot_input_text")
   
    # Chame o método para obter a resposta do robô
    bot_res = bot_response(input_text)

    response = {
            "bot_response": bot_res
        }

    return jsonify(response)     
     
if __name__ == '__main__':
    app.run(debug=True)
