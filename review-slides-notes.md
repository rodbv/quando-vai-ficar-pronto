# Revisao de Slides - Notas de Critica

Objetivo: registrar ideias, criticas e sugestoes sem aplicar mudancas ainda.

## Regras desta fase

- Nao alterar os slides durante a coleta.
- Registrar observacoes de forma objetiva.
- Priorizar impacto na mensagem e na apresentacao ao vivo.

## Resumo rapido da revisao

- Data:
- Contexto da apresentacao:
- Impressao geral:

## Observacoes por slide ou secao

Use este formato para cada ponto:

- Slide/Secao:
- Tipo: Conteudo | Narrativa | Visual | Tecnico | Linguagem | Timing
- Observacao:
- Impacto: Alto | Medio | Baixo
- Sugestao:
- Exemplo de ajuste (opcional):

### Ponto 1

- Slide/Secao: Slide 3 - O cenario classico
- Tipo: Narrativa | Conteudo
- Observacao: Exemplo atual (40 story points) pode soar menos realista para contexto com PM/CEO.
- Impacto: Alto
- Sugestao: Trocar para narrativa com maior pressao executiva e data explicita.
- Exemplo de ajuste (opcional):
	- "Temos 150 story points, nossa velocity e 30, umas 5 semanas?"
	- Cliente [muda pra PM]: "OK, 5 semanas, isso da 10 de junho"
	- PM pro CEO: "Dia 10 de junho sem falta ta pronto"

### Ponto 2

- Slide/Secao: Slide 4 - Roteiro de hoje
- Tipo: Narrativa | Timing
- Observacao: Slide considerado dispensavel no fluxo atual.
- Impacto: Medio
- Sugestao: Remover o slide para acelerar entrada no conteudo principal.
- Exemplo de ajuste (opcional): Ir direto de "O cenario classico" para "O problema com Story Points".

### Ponto 3

- Slide/Secao: Slide 5 - O problema com Story Points
- Tipo: Linguagem | Narrativa
- Observacao: A analogia da camiseta foi percebida como fraca e pouco convincente.
- Impacto: Medio
- Sugestao: Substituir por analogia mais direta sobre medida relativa vs previsao de tempo.
- Exemplo de ajuste (opcional):
	- "Story point e tamanho relativo, nao calendario."
	- Opcoes de analogia para testar:
		- "Story point para data e como usar grau de picancia para prever tempo de preparo: ajuda a comparar pratos, nao a dizer que sai em 12 minutos."
		- "Story point para data e como usar tamanho de mala para prever duracao da viagem: mede volume, nao tempo."
		- "Story point para data e como usar nota de dificuldade da trilha para prever hora de chegada: orienta esforco, nao cronometro."

## Itens para confirmar (duvidas)

- 
- 
- 

### Ponto 4

- Slide/Secao: Slide 6 - "Mas a gente usa velocity..."
- Tipo: Visual | Layout
- Observacao: Grafico aparenta estar cortando na parte inferior durante apresentacao.
- Impacto: Medio
- Sugestao: Garantir margem/padding inferior de pelo menos 30px para o chart.
- Exemplo de ajuste (opcional): Aplicar `margin-bottom: 30px` (ou padding equivalente no container) especificamente neste slide.

## Ajustes sugeridos para o proximo ciclo

### Alta prioridade

- 
- 
- 

### Ponto 5

- Slide/Secao: Slide 8 - "Essa nao e uma ideia nova"
- Tipo: Narrativa | Timing
- Observacao: Slide pode ser removido para reduzir duracao e manter ritmo.
- Impacto: Medio
- Sugestao: Matar o slide 8 e distribuir credito aos autores em notas de fala ou em uma secao mais curta.
- Exemplo de ajuste (opcional): Inserir referencia breve a Vacanti/Magennis em 1 linha no fim do slide anterior.

### Ponto 6

- Slide/Secao: Slide 10 - "Tres pilares de fluxo (Vacanti)"
- Tipo: Narrativa | Timing
- Observacao: Slide considerado removivel para enxugar a sequencia e acelerar entrada na parte pratica.
- Impacto: Medio
- Sugestao: Matar o slide 10 e introduzir os pilares de forma mais curta no slide seguinte.
- Exemplo de ajuste (opcional): Manter apenas uma frase-ponte antes de "Cycle Time: do dado ao numero".

### Ponto 7

- Slide/Secao: Slide 11 - "Cycle Time: do dado ao numero"
- Tipo: Narrativa | Didatica
- Observacao: Nao iniciar com codigo; abertura tecnica logo no inicio pode afastar parte da plateia.
- Impacto: Alto
- Sugestao: Comecar com exemplo simples em tabela antes do codigo.
- Exemplo de ajuste (opcional): Tabela com 5 linhas contendo apenas data de inicio (sem hora), data de fim e dias corridos.

### Ponto 8

- Slide/Secao: Slide 12 - histograma/distribuicao de cycle time
- Tipo: Visual | Grafico
- Observacao: Numeros no eixo estao muito comprimidos na parte inferior, dificultando leitura.
- Impacto: Medio
- Sugestao: Ajustar escala do eixo para melhorar separacao visual; proposta do revisor: escala logaritmica.
- Exemplo de ajuste (opcional): Usar eixo Y em log no grafico deste slide e revisar labels para manter interpretacao clara para publico nao tecnico.

### Ponto 9

- Slide/Secao: Slide 16 - "Throughput: o ritmo da equipe"
- Tipo: Didatica | Narrativa
- Observacao: Nao usar codigo nesse ponto da historia.
- Impacto: Alto
- Sugestao: Trocar bloco de codigo por tabela simples de throughput semanal (TP), com 5 linhas reais do CSV.
- Exemplo de ajuste (opcional): Colunas `# semana` e `valor` (TP da semana), mantendo linguagem visual direta.

### Ponto 10

- Slide/Secao: Slide 24
- Tipo: Narrativa | Timing
- Observacao: Solicitar remocao do slide para encurtar a apresentacao.
- Impacto: Medio
- Sugestao: Matar slide 24 e absorver mensagem essencial no slide anterior ou seguinte, se necessario.
- Exemplo de ajuste (opcional): Remocao direta sem substituicao caso nao haja perda de contexto.

### Ponto 11

- Slide/Secao: Slide 25
- Tipo: Didatica | Narrativa
- Observacao: Nao usar bloco de codigo neste slide.
- Impacto: Medio
- Sugestao: Trocar codigo por representacao visual simples (tabela, fluxograma curto ou pseudo-passos).
- Exemplo de ajuste (opcional): 3 a 5 passos em linguagem natural, sem sintaxe de programacao.

### Ponto 12

- Slide/Secao: Slide 26
- Tipo: Didatica | Visual
- Observacao: Precisamos apenas explicar o conceito, sem mostrar codigo.
- Impacto: Alto
- Sugestao: Substituir por um fluxograma em Mermaid com o fluxo da simulacao.
- Exemplo de ajuste (opcional): Inicio -> Sortear throughput da semana -> Acumular entregas -> Atingiu N itens? -> Sim: registrar semanas / Nao: repetir -> Repetir simulacoes -> Ler percentis.

### Media prioridade

- 
- 
- 

### Baixa prioridade

- 
- 
- 

## O que manter como esta

- 
- 
- 

## Checklist para rodada final de ajustes

- [ ] Mensagem central clara
- [ ] Fluxo narrativo sem quebras
- [ ] Consistencia de termos
- [ ] Consistencia visual
- [ ] Numeros e exemplos alinhados com o codigo
- [ ] Tempo total dentro do planejado
