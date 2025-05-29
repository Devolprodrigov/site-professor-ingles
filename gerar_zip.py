from zipfile import ZipFile

# Conteúdo dos arquivos do site
site_files = {
    "index.html": """<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aulas de Inglês com [Seu Nome]</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="topo">
    <div class="container">
      <h1>[Seu Nome]</h1>
      <nav>
        <ul>
          <li><a href="#sobre">Sobre</a></li>
          <li><a href="#aulas">Aulas</a></li>
          <li><a href="#avaliacoes">Avaliações</a></li>
          <li><a href="#contato">Contato</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <section class="hero">
    <div class="container">
      <h2>Aulas de Inglês Online Personalizadas</h2>
      <p>Aprenda no seu ritmo com um professor experiente e materiais exclusivos.</p>
      <a href="#contato" class="btn">Agende sua primeira aula</a>
    </div>
  </section>

  <section id="sobre" class="container">
    <h2>Sobre mim</h2>
    <p>Sou [Seu Nome], professor(a) de inglês com mais de [X] anos de experiência. Tenho paixão por ajudar alunos a conquistarem seus objetivos com o idioma, seja para viagens, carreira ou exames.</p>
  </section>

  <section id="aulas" class="container">
    <h2>Tipos de Aula</h2>
    <ul class="servicos">
      <li>📚 Inglês para iniciantes e intermediários</li>
      <li>💼 Inglês para negócios</li>
      <li>🎯 Preparação para TOEFL, IELTS</li>
      <li>✈️ Conversação para viagens</li>
      <li>👨‍🏫 Aulas personalizadas individuais</li>
    </ul>
  </section>

  <section id="avaliacoes" class="container">
    <h2>Avaliações de Alunos</h2>
    <blockquote>“Didática excelente! Me sinto mais confiante a cada aula.”</blockquote>
    <blockquote>“Muito paciente e atenciosa. Recomendo demais!”</blockquote>
  </section>

  <section id="contato" class="container">
    <h2>Agende uma Aula</h2>
    <form>
      <label>Nome:<br><input type="text" name="nome" required></label><br>
      <label>Email:<br><input type="email" name="email" required></label><br>
      <label>Mensagem:<br><textarea name="mensagem" required></textarea></label><br>
      <button type="submit">Enviar</button>
    </form>
  </section>

  <footer>
    <div class="container">
      <p>© 2025 [Seu Nome] – Aulas de Inglês Online</p>
    </div>
  </footer>

  <script src="script.js"></script>
</body>
</html>
""",

    "style.css": """body {
  margin: 0;
  font-family: 'Segoe UI', sans-serif;
  background-color: #f8f9fa;
  color: #333;
}
.container {
  max-width: 900px;
  margin: auto;
  padding: 20px;
}
.topo {
  background-color: #004080;
  color: white;
  padding: 10px 0;
}
.topo h1 {
  margin: 0;
}
.topo nav ul {
  list-style: none;
  display: flex;
  gap: 20px;
  padding: 0;
}
.topo nav a {
  color: white;
  text-decoration: none;
}
.hero {
  background-color: #e6f0ff;
  text-align: center;
  padding: 60px 20px;
}
.hero h2 {
  font-size: 2em;
}
.btn {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #004080;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}
section {
  margin: 40px 0;
}
.servicos {
  list-style: none;
  padding: 0;
}
.servicos li {
  padding: 5px 0;
}
blockquote {
  background: #f1f1f1;
  padding: 15px;
  border-left: 5px solid #004080;
  margin: 20px 0;
}
form input, form textarea {
  width: 100%;
  padding: 10px;
  margin-top: 10px;
  box-sizing: border-box;
}
button {
  background-color: #004080;
  color: white;
  padding: 10px 20px;
  border: none;
  margin-top: 10px;
  cursor: pointer;
}
footer {
  background: #222;
  color: white;
  text-align: center;
  padding: 15px;
}
""",

    "script.js": """// Futuras funcionalidades podem ser adicionadas aqui
console.log("Site carregado com sucesso.");
"""
}

# Criação do arquivo .zip
with ZipFile("site-professor.zip", "w") as zipf:
    for filename, content in site_files.items():
        zipf.writestr(filename, content)

print("Arquivo site-professor.zip criado com sucesso.")
