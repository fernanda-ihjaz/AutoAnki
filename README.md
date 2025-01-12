# AutoAnki

O AutoAnki é um script em Python que interage com a API Anki Connect para criar decks e adicionar cards no Anki de forma automatizada.

## Funcionalidades

- **createDeck**: criação de deck
- **saveDeckConfig**: configuração do deck
    
    Permite configurar as preferências do deck, como número máximo de cards a serem revisados por dia e outras opções.
- **addNote**: Adição de Cards
    
    Lê informações de um arquivo JSON e adiciona cards no deck especificado.
    O script pode ser configurado para permitir ou bloquear a adição de cards duplicados.

## Pré-requisitos

Antes de rodar o script, você precisará:

1. **Instalar o Anki**: Baixe e instale o [Anki](https://apps.ankiweb.net/).
2. **Instalar Anki Connect**: O Anki Connect é um plugin para o Anki que permite interação com a API. Você pode instalar o plugin através do próprio Anki:
   - Vá até **Ferramentas** > **Complementos** > **Obter Complementos**.
   - Digite o código de instalação do Anki Connect: `2055492159`.
   - Reinicie o Anki após a instalação.

## Como Usar

1. **Configure o seu arquivo JSON ou CSV**:
   - Prepare um arquivo com os dados que você deseja adicionar ao Anki. Um exemplo de arquivo pode ser o `eng-words.json`:
     ```json
     [
         {"front": "hello", "back": "olá"},
         {"front": "goodbye", "back": "adeus"}
     ]
     ```
   
2. **Configure o Script**
    - **Dê um nome ao seu deck ou coloque o nome de um deck existente.** O script não criará decks com nomes duplicados e precisa dessa informação para mudar as consigurações padrões do deck e adicionar os cards que forem criados nele.
        ```python
            deck_name = 'Nome do Deck'
        ```
    - **Adicione o nome do arquivo com os dados dos cards.**
        ```python
            with open('arquivo.json', 'r') as file:
        ```
    - **Configurações do deck**. "perDay" define quantos cards podem ser criados no dia. Altere de acordo com o nùmero de registros no json.
        ```python
            invoke('saveDeckConfig', config={
                "new": {
                "perDay": 20,}
                })
        ```

3. **Execute o Script**

4. **Visualize o Deck no Anki**:

    Após a execução do script, você poderá visualizar o novo deck no Anki, com os cards que foram adicionados.


