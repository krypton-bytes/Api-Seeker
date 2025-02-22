# Api-Seeker :shield:
<p align="center">
 <img width="600px" src="https://github.com/krypton-bytes/Api-Seeker/blob/main/assets/logo.jpg" align="center" alt="logo api seeker" />
 <p>Api Seeker began its development on January 22, 2025, and is currently in an early stage. While the application is not yet feature-complete, it is undergoing continuous evolution, with planned updates to integrate new functionalities, enhance performance, and align with industry best practices and security standards for API penetration testing.</p>
</p>

# Repository :floppy_disk: 
Remember to clone the project code:
```bash
git clone
```
Through the contribution you can apply codes such as: :wrench: gitbash such as:
```bash
git status
git add .
git commit -m "message"
git push
```

# Previous installation :package:
Prior to installation you must have `python 3.13.2`

[![Lenguage](https://skillicons.dev/icons?i=python)](https://skillicons.dev)

# Installation :package:
The project depends on two libraries which are:
1.  **Requests**: To make HTTP requests to the API. Install:
```bash
pip install requests
```
2. **Reportlab**: Para generar los informes en PDF. Install:
```bash
pip install reportlab
```

# Project :file_folder:
To initialize the project you need to open a terminal and run the command:
```powershell
python index.py
```
It will ask you to enter the URL of the API to be tested to make your vulnerability report. As indicated below:
```powershell
🔗 ¿Qué API deseas escanear? (Introduce la URL base, ej. https://api.ejemplo.com): https://rickandmortyapi.com/api/character/?page=19
```
The console output will be something similar to the following:
```powershell
🚀 Iniciando análisis de seguridad en la API...

🔍 Probando SQL Injection en: users
✅ OK: No se detectó SQL Injection en https://rickandmortyapi.com/api/character/?page=19/users?id=' OR 1=1 --
✅ OK: No se detectó SQL Injection en https://rickandmortyapi.com/api/character/?page=19/users?id=' UNION SELECT NULL, NULL --
✅ OK: No se detectó SQL Injection en https://rickandmortyapi.com/api/character/?page=19/users?id='; DROP TABLE users --
```
At the end of the scan, it will ask you if you want to generate a report in PDF and will give you two options yes or no (y/n)
```powershell
✅ Análisis completado.

📄 ¿Deseas generar un informe en PDF con los resultados? (y/n): y

📄 Generando informe en PDF...
✅ Informe PDF generado con éxito: api_security_report.pdf
```

# Authors :busts_in_silhouette:
- [@krypton-bytes](https://github.com/krypton-bytes)

# Contributing :wrench: 

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

# Remember to say thank you :heart:

You can take up this project as long as:
- Give thanks :blue_heart: 
- Do not use it for malicious purposes :lock:

<a href='' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://cdn.ko-fi.com/cdn/kofi1.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
