import requests
import os
import json
import pprint
import pandas as pd
from base64 import b64encode
from dotenv import load_dotenv


"""

Este script Python realiza a autenticação na API do Spotify, 
coleta dados detalhados de um álbum (incluindo suas faixas) e salva as informações em um arquivo CSV. 
Ele utiliza boas práticas de organização, tratamento de erros e uso de variáveis de ambiente para segurança.

"""



# Carrega variáveis do arquivo .env
load_dotenv(dotenv_path='secret.env')  # Certifique-se que o nome está correto

def get_env_variable(var_name):
    """Obtém uma variável de ambiente ou lança um erro se não estiver definida."""
    value = os.getenv(var_name)
    if value is None:
        raise EnvironmentError(f"Variável de ambiente '{var_name}' não está definida.")
    return value

# Obtém o token de acesso do Spotify usando Client Credentials
def get_access_token():
    try:
        client_id = get_env_variable("CLIENT_ID")
        client_secret = get_env_variable("CLIENT_SECRET")
        token_url = get_env_variable("URL_SPOTIFY_TOKEN")

        auth_string = f"{client_id}:{client_secret}"
        auth_bytes = auth_string.encode('utf-8')
        auth_b64 = b64encode(auth_bytes).decode('utf-8')

        headers = {
            'Authorization': f'Basic {auth_b64}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(token_url, headers=headers, data=data)
        response.raise_for_status()  # lança erro para status != 200

        return response.json().get('access_token')

    except requests.RequestException as e:
        raise SystemExit(f"Erro na requisição do token: {e}")
    except Exception as e:
        raise SystemExit(f"Erro ao obter token: {e}")

# Obtém os dados do álbum usando o token de acesso
def get_album_data(access_token, album_id):
    try:
        spotify_url = get_env_variable("URL_SPOTIFY_GERAL")
        url_album = f"{spotify_url}/albums/{album_id}"
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        response = requests.get(url_album, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        raise SystemExit(f"Erro na requisição do álbum: {e}")
    except Exception as e:
        raise SystemExit(f"Erro ao obter dados do álbum: {e}")

# Processa os dados do álbum e extrai informações relevantes
def get_album_data(access_token, album_id, page_size=5):
    try:
        spotify_url = get_env_variable("URL_SPOTIFY_GERAL")
        url_album = f"{spotify_url}/albums/{album_id}"
        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        # Primeiro, obtenha os dados básicos do álbum (sem tracks)
        response = requests.get(url_album, headers=headers, params={'limit': 1})
        response.raise_for_status()
        album_data = response.json()

        # Agora, obtenha todas as faixas paginando de 5 em 5
        tracks_url = f"{url_album}/tracks"
        all_tracks = []
        offset = 0

        while True:
            params = {'limit': page_size, 'offset': offset}
            resp_tracks = requests.get(tracks_url, headers=headers, params=params)
            resp_tracks.raise_for_status()
            tracks_data = resp_tracks.json()
            items = tracks_data.get('items', [])
            all_tracks.extend(items)
            if len(items) < page_size:
                break
            offset += page_size

        # Atualize os dados do álbum com todas as faixas
        album_data['tracks'] = {'items': all_tracks}
        return album_data

    except requests.RequestException as e:
        raise SystemExit(f"Erro na requisição do álbum: {e}")
    except Exception as e:
        raise SystemExit(f"Erro ao obter dados do álbum: {e}")


def save_to_csv(data, filename='album_tracks_spotify.csv'):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f"Dados salvos em: {filename}")
    except Exception as e:
        raise IOError(f"Erro ao salvar CSV: {e}")

#Executa o script principal 
if __name__ == "__main__":
    try:
        album_id = '7xV2TzoaVc0ycW7fwBwAml'  # Substitua pelo ID desejado
        access_token = get_access_token()
        album_data = get_album_data(access_token, album_id) #parametros para obter os dados do álbum
        processed_data = get_album_data(album_data)
        save_to_csv(processed_data)

    except Exception as err:
        print(f"Erro geral: {err}")
