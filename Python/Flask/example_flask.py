from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <style>
            body {
                background-color: #f2f2f2;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
                text-align: center;
            }
            
            p {
                color: #666;
                font-size: 18px;
                line-height: 1.5;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bem-vindo ao meu aplicativo Flask!</h1>
            <p>O Zac quer muito um emprego de meio período como desenvolvedor backend de Python para alugar uma kitnet e sair logo de casa.</p>
            <p>Ele está aprendendo Flask para criar aplicativos web incríveis.</p>
            <p>Este é apenas um exemplo simples, mas você pode adicionar mais elementos HTML, estilizar a página com CSS e organizar o conteúdo como desejar.</p>
        </div>
    </body>
    </html>
    """

@app.route('/exemplo1')
def ex1():
    return """
    <html>
    <head>
        <style>
            body {
                background-color: #b6aeff;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
                text-align: center;
            }
            
            p {
                color: #666;
                font-size: 18px;
                line-height: 1.5;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Página de exemplo 1</h1>
            <p>Somente um exemplo</p>
        </div>
    </body>
    </html>
    """

@app.route('/exemplo2')
def ex2():
    return """
    <html>
    <head>
        <style>
            body {
                background-color: #F7FFAE;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
            }
            
            h1 {
                color: #333;
                text-align: center;
            }
            
            p {
                color: #666;
                font-size: 18px;
                line-height: 1.5;
            }
            
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Opa, mais um exemplo</h1>
            <p>Quem diria...</p>
        </div>
    </body>
    </html>
    """

@app.route('/exemplo_renderizar')
def exemplo_renderizar():
    return render_template("pagina.html")

if __name__ == "__main__":
    app.run(debug=True)
