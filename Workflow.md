**2- Identify Necessary Modifications:**

Podemos fazer estas coisas:

1. **Buracos no Chão**
- Introduzir lacunas na superfície pode adicionar um elemento de desafio ao agente.
- **Ideia de como fazer:** Alterar a geração do terreno para incluir secções sem piso (pontos de coordenadas onde a altura é indefinida ou nula).
Certificar de que as lacunas sejam atravessáveis para não tornar o ambiente impossível.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. **Objetos no Chão (Obstáculos)**
- Adicionar obstáculos como blocos ou rampas no caminho do agente.
- **Ideia de como fazer:** Modificar a função que gera o terreno para incluir objetos fixos ou móveis. Ajustar as interações físicas, caso necessário.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. **Objetos no Ar (Desafios Adicionais)**
- Insirir objetos aéreos que o agente precisa evitar (como um pêndulo, ou aves etc) ou interagir (como coletar pontos).

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Ideias do chat:**

4. **Modificação do Espaço de Estados**
- Alterar as informações que o agente recebe:
    - Remover algumas variáveis (por exemplo, posição das pernas ou ângulos articulares). 
    - Adicionar novas variáveis (como distância do próximo obstáculo).



5. **Alteração do Modelo de Recompensa**
- Modificar o sistema de recompensas para:
    - Penalizar quedas mais fortemente.
    - Recompensar a distância percorrida, mas com bônus extras por evitar obstáculos ou saltar sobre buracos.

6. **Velocidade do Terreno**
- Introduzir um terreno "em movimento" para simular um terreno em deslocamento.
