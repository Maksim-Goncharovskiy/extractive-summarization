import torch

from transformers import BertForSequenceClassification, BertTokenizer, AutoConfig
from summarizer import Summarizer


class Extrarizer:
    ext_model_name = 'DeepPavlov/rubert-base-cased'
    custom_tokenizer = BertTokenizer.from_pretrained(ext_model_name)
    custom_config = AutoConfig.from_pretrained(ext_model_name)
    custom_config.output_hidden_states = True
    custom_model = BertForSequenceClassification.from_pretrained(ext_model_name, config=custom_config)

    def __init__(self):
        self.summarizer = Summarizer(custom_model=Extrarizer.custom_model, custom_tokenizer=Extrarizer.custom_tokenizer)

    def summarize(self, text, num_sentences):
        return self.summarizer(text, num_sentences=num_sentences)


extrarizer = Extrarizer()