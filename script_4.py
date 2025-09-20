# 4. Crear robots.txt
robots_txt = '''# Robots.txt para Personajes La Tienda
User-agent: *
Allow: /

# Sitemap
Sitemap: https://tudominio.com/sitemap.xml

# Crawl-delay para ser respetuoso con los servidores
Crawl-delay: 1'''

with open("personajes-la-tienda/robots.txt", "w", encoding="utf-8") as file:
    file.write(robots_txt)

# 5. Crear .htaccess para Apache
htaccess = '''# .htaccess para Personajes La Tienda
# Configuración de servidor Apache

# Habilitar compresión GZIP
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
</IfModule>

# Cache para archivos estáticos
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/gif "access plus 1 year"
    ExpiresByType image/ico "access plus 1 year"
    ExpiresByType image/x-icon "access plus 1 year"
</IfModule>

# Headers de seguridad
<IfModule mod_headers.c>
    Header always set X-Content-Type-Options nosniff
    Header always set X-Frame-Options DENY
    Header always set X-XSS-Protection "1; mode=block"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Permissions-Policy "camera=(), microphone=(), geolocation=()"
</IfModule>

# Redirección HTTPS (descomenta si tienes SSL)
# RewriteEngine On
# RewriteCond %{HTTPS} off
# RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# Error pages personalizadas
ErrorDocument 404 /404.html

# Desactivar listado de directorios
Options -Indexes

# Proteger archivos sensibles
<Files ~ "^\\.(htaccess|htpasswd)$">
    Order allow,deny
    Deny from all
</Files>'''

with open("personajes-la-tienda/.htaccess", "w", encoding="utf-8") as file:
    file.write(htaccess)

# 6. Crear manifest.json para PWA
manifest_json = '''{
    "name": "Personajes de La Tienda - Stephen King",
    "short_name": "La Tienda",
    "description": "Guía completa de personajes de La Tienda de Stephen King sin spoilers",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#667eea",
    "theme_color": "#667eea",
    "orientation": "portrait-primary",
    "categories": ["books", "reference", "education"],
    "lang": "es-ES",
    "icons": [
        {
            "src": "assets/img/icon-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "assets/img/icon-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ]
}'''

with open("personajes-la-tienda/manifest.json", "w", encoding="utf-8") as file:
    file.write(manifest_json)

# 7. Crear sitemap.xml
sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://tudominio.com/</loc>
        <lastmod>2025-09-20</lastmod>
        <changefreq>monthly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>'''

with open("personajes-la-tienda/sitemap.xml", "w", encoding="utf-8") as file:
    file.write(sitemap_xml)

print("✅ robots.txt creado")
print("✅ .htaccess creado")
print("✅ manifest.json creado")
print("✅ sitemap.xml creado")