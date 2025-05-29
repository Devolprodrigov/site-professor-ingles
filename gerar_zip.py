from zipfile import ZipFile
import os

site_files = {
    "index.html": """<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Professor(a) de Inglês</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
    <h1>Aprenda Inglês com [Seu Nome]</h1>
    <nav>
      <ul>
        <li><a href="#sobre">Sobre</a></li>
        <li><a href="#servicos">Aulas</a></li>
        <li><a href="#depoimentos">Depoimentos</a></li>
        <li><a href="#contato">Contato</a></li>
      </ul>
    </nav>
  </header>
  <section id="hero">
    <h2>Desperte seu potencial com o inglês!</h2>
    <p>Aulas personalizadas, materiais exclusivos e acompanhamento de verdade.</p>
  </section>
  <section id="sobre">
    <h2>Sobre mim</h2>
    <p>Sou [Seu Nome], professor(a) de inglês com [X] anos de experiência.</p>
  </section>
  <section id="servicos">
    <h2>Aulas e Serviços</h2>
    <ul>
      <li>📘 Aulas particulares presenciais e online</li>
      <li>🎯 Preparação para exames (TOEFL, IELTS, etc)</li>
      <li>💼 Inglês para negócios</li>
      <li>✈️ Conversação para viagens</li>
    </ul>
  </section>
  <section id="depoimentos">
    <h2>Depoimentos</h2>
    <blockquote>"As aulas mudaram minha vida!"</blockquote>
    <blockquote>"O melhor professor de inglês que já tive!"</blockquote>
  </section>
  <section id="contato">
    <h2>Entre em Contato</h2>
    <form>
      <label>Nome:<br><input type="text" name="nome" required></label><br>
      <label>Email:<br><input type="email" name="email" required></label><br>
      <label>Mensagem:<br><textarea name="mensagem" required></textarea></label><br>
      <button type="submit">Enviar</button>
    </form>
  </section>
  <footer>
    <p>© 2025 [Seu Nome]. Todos os direitos reservados.</p>
  </footer>
</body>
</html>
""",
    "style.css": """body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}
header {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 20px 0;
}
header nav ul {
  list-style: none;
  padding: 0;
}
header nav ul li {
  display: inline;
  margin: 0 10px;
}
header nav ul li a {
  color: #fff;
  text-decoration: none;
}
#hero {
  background-color: #0066cc;
  color: white;
  padding: 50px;
  text-align: center;
}
section {
  padding: 20px;
  max-width: 800px;
  margin: auto;
  background: white;
  margin-bottom: 20px;
}
form input, form textarea {
  width: 100%;
  padding: 10px;
}
button {
  background-color: #0066cc;
  color: white;
  border: none;
  padding: 10px;
}
footer {
  background: #222;
  color: white;
  text-align: center;
  padding: 10px;
}
""",
    "script.js": "// Código JavaScript opcional para funcionalidades futuras"
}

with ZipFile("site-professor-ingles.zip"
