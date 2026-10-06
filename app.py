from flask import Flask, render_template_string, request

app = Flask(__name__)

# Single HTML template with CSS styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>R Counter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f7f6;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 400px;
            width: 100%;
        }
        h1 {
            color: #333;
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
        }
        input[type="text"] {
            width: 80%;
            padding: 10px;
            font-size: 1rem;
            border: 2px solid #ddd;
            border-radius: 6px;
            margin-bottom: 1rem;
            outline: none;
        }
        input[type="text"]:focus {
            border-color: #007bff;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 1rem;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.2s;
        }
        button:hover {
            background-color: #0056b3;
        }
        .result {
            margin-top: 1.5rem;
            font-size: 1.2rem;
            color: #2c3e50;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>How many R's are in your word?</h1>
        <form method="POST">
            <input 
                type="text" 
                name="word" 
                placeholder="Enter a word..." 
                value="{{ word }}" 
                required 
                autofocus
            >
            <br>
            <button type="submit">Count R's</button>
        </form>

        {% if count is not none %}
            <div class="result">
                The word "<strong>{{ word }}</strong>" contains <strong>{{ count }}</strong> R's.
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    word = ""
    count = None
    if request.method == "POST":
        word = request.form.get("word", "")
        # Case-insensitive count of 'r'
        count = word.lower().count("r")
    
    return render_template_string(HTML_TEMPLATE, word=word, count=count)

if __name__ == "__main__":
    app.run(debug=True)
