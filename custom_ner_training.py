import spacy
import random

#1. Define your training data
TEXT_FROM_INVOICE = """
ABC Sueet, Sector-123

9801768410 Gurugram, Haryana
13011
 
Billed To Duteofisue lnvoice Number
Sata Mintal 2204 (7a 806
XYZ
Due Dae
25992020
Description Rate Qty Line Total
InvoiceNet - Trainer 5230.00 1 550,00
2
lnvoiceNet - Extactor 3500.00 1 $500.00
13h
Subwtl 750.00
75% (75%) 36.25
Total fosad
Amouat Paid 0.00

Anoum Due (USD)

"""

# --- THIS IS THE CORRECTED PART ---
TRAIN_DATA = [
    (
        TEXT_FROM_INVOICE,
        {
            "entities": [
                (116, 127, "BILLED_TO"),     # "Sata Mintal"
                (138, 141, "INVOICE_ID"),    # "806"
                (154, 162, "DUE_DATE"),      # "25992020"
                (368, 384, "AMOUNT_DUE")     # "Anoum Due (USD)"
            ]
        },
    )
]

#2. Set up the model
nlp = spacy.blank("en")
ner = nlp.add_pipe("ner")

for _, annotations in TRAIN_DATA:
    for ent in annotations.get("entities"):
        ner.add_label(ent[2])

#3. Train the model
print("---STARTING TRAINING---")
optimizer = nlp.begin_training()
for itn in range(20):
    random.shuffle(TRAIN_DATA)
    losses = {}
    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = spacy.training.Example.from_dict(doc, annotations)
        nlp.update([example], drop=0.5, sgd=optimizer, losses=losses)
    print(f"Iteration {itn+1}, Losses:{losses}")

print("--- TRAINING COMPLETE ---")

#4. Save the trained model
output_dir = "./my_invoice_model"
nlp.to_disk(output_dir)
print(f"Model saved to {output_dir}")