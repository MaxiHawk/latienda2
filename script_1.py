# 1. Crear index.html
index_html = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personajes de La Tienda - Stephen King | Guía sin Spoilers</title>
    <meta name="description" content="Guía completa de personajes de La Tienda (Needful Things) de Stephen King. Descripciones sin spoilers para recordar cada personaje.">
    <meta name="keywords" content="La Tienda, Stephen King, Needful Things, personajes, Castle Rock, sin spoilers">
    <meta name="author" content="Guía de Personajes">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="">
    <meta property="og:title" content="Personajes de La Tienda - Stephen King">
    <meta property="og:description" content="Guía completa de personajes sin spoilers">
    
    <!-- Twitter -->
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="Personajes de La Tienda - Stephen King">
    <meta property="twitter:description" content="Guía completa de personajes sin spoilers">
    
    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="assets/img/favicon.ico">
    <link rel="apple-touch-icon" sizes="180x180" href="assets/img/apple-touch-icon.png">
    
    <!-- CSS -->
    <link rel="stylesheet" href="assets/css/style.css">
    
    <!-- PWA Manifest -->
    <link rel="manifest" href="manifest.json">
    
    <!-- Theme color -->
    <meta name="theme-color" content="#667eea">
</head>
<body>
    <div class="container">
        <header>
            <h1>La Tienda</h1>
            <p class="subtitle">Guía de personajes - Stephen King</p>
            <p class="description">Encuentra información sobre los personajes sin spoilers para recordar quién es cada uno mientras lees.</p>
        </header>
        
        <main>
            <section class="search-section">
                <div class="search-container">
                    <input type="text" id="nombre" placeholder="Escribe el nombre del personaje..." autocomplete="off" aria-label="Buscar personaje">
                    <button onclick="buscarPersonaje()" aria-label="Buscar personaje">Buscar Personaje</button>
                </div>
                
                <div class="result-container" id="resultContainer">
                    <p class="descripcion" id="descripcion">Escribe el nombre de un personaje para conocer más sobre él sin spoilers.</p>
                </div>
            </section>
            
            <section class="personajes-section">
                <div class="personajes-lista">
                    <h2>Personajes disponibles</h2>
                    <p class="help-text">Haz clic en cualquier nombre para ver su descripción</p>
                    <div class="personajes-grid" id="personajesGrid"></div>
                </div>
            </section>
        </main>
        
        <footer class="creditos">
            <p>Basado en la novela <strong>"La Tienda" (Needful Things)</strong> de Stephen King</p>
            <p>Descripciones libres de spoilers para ayudar a recordar a los personajes</p>
            <p class="copyright">&copy; 2025 - Guía de Personajes</p>
        </footer>
    </div>

    <!-- JavaScript -->
    <script src="assets/js/script.js"></script>
    
    <!-- Analytics placeholder -->
    <script>
        // Aquí puedes agregar Google Analytics u otros scripts de tracking
        // gtag('config', 'GA_MEASUREMENT_ID');
    </script>
</body>
</html>'''

with open("personajes-la-tienda/index.html", "w", encoding="utf-8") as file:
    file.write(index_html)

print("✅ index.html creado")