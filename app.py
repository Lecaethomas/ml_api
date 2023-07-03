# Start the API :: " python app.py "

from flask import Flask, request, jsonify
import joblib
import spacy
import sys

app = Flask(__name__)

# Le modèle pour identifier les stop_words, ponctuation... (ajouté avec conda)
nlp = spacy.load("fr_core_news_md")

# Load the SVM model and vectorizer
svr = joblib.load('data/svm_model.joblib')

vectorizer = joblib.load('data/vectorizer.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input sentence from the request
    sentence = request.json['data']
    print(sentence, file=sys.stderr)
    sentence = nlp(sentence)
    no_stop_lemma_list = []

    for token in sentence:
    # On rajoute un token à la liste s'il remplit les conditions suivantes
        if not (token.is_stop or token.is_punct) and token.is_alpha and len(token) >= 3:
            no_stop_lemma_list.append(token.lemma_)

        # On concatène les éléments de la liste, séparés par un espace
    no_stop_lemma = " ".join(no_stop_lemma_list)
    print(no_stop_lemma)
    # Preprocess the input sentence using the same vectorizer
    vectorized_sentence = vectorizer.transform([no_stop_lemma])
    print(vectorized_sentence)
    # Make predictions using the SVM model
    prediction = svr.predict(vectorized_sentence)[0]
    # Return the predicted note as a respons
    response = {'note': int(prediction)}
    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
