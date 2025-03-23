import requests
from bs4 import BeautifulSoup
import time

# url do site escolhido para o scraping
url = "https://g1.globo.com"

# envia solicitação HTTP GET para o site
response = requests.get(url)

# verifica a solicitação
if response.status_code == 200:
    # utiliza o BeautifulSoup para analisar o conteudo HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # encontra todos os titulos de noticias
    titles = soup.find_all('a', class_='feed-post-link gui-color-primary gui-color-hover')

    # criação de arquivo HTML
    with open("noticias.html", "w", encoding="utf-8") as file:
        file.write("<html><head><title>Notícias G1</title></head>\n")

        #style
        file.write("""
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                h1 { color: #003366 }
                ul { list-style-type: none; padding: 0; }
                li { margin: 10px 0; }
                a { text-decoration: none; color: #0066cc; }
                a:hover { color: #003366; }
            </style>\n                       
            """)

        file.write("<body>\n<h1>Últimas Notícias do G1</h1>\n")
        file.write("<ul>\n")

        # exibe os titulos das noticias
        for title in titles:
            text = title.get_text() # texto do titulo
            link = title.get('href') # link da noticia

            if link:
                file.write(f'<li><a href="{link}">{text}</a></li>\n')
            else:
                file.write(f'<li>{text} (Link não disponível)</li>\n')

            time.sleep(1) # pausa de 1s para evitar sobrecarga

            # fim do html
            file.write("</ul>\n")
            file.write("</body></html>\n")

        print("Arquivo HTML gerado com sucesso!")

else:
    print(f"Erro ao acessar o site: {response.status_code}")