import os
from app import create_app

# Ortam değişkenlerinden konfigürasyon modu belirleyin
config_mode = os.environ.get('FLASK_CONFIG_MODE', 'development')

# Uygulama oluşturulurken konfigürasyonu geçirme
app = create_app()

if __name__ == "__main__":
    # Eğer geliştirme modundaysa debug açık olur
    app.run(debug=(config_mode == 'development'))
