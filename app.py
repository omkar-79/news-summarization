from flask import Flask, request, jsonify, render_template
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the pre-trained model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./t5_finetuned")
tokenizer = T5Tokenizer.from_pretrained("./t5_finetuned")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  

# Route for summarizing text
@app.route("/summarize", methods=["POST"])  
def summarize():

    data = request.form.get("article") 
    if not data:
        return render_template("index.html", error="No article provided.") 


    inputs = tokenizer.encode("summarize: " + data, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return render_template("index.html", summary=summary)  

if __name__ == "__main__":
    app.run(debug=True)
