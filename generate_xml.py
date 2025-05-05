# generate_xml.py

def generar_xml():
    with open("weather.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<weather>\n')
        f.write('  <location>Madrid</location>\n')
        f.write('  <temperature>22</temperature>\n')
        f.write('</weather>\n')

if __name__ == "__main__":
    generar_xml()
