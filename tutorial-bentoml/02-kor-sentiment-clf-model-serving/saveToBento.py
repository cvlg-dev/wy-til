import torch
from transformers import BertForSequenceClassification
from KobertSentiClassificationService import KobertSentiClassifier


def set_model_dir(self):
    self.model_dir = './model'

def saveToBento():

    bento_service = KobertSentiClassifier()
    model_dir = set_model_dir()
    
    model = BertForSequenceClassification.from_pretrained(model_dir)
    tokenizer = BertForSequenceClassification.from_pretrained(model_dir)
    artifact = {"model": model, "tokenizer": tokenizer}
    bento_service.pack("model", artifact)

    saved_path = bento_service.save()
    print('Bento Service Saved in ', saved_path)

if __name__ == "__main__":
    saveToBento()