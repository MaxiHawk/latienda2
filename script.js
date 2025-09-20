/**
 * Personajes La Tienda - JavaScript
 * Funcionalidades de búsqueda y manejo de personajes
 */

// Base de datos de personajes
const personajes = {
    "Leland Gaunt": "Misterioso propietario de la tienda 'Cosas Necesarias'. Un hombre elegante y persuasivo que siempre parece tener exactamente lo que cada cliente desea.",
    "Alan Pangborn": "Sheriff de Castle Rock, un hombre íntegro y experimentado. Está en una relación con Polly Chalmers y comienza a sospechar de las verdaderas intenciones del nuevo comerciante.",
    "Polly Chalmers": "Propietaria de una tienda de costura y novia de Alan Pangborn. Es una mujer querida en el pueblo que sufre de artritis en las manos.",
    "Brian Rusk": "Un niño de once años, hijo de Cora Rusk. Es uno de los primeros clientes de la tienda de Gaunt y se convierte en parte de sus planes.",
    "Nettie Cobb": "Una mujer mayor y tímida que trabaja como ama de llaves para Polly. Tiene una enemistad histórica con Wilma Jerzyck que se remonta a un incidente pasado.",
    "Wilma Jerzyck": "Una mujer del pueblo conocida por su mal genio y sus disputas con los vecinos, especialmente con Nettie Cobb.",
    "Hugh Priest": "Un hombre con problemas de alcoholismo y un pasado problemático. Se convierte en uno de los peones en los juegos de manipulación de Gaunt.",
    "John 'Ace' Merrill": "Un delincuente local con antecedentes criminales. Gaunt lo utiliza para sus propios fines, aprovechando su naturaleza violenta.",
    "Danforth 'Buster' Keeton": "Funcionario municipal de Castle Rock que tiene serios problemas financieros debido a su adicción a las apuestas.",
    "Norris Ridgewick": "Ayudante del sheriff Alan Pangborn. Un hombre bien intencionado pero a veces ingenuo que se ve envuelto en los eventos extraños del pueblo.",
    "Cora Rusk": "Madre de Brian Rusk, una mujer trabajadora que se preocupa por el comportamiento cada vez más extraño de su hijo.",
    "Sally Ratcliffe": "Esposa de Lester Pratt y una de las clientas de la tienda de Gaunt. Su compra desencadena una serie de eventos problemáticos.",
    "Lester Pratt": "Esposo de Sally Ratcliffe, involucrado en los conflictos que surgen a partir de las manipulaciones de Gaunt.",
    "Reverendo William Rose": "Ministro religioso de Castle Rock que se opone a la influencia de Gaunt en el pueblo.",
    "Myra Evans": "Una mujer del pueblo que se convierte en clienta de la tienda y se ve afectada por las manipulaciones de Gaunt.",
    "Eddie Warburton": "Mecánico del pueblo que se involucra en los eventos desencadenados por las manipulaciones de Gaunt.",
    "Frank Jewett": "Habitante de Castle Rock que participa en los conflictos orquestados por el propietario de la tienda.",
    "George T. Nelson": "Ciudadano del pueblo que se ve afectado por la llegada de Gaunt y su tienda misteriosa.",
    "Don Hemphill": "Residente local que forma parte de la comunidad de Castle Rock durante los eventos de la historia."
};

// Variables globales
let currentSearch = '';
let searchTimeout = null;

/**
 * Función principal de búsqueda de personajes
 */
function buscarPersonaje() {
    const nombre = document.getElementById("nombre").value.trim();
    const descripcionElem = document.getElementById("descripcion");
    const container = document.getElementById("resultContainer");

    // Validación de entrada
    if (nombre.length === 0) {
        mostrarResultado("Por favor, introduce el nombre de un personaje.", "error");
        return;
    }

    // Guardar búsqueda actual para analytics
    currentSearch = nombre;

    // Buscar coincidencia exacta primero
    let descripcion = personajes[nombre];
    let personajeEncontrado = nombre;

    // Si no hay coincidencia exacta, buscar coincidencia parcial
    if (!descripcion) {
        const nombreLower = nombre.toLowerCase();
        for (const [key, value] of Object.entries(personajes)) {
            if (key.toLowerCase().includes(nombreLower) || 
                nombreLower.includes(key.toLowerCase().split(' ')[0].toLowerCase())) {
                descripcion = value;
                personajeEncontrado = key;
                break;
            }
        }
    }

    if (descripcion) {
        mostrarResultado(descripcion, "show");
        // Analytics: registrar búsqueda exitosa
        registrarBusqueda(personajeEncontrado, true);

        // Actualizar campo de búsqueda con el nombre correcto si fue parcial
        if (personajeEncontrado !== nombre) {
            document.getElementById("nombre").value = personajeEncontrado;
        }
    } else {
        const sugerencia = obtenerSugerencia(nombre);
        const mensaje = sugerencia 
            ? `Personaje no encontrado. ¿Quizás buscabas "${sugerencia}"?`
            : "Personaje no encontrado. Verifica el nombre o consulta la lista de personajes disponibles.";

        mostrarResultado(mensaje, "error");
        registrarBusqueda(nombre, false);
    }
}

/**
 * Obtiene una sugerencia basada en similitud de nombres
 */
function obtenerSugerencia(nombre) {
    const nombreLower = nombre.toLowerCase();
    let mejorCoincidencia = null;
    let mejorPuntuacion = 0;

    for (const personaje of Object.keys(personajes)) {
        const personajeLower = personaje.toLowerCase();
        const puntuacion = calcularSimilitud(nombreLower, personajeLower);

        if (puntuacion > mejorPuntuacion && puntuacion > 0.3) {
            mejorPuntuacion = puntuacion;
            mejorCoincidencia = personaje;
        }
    }

    return mejorCoincidencia;
}

/**
 * Calcula similitud entre dos strings usando algoritmo simple
 */
function calcularSimilitud(str1, str2) {
    const longer = str1.length > str2.length ? str1 : str2;
    const shorter = str1.length > str2.length ? str2 : str1;

    if (longer.length === 0) return 1.0;

    const editDistance = calcularDistanciaEdicion(longer, shorter);
    return (longer.length - editDistance) / longer.length;
}

/**
 * Calcula distancia de edición entre dos strings
 */
function calcularDistanciaEdicion(str1, str2) {
    const matrix = [];

    for (let i = 0; i <= str2.length; i++) {
        matrix[i] = [i];
    }

    for (let j = 0; j <= str1.length; j++) {
        matrix[0][j] = j;
    }

    for (let i = 1; i <= str2.length; i++) {
        for (let j = 1; j <= str1.length; j++) {
            if (str2.charAt(i - 1) === str1.charAt(j - 1)) {
                matrix[i][j] = matrix[i - 1][j - 1];
            } else {
                matrix[i][j] = Math.min(
                    matrix[i - 1][j - 1] + 1,
                    matrix[i][j - 1] + 1,
                    matrix[i - 1][j] + 1
                );
            }
        }
    }

    return matrix[str2.length][str1.length];
}

/**
 * Muestra el resultado de la búsqueda
 */
function mostrarResultado(texto, tipo) {
    const descripcionElem = document.getElementById("descripcion");
    const container = document.getElementById("resultContainer");

    // Limpiar clases anteriores
    container.className = "result-container";

    // Aplicar nueva clase después de un breve delay para la animación
    setTimeout(() => {
        descripcionElem.textContent = texto;
        container.className = "result-container " + tipo;
    }, 50);
}

/**
 * Selecciona un personaje de la lista
 */
function seleccionarPersonaje(nombre) {
    const input = document.getElementById("nombre");
    input.value = nombre;
    input.focus();

    // Realizar búsqueda
    buscarPersonaje();

    // Scroll suave hacia el resultado
    setTimeout(() => {
        document.getElementById("resultContainer").scrollIntoView({ 
            behavior: 'smooth', 
            block: 'center' 
        });
    }, 100);
}

/**
 * Crea la grilla de personajes clickeables
 */
function crearGridPersonajes() {
    const grid = document.getElementById("personajesGrid");

    // Ordenar personajes alfabéticamente
    const personajesOrdenados = Object.keys(personajes).sort();

    personajesOrdenados.forEach(nombre => {
        const item = document.createElement("div");
        item.className = "personaje-item";
        item.textContent = nombre;
        item.setAttribute('role', 'button');
        item.setAttribute('tabindex', '0');
        item.setAttribute('aria-label', `Buscar información de ${nombre}`);

        // Event listeners
        item.addEventListener('click', () => seleccionarPersonaje(nombre));
        item.addEventListener('keypress', (event) => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                seleccionarPersonaje(nombre);
            }
        });

        grid.appendChild(item);
    });
}

/**
 * Búsqueda con autocompletado mientras escribe
 */
function configurarAutocompletado() {
    const input = document.getElementById("nombre");

    input.addEventListener('input', function(event) {
        // Cancelar timeout anterior
        if (searchTimeout) {
            clearTimeout(searchTimeout);
        }

        // Configurar nuevo timeout para búsqueda automática
        searchTimeout = setTimeout(() => {
            const valor = event.target.value.trim();
            if (valor.length > 2) {
                // Solo buscar automáticamente si hay más de 2 caracteres
                const sugerencia = obtenerSugerencia(valor);
                if (sugerencia && calcularSimilitud(valor.toLowerCase(), sugerencia.toLowerCase()) > 0.6) {
                    // Auto-completar si la similitud es alta
                    mostrarSugerencia(sugerencia);
                }
            }
        }, 300);
    });
}

/**
 * Muestra una sugerencia de autocompletado
 */
function mostrarSugerencia(sugerencia) {
    const container = document.getElementById("resultContainer");
    const descripcion = document.getElementById("descripcion");

    descripcion.innerHTML = `💡 <strong>Sugerencia:</strong> ¿Buscas "${sugerencia}"? <button onclick="seleccionarPersonaje('${sugerencia}')" style="margin-left: 10px; padding: 5px 10px; background: var(--primary-color); color: white; border: none; border-radius: 5px; cursor: pointer;">Seleccionar</button>`;
    container.className = "result-container";
}

/**
 * Registra búsquedas para analytics (placeholder)
 */
function registrarBusqueda(termino, exitosa) {
    // Aquí se puede integrar con Google Analytics o similar
    console.log(`Búsqueda: "${termino}" - ${exitosa ? 'Exitosa' : 'Sin resultados'}`);

    // Ejemplo de integración con Google Analytics:
    // if (typeof gtag !== 'undefined') {
    //     gtag('event', 'search', {
    //         search_term: termino,
    //         success: exitosa
    //     });
    // }
}

/**
 * Configurar accesibilidad y eventos
 */
function configurarAccesibilidad() {
    // Permitir búsqueda con Enter
    const input = document.getElementById("nombre");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
            buscarPersonaje();
        }
    });

    // Focus management
    input.addEventListener('focus', function() {
        this.select();
    });
}

/**
 * Función de inicialización que se ejecuta cuando carga la página
 */
function inicializarApp() {
    try {
        // Crear grilla de personajes
        crearGridPersonajes();

        // Configurar accesibilidad
        configurarAccesibilidad();

        // Configurar autocompletado
        configurarAutocompletado();

        // Registrar que la app se cargó correctamente
        console.log('App inicializada correctamente');

        // Focus inicial en el campo de búsqueda
        setTimeout(() => {
            document.getElementById("nombre").focus();
        }, 500);

    } catch (error) {
        console.error('Error al inicializar la aplicación:', error);
    }
}

/**
 * Función de limpieza para cerrar recursos
 */
function limpiarRecursos() {
    if (searchTimeout) {
        clearTimeout(searchTimeout);
    }
}

// Event Listeners principales
document.addEventListener('DOMContentLoaded', inicializarApp);
window.addEventListener('beforeunload', limpiarRecursos);

// Exponer funciones globalmente para el HTML
window.buscarPersonaje = buscarPersonaje;
window.seleccionarPersonaje = seleccionarPersonaje;