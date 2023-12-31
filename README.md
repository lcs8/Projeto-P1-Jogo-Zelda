# Projeto-P1-Jogo-Zelda
O Zelda Arcade é um jogo 2D, inspirado em The Legend of Zelda uma série de jogos eletrônicos da Nintendo criada em 1986 por Shigeru Miyamoto e Takashi Tezuka. É centrado em jogos eletrônicos de ação e aventura e alguns elementos de RPG. desenvolvido em python utilizando a biblioteca pygame, com a finalidade de ser um projeto a ser apresentado na cadeira de P1SI.2023.1 do curso de Sistema de Informação da UFPE (Universidade Federal de Pernambuco). Projeto esse desenvolvido utilizando a implementação POO (Programação Orientada a Objeto). A intenção do jogo é ser do tipo coletável, onde o objetivo de Link é coletar o máximo de rupee possíveis, em um determinado intervalo de tempo pré estabelecido, podendo coletar vidas para aumentá-la ajudando-a na possível colisão com seus inimigos.Para rodar o jogo, realize o download do arquivo nesse repositório, para ser executado é necessário que usuário tenha instalado no seu computador uma versão do python3 e instalado a biblioteca Pygame.Pygame é uma biblioteca de jogos multiplataforma (independente de sistema operacional) feita para ser utilizada em conjunto com a linguagem de programação Python. Para instalar no seu computador execute o comando **pip install pygame** no terminal do seu computador.


![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/Link1.jpg)
# Membros
- Lucas Occenstein (lao2)
- Heriberto Guimarães(hdgs)
- Gabriel Mendonça(gmva)
- Luiz Carlos(lcs8)

# Elementos do Jogo
## Link
![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/Link.png)
### Personagem principal controlado pelo jogador, utilizando as seguintes teclas:
- w : Faz com que o personagem ande para cima dentro do ambiente do jogo.
- s : Faz com que o personagem ande para baixo dentro do ambiente do jogo.
- a : Faz com que o personagem ande para o lado esquerdo dentro do ambiente do jogo.
- d : Faz com que o personagem ande para o lado direito dentro do ambiente do jogo.
## Rupees
### Elementos coletáveis objetivo de Link, cada rupee tem seu valor de coleta:
![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/red_rupee.png) Ruppe vermelho vale 10 ponto
![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/blue_rupee.png) Rupee azul vale 5 pontos

![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/yellow_rupee.png) Rupee amarelo vale 1 pontos
## Arrow
### Elemento coletável por Link:
![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/Arrow.png) Elemento inserido para futuras atualizações
## Health
### Elemento coletável por Link com objetivo de aumentar seu número de vida:
![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/Hearth.png) Elemento aumenta 1 vida de Link
## Enemy
### Personagens responsáveis por retirar vidas de Link a cada vez que Link toca em um deles:
![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/enemy1.png) Retira 1 vida de Link

![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/enemy2.png) Retira 2 vidas de Link

![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/enemy3.png) Retira 3 vidas de Link
# Organização do código
## Fluxograma
![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/sprits/Fluxograma_page-0001.jpg)
- Sprits : Pasta onde está todas as imagens e mùsicas contidas no código do jogo e na construção desse arquivo.
- Classe Player : Responsavel por carregar o objeto do personagem Link, bem como seu método de movimentação dentro do jogo.
- Classe Item : Responsavel por carregar o restante dos itens do jogo, bem como seus métodos de coordenadas dentro do jogo.
- Main : Responsavel pelo o que pode ser chamado de estrutura geral interativa do jogo, contem o loop principal do jogo e instancia as classes. Também armazena as colisões, pontuaçao, tempo e score do jogo.
### Bibliotecas e Ferramentas
- *Pygame* : Pygame é um conjunto de módulos python para desenvolvimento de jogos, essencial para o desenvolvimento do projeto.
- *Os* : Em Python é uma biblioteca padrão muito útil quando se trata de interagir com o sistema operacional. utilizamos para carregar as sprits(imagens e músicas) do jogo.
- *Random* : Essa biblioteca oferece métodos para gerar números aleatórios, embaralhar listas e sortear item de sequências. utilizamos na obtenção de aleatoriedade nos itens do jogo.
- *Visual Studio Code* : Editor de código-fonte e inclui suporte para depuração, muito útil na hora de implementar o código ajudando a entender o passo a passo do mesmo.
# Divisão de Trabalho
Lucas Occenstein - Responsável pelo sistema de movimento;
Heriberto Guimarães - Responsável pela idealização, sistema de mundo e design gráfico;
Gabriel Mendonça - Responsável pelo sistema de sons e música;
Luiz Carlos - Responsável pelo sistema de itens e coletáveis.
# Conceitos
Dentro do projeto foi passado tanto conceitos básicos vistos no inicio da disciplina como estrutura de decisão e estrutura de repetição bem como conceitos de listas, tuplas. Analisando o código dentro dos conceitos visto não foi utilizado dicionario mas também foi utilizado sistematicamente o conceito de funções e o principal que era fundamental para o projeto, as noções iniciais de POO (Programação Orientada a Objeto).
# Desafios Erros e Lições Aprendidas
### Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
Um dos maiores erros cometidos ao desenvolver esse projeto foi o subestimar o entendimento da POO, para o grupo foi e esta sendo um processo desafiador.
### Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
O maior desafio continua sendo entende o funcionamento do POO, que aparentemente se bem utilizada facilita o desenvolvimento dos código, isso pode ser uma premissa verdadeira, mas entender POO tem uma curva de aprendizado maior.
### Quais as lições aprendidas durante o projeto?
O conceito de desenvolver algo em conjunto, entender as ideias individuais e como essas ideias são concatenadas no produto final e as lições técnicas aprendidas ao longo do desenvolvimento do projeto.
# Capturas de Tela
![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/ScreenGame/screen1.jpg)

![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/ScreenGame/screen2.jpg)

![](https://github.com/lcs8/Projeto-P1-Jogo-Zelda/blob/main/ScreenGame/screen3.jpg)






