import requests
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import black

class APISecurityExplorer:
    def __init__(self, base_url):
        self.base_url = base_url
        self.report_data = {
            "SQL Injection": [],
            "XSS": [],
            "Access Control": [],
            "Input Validation": []
        }

    def test_sql_injection(self, endpoint):
        """Prueba de inyección SQL en un parámetro de la API"""
        print(f"\n🔍 Probando SQL Injection en: {endpoint}")
        payloads = ["' OR 1=1 --", "' UNION SELECT NULL, NULL --", "'; DROP TABLE users --"]
        for payload in payloads:
            url = f"{self.base_url}/{endpoint}?id={payload}"
            response = requests.get(url)

            if "error" in response.text or "SQL" in response.text:
                print(f"⚠️ ALERTA: Posible SQL Injection en {url}")
                self.report_data["SQL Injection"].append(("⚠️ ALERTA", url, f"Payload: {payload}"))
            else:
                print(f"✅ OK: No se detectó SQL Injection en {url}")
                self.report_data["SQL Injection"].append(("✅ OK", url, f"Payload: {payload}"))

    def test_xss(self, endpoint):
        """Prueba de inyección XSS en un parámetro de la API"""
        print(f"\n🔍 Probando XSS en: {endpoint}")
        payload = "<script>alert('XSS')</script>"
        url = f"{self.base_url}/{endpoint}?input={payload}"
        response = requests.get(url)

        if payload in response.text:
            print(f"⚠️ ALERTA: Posible vulnerabilidad XSS en {url}")
            self.report_data["XSS"].append(("⚠️ ALERTA", url, "XSS detectado"))
        else:
            print(f"✅ OK: No se detectó XSS en {url}")
            self.report_data["XSS"].append(("✅ OK", url, "No vulnerable"))

    def test_unauthorized_access(self, endpoint):
        """Verifica si un endpoint requiere autenticación"""
        print(f"\n🔍 Probando control de acceso en: {endpoint}")
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)

        if response.status_code == 401:
            print(f"✅ OK: El acceso está restringido correctamente en {url}")
            self.report_data["Access Control"].append(("✅ OK", url, "Acceso restringido correctamente"))
        elif response.status_code == 200:
            print(f"⚠️ ALERTA: Endpoint accesible sin autenticación en {url}")
            self.report_data["Access Control"].append(("⚠️ ALERTA", url, "Acceso sin autenticación"))
        else:
            print(f"ℹ️ INFO: Respuesta inesperada en {url}: {response.status_code}")
            self.report_data["Access Control"].append(("ℹ️ INFO", url, f"Respuesta inesperada: {response.status_code}"))

    def test_input_validation(self, endpoint):
        """Prueba de validación de entradas"""
        print(f"\n🔍 Probando validación de entradas en: {endpoint}")
        payload = "' OR 1=1 --"
        url = f"{self.base_url}/{endpoint}?user_id={payload}"
        response = requests.get(url)

        if "error" in response.text:
            print(f"⚠️ ALERTA: Falta validación de entrada en {url}")
            self.report_data["Input Validation"].append(("⚠️ ALERTA", url, "Falta validación de entrada"))
        else:
            print(f"✅ OK: La validación de entrada es correcta en {url}")
            self.report_data["Input Validation"].append(("✅ OK", url, "Validación correcta"))

    def scan_api(self):
        """Escanea la API"""
        endpoints = ["users", "products", "search"]
        for endpoint in endpoints:
            self.test_sql_injection(endpoint)
            self.test_xss(endpoint)
            self.test_unauthorized_access(endpoint)
            self.test_input_validation(endpoint)

    def generate_pdf_report(self, filename="api_security_report.pdf"):
        """Genera un informe en PDF con los resultados de las pruebas utilizando caracteres Unicode"""
        print("\n📄 Generando informe en PDF...")
        c = canvas.Canvas(filename, pagesize=letter)
        c.setFont("Helvetica-Bold", 16)
        width, height = letter

        margin_x = 50
        y_position = height - 50
        c.drawString(margin_x, y_position, "📜 Informe de Seguridad de la API")

        # Registrar y establecer la fuente para Segoe UI Emoji
        font_path = "C:/Windows/Fonts/seguiemj.ttf"
        if os.path.exists(font_path):
            # Registrar la fuente con el nombre exacto
            pdfmetrics.registerFont(TTFont('Segoe UI Emoji Normal', font_path))  # Usar el nombre exacto
            c.setFont("Segoe UI Emoji Normal", 12)
        else:
            print("❌ Fuente no encontrada. Usando fuente predeterminada.")
            c.setFont("Helvetica", 12)

        y_position -= 30

        for category, results in self.report_data.items():
            c.setFont("Helvetica-Bold", 14)
            c.drawString(margin_x, y_position, f"🔹 {category}")
            y_position -= 20

            for result in results:
                status, url, details = result
                c.setFont("Helvetica", 10)
                # Mostrar el texto con íconos usando Segoe UI Emoji para los íconos
                if "⚠️" in status or "✅" in status or "🔍" in status:
                    c.setFillColorRGB(0, 0, 0)  # Establecer color negro para los emojis
                    c.setFont("Segoe UI Emoji Normal", 12)  # Usar la fuente registrada
                else:
                    c.setFont("Helvetica", 10)  # Restablecer a Helvetica para el texto
                c.drawString(margin_x, y_position, f"{status} {url} - {details}")
                y_position -= 15

                if y_position < 50:  # Nueva página si se acaba el margen
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_position = height - 50

            y_position -= 10

        c.save()
        print(f"✅ Informe PDF generado con éxito: {filename}")

def main():
    base_url = input("🔗 ¿Qué API deseas escanear? (Introduce la URL base, ej. https://api.ejemplo.com): ")

    if not base_url:
        print("❌ No se ha proporcionado una URL válida.")
        return

    explorer = APISecurityExplorer(base_url)

    print("\n🚀 Iniciando análisis de seguridad en la API...")
    explorer.scan_api()
    print("\n✅ Análisis completado.")

    generar_pdf = input("\n📄 ¿Deseas generar un informe en PDF con los resultados? (y/n): ").strip().lower()
    if generar_pdf == "y":
        explorer.generate_pdf_report()

if __name__ == "__main__":
    main()
