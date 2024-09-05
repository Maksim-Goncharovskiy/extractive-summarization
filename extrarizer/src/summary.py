from transformers import BertForSequenceClassification, BertTokenizer, AutoConfig
from summarizer import Summarizer

model_name = 'DeepPavlov/rubert-base-cased'

tokenizer = BertTokenizer.from_pretrained(model_name)
config = AutoConfig.from_pretrained(model_name)

config.output_hidden_states = True

base_model = BertForSequenceClassification.from_pretrained(model_name, config=config)

model = Summarizer(custom_model=base_model, custom_tokenizer=tokenizer)


def make_extract_summary(text: str, ratio: float) -> str:

    summary = model(text, ratio=ratio)

    return summary


