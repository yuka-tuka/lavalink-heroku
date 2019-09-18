![lavalink](https://i.imgur.com/TTfLd3k.png)
# Lavalink
**Lavalink** na **Heroku**, em poucos passos.


### Heroku

### 1° Clique no botão **[Deploy to heroku]** abaixo para instalar.

  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/yuka-tuka/lavalink-heroku)

###  2° Após clicar, aparecerá uma janela semelhante

![Deploy](https://i.imgur.com/SEDc43Z.png)

1. Digite o **nome** do seu aplicativo.
2. Selecione o **local ** do seu servidor que você irá querer.
3. Clique no botão **Deploy app**

### 3° Após clicar, aparecerá uma janela semelhante, espere um pouco a criação do aplicativo, a **env**, entre outras coisas.

 ![Deploy](https://i.imgur.com/Tj48u4z.png)

### 4° Depois de realizar os processos irá aparecer uma janela com "caixinhas" marcada em verde caso todas tiver **Verde** a instalação foi realizada com sucesso, após clique em **Manage app**

![Deploy](https://i.imgur.com/rpFg8NZ.png)
### 5° Para checar se nosso lavalink está OK, iremos em 2 locais.

   ![Deploy](https://i.imgur.com/ejT8JRs.png)

 1. Primeiro em **More** e depois em **View logs** aqui irá aparecer umas informações ou algum erro caso tiver.

   ![Deploy](https://i.imgur.com/0UP6PdV.png)

2. Depois iremos em **Settings** e desca um pouco para baixo que você irá encontrar um **link**.

   ![Deploy](https://i.imgur.com/dcmCg6p.png)
3. Basta clicar nele e ir para esse **url**, caso a página apresente um **erro 401** que dizer que o servidor lavalink está 100% operante.
  
  ![Deploy](https://i.imgur.com/Qd6k2Qa.png)


# Observação
1. Caso você não tenha devido a sua porta na **env** ela será **80** (recomendo que sempre deixe em 80 pra evitar problemas)
2.  Caso você não tenha devido a sua senha na **env** ela será **youshallnotpass**
3. Para deixar o servidor lavalink **24/7**, você precisa criar uma conta no serviço [UptimeRobot](https://uptimerobot.com/ "UptimeRobot") e fazer uma solicitação HTTP para o seu aplicativo a cada **5 a 10 minutos**. Por exemplo, se seu aplicativo for nomeado **tutorial-lavalink**, faça uma solicitação HTTP para [https://tutorial-lavalink.herokuapp.com](https://tutorial-lavalink.herokuapp.com)




# Exemplos

## Python is best
### discord.py

- [x] **Wavelink** | **[link do repositório](https://github.com/EvieePy/Wavelink)**
```python
async def initiate_nodes(self):
    nodes = {"MAIN": 
        {
            "host": "tutorial-lavalink.herokuapp.com",
            "port": 80,
            "rest_url": "http://tutorial-lavalink.herokuapp.com",
            "password": "youshallnotpass",
            "identifier": "MAIN",
            "region": "eu"
        }
    }

    for n in nodes.values():
        # ...
```
- [x] **Lavalink.py** | **[link do repositório](https://github.com/Devoxin/Lavalink.py)**
```python
async def initiate_nodes(self):
    self.bot.lavalink = lavalink.Client(
        self.bot.user.id
    )
    
    self.bot.lavalink.add_node(
        "tutorial-lavalink.herokuapp.com", 
        80, 
        "youshallnotpass", 
        "eu", 
        "default-node"
    )  # Host, Port, Password, Region, Name
    # ...
```
