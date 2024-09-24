meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobacion",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado"
            }

while True:
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Perdon, no tenemos esa palabra en el diccionario, ahorita lo actualizaremos")
        palabra = input("Pon la palabra que quieras aniadir: ")
        definicion = input("Pon la definicion de esta palabra: ")
        meme_dict[palabra] = definicion
        print(meme_dict)
    continue
