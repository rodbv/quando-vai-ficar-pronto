# ROTEIRO: Quando Vai Ficar Pronto?

## Mensagem central
Prazo sem probabilidade parece resposta, mas ainda é chute.

A palestra deve mostrar que previsibilidade melhora quando a conversa sai de estimativa pontual e passa para risco explícito, usando dados reais do fluxo.

## Objetivo
- Mostrar por que data única costuma falhar.
- Explicar a diferença entre estimar e prever.
- Apresentar um caminho simples para responder prazo com confiança.
- Fechar com ações práticas que o time pode aplicar no dia seguinte.

## Tom
- Direto, didático e sem jargão desnecessário.
- Mais gestão de risco do que evangelização de método.
- Matemática só quando ela realmente ajuda a decisão.

## Estrutura sugerida

### 1. A pergunta que sempre volta
Ideia principal:
A conversa começa com a pergunta "quando vai ficar pronto?" e quase sempre termina em uma data frágil demais.

Pontos que precisam aparecer:
- A pergunta é legítima.
- O problema não está em perguntar prazo.
- O problema está em responder com precisão falsa.

Mensagem de palco:
Não é uma palestra sobre estimar melhor. É uma palestra sobre responder melhor.

### 2. Variabilidade é normal, não exceção
Ideia principal:
Mesmo quando o trabalho parece parecido, o resultado varia.

1. O Gancho (A Armadilha do "Eu Acho")

Conte exatamente a história qu  e você propôs: “A gente junta o time, chuta margens de erro, imagina paralelismo, e chega num 'talvez 5 semanas'. A liderança repassa pra frente. De repente, chega o email com a data de lançamento gravada na pedra.”

A pergunta de transição: "Como sair dessa armadilha onde um palpite vira um compromisso inegociável?"

2. A Virada (Estimativa vs. Previsão)

Pule direto para o conceito. Não faça a história inteira do trânsito com gráficos, use-a apenas como uma micro-analogia de 15 segundos para definir os termos:

"A saída é parar de fazer Estimativas e começar a fazer Previsões (Forecasts). * Estimativa é um número único: 'Chego no trabalho em 30 minutos'.

Previsão é um intervalo com probabilidade: 'Tenho 90% de chance de chegar em até 45 minutos'."

O "Aha! Moment": Para fazer previsões, não precisamos de bolas de cristal, Planning Poker ou horas em reunião. Precisamos apenas de dois dados que o sistema de vocês já tem: Data de Início e Data de Fim.

3. O "How To" Matemático (A Prova)

Para 1 item: Mostre o Scatterplot (Gráfico de Dispersão) de Lead Time. Mostre como traçar a linha do p85 e responder: "Qualquer item que entra aqui tem 85% de chance de sair em X dias".

Para N itens: Apresente a Simulação de Monte Carlo. Explique rapidamente que é o computador jogando milhares de cenários possíveis com o seu Throughput histórico para gerar uma curva de probabilidade. (Aqui você brilha com a solução do problema das "5 semanas").

4. A Gestão do Dia a Dia (Ação Prática)

Como ser mais previsível e não deixar a cauda longa te engolir?

Fale sobre parar de gerenciar quem está ocupado e começar a gerenciar o trabalho no fluxo.

Stop Starting, Start Finishing: O poder dos limites de WIP.

Item Age: A métrica mais importante do dia a dia (se um item está envelhecendo, aja sobre ele antes que ele fure o seu p85).

A Base (Opcional, se o tempo permitir): Uma pincelada na Lei de Little para embasar matematicamente por que WIP alto destrói a previsibilidade.

5. O Gran Finale (O Código)

Termine empoderando a plateia: "Tudo isso não é teoria, é matemática pura." E solte o link (ou QR Code) para o seu Jupyter Notebook com as simulações em Python para que eles mesmos possam plugar seus dados.

Esse formato é letal. Ele identifica uma dor corporativa universal, muda a perspectiva (de palpite para probabilidade), prova matematicamente como fazer, ensina como gerenciar e entrega a ferramenta pronta.

Considerando que a sua plateia é mista (devs, designers, líderes), você pretende mostrar o código rodando ao vivo rapidamente ou vai apenas focar nos gráficos gerados por ele durante a explicação do Monte Carlo?
- O sistema já carrega variabilidade antes de qualquer planejamento.

Mensagem de palco:
Se o sistema varia, a previsão precisa conversar com essa variação.

### 3. Onde a conta linear seduz
Ideia principal:
Times costumam transformar backlog em data com uma regra de três elegante demais.

Pontos que precisam aparecer:
- Story points e velocity ajudam planejamento interno.
- O erro está em promover essa conta a previsão confiável para negócio.
- A conta parece objetiva, mas esconde incerteza.

Mensagem de palco:
Planejamento e previsão não são a mesma coisa.

### 4. Estimativa nao e previsao
Ideia principal:
Estimativa é um valor. Previsão é uma faixa com chance associada.

Pontos que precisam aparecer:
- Uma data sozinha não informa risco.
- Centro da distribuição normalmente equivale a algo próximo de p50.
- p50 para compromisso significa aceitar falhar com frequência alta.

Mensagem de palco:
Uma resposta melhor não é "10 de junho". É "até 10 de junho com 85% de confiança".

### 5. Os dados minimos que voce precisa
Ideia principal:
O time já possui dados suficientes para começar sem transformar a empresa num laboratório.

Pontos que precisam aparecer:
- Data de início do item.
- Data de conclusão do item.
- Histórico real do próprio fluxo.
- Ferramenta importa menos do que consistência do dado.

Mensagem de palco:
Você não precisa de maturidade perfeita para começar a prever melhor.

### 6. Como prever um item
Ideia principal:
Para um item, a referência principal é a distribuição de lead time histórico.

Pontos que precisam aparecer:
- Lead time como tempo entre começar e concluir.
- Percentis como linguagem simples de risco.
- Item Age como leitura operacional do que está acontecendo agora.

Mensagem de palco:
Previsão boa não serve só para promessa. Serve para agir cedo quando o risco sobe.

### 7. Como prever varios itens
Ideia principal:
Quando a pergunta é sobre backlog, release ou trimestre, o dado central passa a ser throughput.

Pontos que precisam aparecer:
- Throughput como itens concluídos por período.
- Distribuição histórica de throughput.
- As duas perguntas de negócio:
  - quando N itens ficam prontos
  - quantos itens ficam prontos até a data X

Mensagem de palco:
Para lote, throughput conversa melhor com a realidade do sistema do que pontos.

### 8. Monte Carlo como ferramenta pragmatica
Ideia principal:
Monte Carlo não precisa ser vendido como sofisticação; ele é apenas um jeito prático de simular futuros plausíveis.

Pontos que precisam aparecer:
- Usa o comportamento histórico do sistema.
- Gera faixa provável, não data mágica.
- Evita a falsa sensação de certeza da planilha linear.

Mensagem de palco:
Em vez de apostar em um futuro inventado, você testa milhares de futuros compatíveis com seus dados.

### 9. O que fazer para melhorar o sistema
Ideia principal:
Não basta prever. É preciso mexer nas alavancas que reduzem o tempo de entrega.

Pontos que precisam aparecer:
- Lei de Little como modelo simples.
- WIP alto aumenta fila e alonga cycle time.
- No curto prazo, reduzir WIP costuma ser mais controlável do que tentar aumentar throughput.

Mensagem de palco:
Previsibilidade não é um relatório. É uma propriedade operacional do sistema.

### 10. Fechamento
Ideia principal:
O ganho real não é acertar o futuro. É tomar decisão melhor diante da incerteza.

Pontos que precisam aparecer:
- Trocar promessa frágil por conversa transparente.
- Responder prazo com data e confiança.
- Usar os dados para decidir, priorizar e agir.

Mensagem de palco:
Quem explicita risco parece menos certo no começo, mas se torna muito mais confiável ao longo do tempo.

## Sequencia minima para montar os slides
Se for construir aos poucos no Slidev, esta ordem já dá uma espinha dorsal boa:

1. Capa.
2. A pergunta "quando vai ficar pronto?".
3. Exemplo de variabilidade.
4. O problema da conta linear.
5. Estimativa x previsão.
6. Dados mínimos.
7. Lead time e item age.
8. Throughput para lote.
9. Monte Carlo.
10. Lei de Little e encerramento.

## Frase-guia para manter consistencia
Toda vez que surgir uma data no deck, ela deve vir acompanhada da pergunta: com qual nivel de confianca?
- Princípio:
  - Stop starting, start finishing

### Speaker notes
- Use o gráfico para mostrar visualmente o efeito da fila.
- Se a pressão é velocidade, a resposta prática é reduzir WIP.
- Menos WIP reduz cycle time e tende a reduzir variabilidade.
- Resultado: mais rapidez e mais previsibilidade ao mesmo tempo.
- Mensagem para liderança iniciante: parar de começar tudo acelera mais do que cobrar estimativa "precisa".

## Slide 16: Encerramento + QR Code
### Título
Quer aplicar amanhã no seu contexto?

### Texto do slide
- QR code para:
  - repositório no GitHub
  - notebook
  - dados de exemplo
- Próximo passo sugerido:
  - rodar com os dados reais do seu time
- Mensagem final:
  - Data com confiança + ações no sistema

### Speaker notes
- Fechar com convite para experimentação imediata.
- Síntese: não é data mágica, é risco explícito e melhoria de fluxo.
- Última frase: previsibilidade é uma capacidade de gestão, não um chute sofisticado.
