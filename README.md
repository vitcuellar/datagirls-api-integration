# Visão Geral do Repositório
Repositório para salvar scripts e documentação referente à assunto de integração de dados de API, apresentado na Comunidade de Dados DataGirls.

## Integração API IBGE

Este script Python consulta a API do IBGE para obter informações sobre dois estados brasileiros (Pará e São Paulo), processa os dados em um DataFrame do pandas, salva os resultados em um arquivo CSV e imprime os dados formatados no console.

### Funcionalidades
- Consulta a API do IBGE para obter dados dos estados Pará e São Paulo.
- Converte a resposta JSON em um DataFrame pandas.
- Seleciona e renomeia as colunas relevantes.
- Salva os dados em um arquivo CSV (estados_brasil.csv).
- Exibe os dados formatados no console.

### Dependências
- **requests:** Para realizar requisições HTTP.
- **json:** Para manipulação de dados JSON (não utilizado diretamente, mas pode ser útil).
- **pandas:** Para manipulação e exportação dos dados.
- **pprint:** Para exibir os dados de forma legível no console.


### Boas Práticas Aplicadas
- Uso de bibliotecas especializadas: Utiliza requests para HTTP, pandas para manipulação de dados e pprint para exibição legível.
- Separação de parâmetros: IDs dos estados são definidos em um dicionário, facilitando manutenção e expansão.
- Verificação de status da resposta: O código só processa os dados se a resposta da API for bem-sucedida (status_code == 200).
- Tratamento de erros: Mensagens de erro são exibidas caso a requisição falhe.
- Exportação de dados: Salva o DataFrame em CSV, permitindo reutilização dos dados.
- Renomeação de colunas: Torna os nomes das colunas mais amigáveis e claros.
- Código limpo e comentado: Comentários explicam as principais etapas do processo.


## Integração API Spotify
Este script Python realiza a autenticação na API do Spotify, coleta dados detalhados de um álbum (incluindo suas faixas) e salva as informações em um arquivo CSV. Ele utiliza boas práticas de organização, tratamento de erros e uso de variáveis de ambiente para segurança.

### Estrutura Geral
O código está dividido em funções bem definidas, cada uma responsável por uma tarefa específica, facilitando a manutenção e a reutilização. O fluxo principal está protegido por um bloco if __name__ == "__main__":, garantindo que o script só execute automaticamente quando chamado diretamente.

### Funções Criadas
#### 1. get_env_variable(var_name)
- Descrição: Busca uma variável de ambiente e lança um erro caso ela não esteja definida.
- Boas práticas:
  - Centraliza o acesso às variáveis de ambiente.
  - Fornece mensagens de erro claras.
  - Ajuda a manter informações sensíveis fora do código-fonte.


#### 2. get_access_token()
- Descrição: Realiza a autenticação via Client Credentials com o Spotify e retorna o token de acesso.
- Boas práticas:
  - Utiliza variáveis de ambiente para credenciais.
  - Usa tratamento de exceções para capturar e exibir erros de requisição.
  - Segue o padrão OAuth2 para autenticação segura.

#### 3. get_album_data(access_token, album_id, page_size=5)
- Descrição: Busca os dados básicos do álbum.
- Realiza paginação para coletar todas as faixas do álbum, agrupando de acordo com o parâmetro page_size.
- Retorna um dicionário com os dados completos do álbum e suas faixas.
- Boas práticas:
 - Implementa paginação para evitar sobrecarga de memória e respeitar limites da API.
 - Utiliza tratamento robusto de exceções.
 - Permite customização do tamanho da página de faixas.

#### 4. save_to_csv(data, filename='album_tracks_spotify.csv')
- Descrição: Salva os dados extraídos em um arquivo CSV usando pandas.
- Boas práticas:
 - Utiliza pandas para manipulação eficiente de dados.
 - Permite customização do nome do arquivo.
 - Implementa tratamento de erros para escrita de arquivos.

### Fluxo Principal

- Define o album_id desejado.
- Obtém o token de acesso.
- Busca os dados completos do álbum.
- Salva os dados em CSV.
- Todos os passos estão protegidos por tratamento de exceções, garantindo mensagens claras em caso de falha.
- **Boas Práticas Adotadas**
   - Uso de variáveis de ambiente:
      - Informações sensíveis (tokens, URLs, credenciais) não ficam expostas no código.
- **Tratamento de exceções:**
  - Todas as funções que fazem requisições externas ou operações críticas possuem tratamento de erros, evitando falhas silenciosas.
- **Organização modular:**
  - Cada função tem responsabilidade única, facilitando testes e manutenção.
- **Documentação e comentários:**
  - O código possui comentários explicativos, tornando-o mais compreensível.
**Uso de bibliotecas adequadas:**
  **requests** para HTTP.
  **pandas** para manipulação e exportação de dados.
  **dotenv** para carregar variáveis de ambiente.
    
**Pontos de Atenção**
Há duas funções chamadas get_album_data (uma sobrescreve a outra). Recomenda-se renomear a função de processamento para evitar confusão.
O processamento dos dados para salvar em CSV pode precisar de ajustes, dependendo do formato retornado pela API.



