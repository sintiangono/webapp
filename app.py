from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<h1>IC Group - Site Vitrine</h1>
<p><strong>Version :</strong> {{ version }}</p>
<p><a href="{{ odoo_url }}">Odoo</a> | <a href="{{ pgadmin_url }}">pgAdmin</a></p>
"""

@app.route('/')
def home():
    version = "1.0"
    try:
        with open('releases.txt') as f:
            for line in f:
                if line.startswith('version:'):
                    version = line.split(':')[1].strip()
    except:
        pass
    return render_template_string(
        HTML,
        version=version,
        odoo_url=os.getenv('ODOO_URL', 'http://localhost:8069'),
        pgadmin_url=os.getenv('PGADMIN_URL', 'http://localhost:8080')
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
