import torch
from transformers import BartForConditionalGeneration, BartTokenizer
from transformers import AdamW
from torch.utils.data import DataLoader
from transformers import BartTokenizer, BartConfig
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset

class SummarizationDataset(Dataset):
    def __init__(self, tokenizer, data):
        self.tokenizer = tokenizer
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        source_text = self.data[idx]['source_text']
        target_text = self.data[idx]['target_text']

        source_tokens = self.tokenizer.batch_encode_plus([source_text], truncation=True, padding='longest', max_length=1024, return_tensors='pt')
        target_tokens = self.tokenizer.batch_encode_plus([target_text], truncation=True, padding='longest', max_length=1024, return_tensors='pt')

        source_ids = source_tokens['input_ids'].squeeze()
        source_mask = source_tokens['attention_mask'].squeeze()
        target_ids = target_tokens['input_ids'].squeeze()
        target_mask = target_tokens['attention_mask'].squeeze()

        return {
            'source_ids': source_ids,
            'source_mask': source_mask,
            'target_ids': target_ids,
            'target_mask': target_mask
        }

def collate_fn(batch):
    source_ids = [item['source_ids'] for item in batch]
    source_mask = [item['source_mask'] for item in batch]
    target_ids = [item['target_ids'] for item in batch]
    target_mask = [item['target_mask'] for item in batch]

    source_ids = pad_sequence(source_ids, batch_first=True, padding_value=1)
    source_mask = pad_sequence(source_mask, batch_first=True, padding_value=0)
    target_ids = pad_sequence(target_ids, batch_first=True, padding_value=-100)
    target_mask = pad_sequence(target_mask, batch_first=True, padding_value=0)

    return {
        'input_ids': source_ids,
        'attention_mask': source_mask,
        'labels': target_ids,
        'target_mask': target_mask
    }

# Load the dataset
# Your dataset loading code here

# Load the BART tokenizer
tokenizer = BartTokenizer.from_pretrained('bart-large')

# Create the dataset
dataset = SummarizationDataset(tokenizer, your_data)

# Define the data loader
data_loader = DataLoader(dataset, batch_size=4, collate_fn=collate_fn)

# Load the BART model for conditional generation
model = BartForConditionalGeneration.from_pretrained('bart-large')

# Set the device to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Set the optimizer and learning rate
optimizer = AdamW(model.parameters(), lr=1e-5)

# Training loop
for epoch in range(5):
    model.train()
    total_loss = 0
    for batch in data_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        target_mask = batch['target_mask'].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels, decoder_attention_mask=target_mask)
        loss = outputs.loss
        total_loss += loss.item()

        optimizer.zero_grad()
        loss.backward
