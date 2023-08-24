from flask import Flask, request
import random

app = Flask(__name__) 


@app.route("/sim-ou-nao", methods=["POST"]) #app principal de host
def sim_ou_nao():
    resposta = random.choice(["sim", "não"])
    return resposta


if __name__ == "__main__": #run main
    app.run(debug=True)
