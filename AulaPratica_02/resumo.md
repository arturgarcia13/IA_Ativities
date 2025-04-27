# 🧠 **Busca de Custo Uniforme**

## 1. O que é essa tal de "Busca de Custo Uniforme"?

Imagina que tu tá andando numa cidade com várias ruas.  
Cada rua tem um **custo** (tempo, distância, dinheiro, tanto faz).  
A ideia é: **achar o caminho mais barato** para chegar onde tu quer.

**Busca de Custo Uniforme** é simplesmente um jeito organizado de fazer isso, sempre escolhendo a opção **mais baratinha primeiro**.

---

## 2. Como ela funciona (passo a passo)

### Passo 1: Começa do início

- Tu começa no teu **nó inicial** (por exemplo, a tua casa).

### Passo 2: Olha quem tá perto

- Vê todas as opções de caminho que saem de onde tu tá.
- Anota o custo de chegar em cada lugar.

### Passo 3: Escolhe o mais barato

- Entre todas as opções **de todo mundo que já foi visitado**, tu vai para o que tá mais barato.
- Não importa se ele é "direto" ou "longe", o que manda é o **custo acumulado**.

### Passo 4: Repete até achar o destino

- Quando chegar no nó objetivo, **pronto**! Achou o caminho de menor custo.

---

## 3. Ferramenta que usamos: **Fila de Prioridade**

Pra fazer isso rápido, a gente usa uma **fila de prioridade**:

- Sempre pega o caminho com **menor custo acumulado**.
- Se tiver vários caminhos, sempre atualiza os custos enquanto anda.

É tipo uma lista mágica que sempre entrega o mais barato primeiro.

---

## 4. Resumo SUPER curto (como se eu tivesse que explicar pra uma criança)

> "É como procurar o caminho até a escola escolhendo sempre a rua que custa menos passar, até chegar lá."

---

# 📈 Exemplo bem simples (micrografo)

Imagina esse mini mapa:

```
A --(2)--> B --(2)--> D
A --(1)--> C --(5)--> D
```

- De A pra B custa 2.
- De B pra D custa 2.
- De A pra C custa 1.
- De C pra D custa 5.

**Qual caminho tu escolhe para sair do A e chegar no D?**

**Simulação da Busca de Custo Uniforme:**

- Começo no **A**.
- Vizinhos de A: B (2) e C (1).
- Escolho **C** primeiro (porque custa 1).
- De C para D custa 5 → custo total = 1 + 5 = 6.
- B ainda tá lá (custo 2 pra chegar nele).
- Agora vou para **B** (porque custa 2, mais barato que 6).
- De B para D custa 2 → custo total = 2 + 2 = 4.
- Pronto! Achei um caminho de custo 4 (melhor que 6).

**Resposta**: Caminho A → B → D (com custo 4).

---

# 🔥 Resumo final pra lembrar SEMPRE:

**"Expande sempre o caminho mais barato. Quando chegar no objetivo, o caminho tá garantido ser o de menor custo."**