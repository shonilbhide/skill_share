import os
import pickle
from sentence_transformers import SentenceTransformer, util


def save_model():
    model_name = 'distilbert-base-nli-mean-tokens'
    model_save_path = './models/model.pkl'  # Specify the desired path to save the model

    # Check if the file already exists
    if os.path.exists(model_save_path):
        print(f"The model file '{model_save_path}' already exists.")
    else:
        # Load the SentenceTransformer model
        model = SentenceTransformer(model_name)

        # Save the model as a pickle file
        with open(model_save_path, 'wb') as file:
            pickle.dump(model, file)

        print(f"Model saved successfully at '{model_save_path}'.")

def load_model(model_path):
    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

def get_embeddings(sentence,model):
    embedding = model.encode(sentence)
    return embedding

def compare(sentence_embeddings1, sentence_embeddings2):
    return util.pytorch_cos_sim(sentence_embeddings1, sentence_embeddings2)

def get_matches(incoming_data, result):
    embedding1 = incoming_data.description
    sorted_numbers = sorted(result, key=lambda x: compare(embedding1, x.description), reverse=True)
    top_items = sorted_numbers[:10]
    return top_items
