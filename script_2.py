# 2. Crear style.css
style_css = '''/* ==========================================================================
   Personajes La Tienda - Estilos CSS
   ========================================================================== */

/* Variables CSS */
:root {
    --primary-color: #667eea;
    --secondary-color: #764ba2;
    --text-dark: #2c3e50;
    --text-light: #7f8c8d;
    --background-light: #f8f9fa;
    --success-color: #28a745;
    --warning-color: #ffc107;
    --border-color: #e0e6ed;
    --shadow-light: 0 2px 10px rgba(0,0,0,0.1);
    --shadow-medium: 0 4px 15px rgba(102, 126, 234, 0.3);
    --shadow-heavy: 0 10px 30px rgba(0,0,0,0.2);
    --border-radius: 15px;
    --transition: all 0.3s ease;
}

/* Reset y base */
* {
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    margin: 0;
    padding: 20px;
    min-height: 100vh;
    line-height: 1.6;
}

/* Contenedor principal */
.container {
    max-width: 800px;
    margin: 0 auto;
    background: #fff;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-heavy);
    padding: 40px;
    animation: fadeIn 0.8s ease-in;
}

@keyframes fadeIn {
    from { 
        opacity: 0; 
        transform: translateY(20px); 
    }
    to { 
        opacity: 1; 
        transform: translateY(0); 
    }
}

/* Header */
header {
    text-align: center;
    margin-bottom: 40px;
}

h1 {
    color: var(--text-dark);
    margin-bottom: 10px;
    font-size: 3em;
    font-weight: 300;
    margin-top: 0;
}

.subtitle {
    color: var(--text-light);
    margin-bottom: 15px;
    font-style: italic;
    font-size: 1.2em;
}

.description {
    color: var(--text-light);
    margin-bottom: 0;
    max-width: 500px;
    margin-left: auto;
    margin-right: auto;
}

/* Sección de búsqueda */
.search-section {
    margin-bottom: 40px;
}

.search-container {
    margin-bottom: 30px;
}

input[type="text"] {
    width: 100%;
    padding: 15px 20px;
    font-size: 16px;
    border: 2px solid var(--border-color);
    border-radius: 25px;
    outline: none;
    transition: var(--transition);
    box-shadow: var(--shadow-light);
}

input[type="text"]:focus {
    border-color: var(--primary-color);
    box-shadow: var(--shadow-medium);
}

button {
    background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
    color: white;
    border: none;
    padding: 15px 30px;
    font-size: 16px;
    border-radius: 25px;
    cursor: pointer;
    transition: var(--transition);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    width: 100%;
    margin-top: 10px;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
}

button:active {
    transform: translateY(0);
}

button:focus {
    outline: 2px solid var(--primary-color);
    outline-offset: 2px;
}

/* Contenedor de resultados */
.result-container {
    margin-top: 30px;
    padding: 25px;
    border-radius: var(--border-radius);
    background: var(--background-light);
    border-left: 5px solid var(--primary-color);
    min-height: 80px;
    display: flex;
    align-items: center;
    transition: var(--transition);
}

.result-container.show {
    background: #e8f5e8;
    border-left-color: var(--success-color);
    animation: slideIn 0.5s ease-out;
}

.result-container.error {
    background: #fff3cd;
    border-left-color: var(--warning-color);
    animation: shake 0.5s ease-in-out;
}

@keyframes slideIn {
    from { 
        opacity: 0; 
        transform: translateX(-20px); 
    }
    to { 
        opacity: 1; 
        transform: translateX(0); 
    }
}

@keyframes shake {
    0%, 20%, 50%, 80%, 100% { transform: translateX(0); }
    10% { transform: translateX(-5px); }
    30% { transform: translateX(5px); }
    60% { transform: translateX(-3px); }
    90% { transform: translateX(3px); }
}

.descripcion {
    color: var(--text-dark);
    font-size: 16px;
    line-height: 1.6;
    margin: 0;
}

/* Sección de personajes */
.personajes-section {
    margin-bottom: 40px;
}

.personajes-lista {
    padding: 30px;
    background: var(--background-light);
    border-radius: var(--border-radius);
}

.personajes-lista h2 {
    color: var(--text-dark);
    margin-bottom: 15px;
    text-align: center;
    font-size: 1.8em;
    margin-top: 0;
}

.help-text {
    text-align: center;
    color: var(--text-light);
    margin-bottom: 25px;
    font-style: italic;
}

.personajes-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 15px;
    margin-top: 20px;
}

.personaje-item {
    background: white;
    padding: 15px 20px;
    border-radius: 10px;
    cursor: pointer;
    transition: var(--transition);
    text-align: center;
    border: 2px solid transparent;
    font-weight: 500;
    box-shadow: var(--shadow-light);
}

.personaje-item:hover {
    background: var(--primary-color);
    color: white;
    transform: translateY(-3px);
    box-shadow: var(--shadow-medium);
    border-color: var(--primary-color);
}

.personaje-item:focus {
    outline: 2px solid var(--primary-color);
    outline-offset: 2px;
}

/* Footer */
footer.creditos {
    text-align: center;
    color: var(--text-light);
    font-size: 14px;
    margin-top: 40px;
    padding-top: 30px;
    border-top: 2px solid #ecf0f1;
}

footer.creditos p {
    margin: 10px 0;
}

footer.creditos .copyright {
    font-size: 12px;
    margin-top: 20px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .container {
        margin: 10px;
        padding: 25px;
    }
    
    h1 {
        font-size: 2.5em;
    }
    
    .personajes-grid {
        grid-template-columns: 1fr;
        gap: 10px;
    }
    
    .personaje-item {
        padding: 12px 15px;
    }
    
    input[type="text"], button {
        font-size: 16px; /* Evita zoom en iOS */
    }
}

@media (max-width: 480px) {
    body {
        padding: 10px;
    }
    
    .container {
        padding: 20px;
    }
    
    h1 {
        font-size: 2em;
    }
    
    .subtitle {
        font-size: 1.1em;
    }
    
    .description {
        font-size: 14px;
    }
}

/* Estados de accesibilidad */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* Modo oscuro */
@media (prefers-color-scheme: dark) {
    :root {
        --text-dark: #ecf0f1;
        --text-light: #bdc3c7;
        --background-light: #34495e;
        --border-color: #5a6c7d;
    }
    
    .container {
        background: #2c3e50;
        color: var(--text-dark);
    }
    
    .personaje-item {
        background: #34495e;
        color: var(--text-dark);
    }
    
    input[type="text"] {
        background: #34495e;
        color: var(--text-dark);
        border-color: var(--border-color);
    }
    
    input[type="text"]::placeholder {
        color: var(--text-light);
    }
}

/* Print styles */
@media print {
    body {
        background: none;
        color: black;
    }
    
    .container {
        box-shadow: none;
        border: 1px solid #ccc;
    }
    
    button {
        display: none;
    }
    
    .search-container {
        display: none;
    }
}'''

with open("personajes-la-tienda/assets/css/style.css", "w", encoding="utf-8") as file:
    file.write(style_css)

print("✅ style.css creado")