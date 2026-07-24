# 🤖 Machine Learning: Segmentação e Agrupamento de Dados com K-Means (`Scikit-Learn`)

Este repositório contém um projeto prático de **Aprendizagem Não-Supervisionada (*Unsupervised Machine Learning*)** desenvolvido com a biblioteca `Scikit-Learn` em Python, focado no algoritmo de agrupamento **K-Means**.

---

## 🎯 Objetivos do Projeto
- Aplicar o algoritmo de clusterização **K-Means** para identificar agrupamentos naturais em conjuntos de dados multidimensionais.
- Utilizar o **Método do Cotovelo (*Elbow Method / Inércia*)** para selecionar o número ótimo de clusters ($K$).
- Avaliar a separabilidade e densidade dos clusters utilizando o **Score de Silhueta (*Silhouette Score*)**.
- Mapear visualmente as **Coordenadas Exatas dos Centróides** e suas regiões de atração espacial.

---

## 📈 Resultados Visualizados

### 📐 1. Método do Cotovelo (Determinação do K Ideal)
![Método do Cotovelo](elbow_method.png)

> **Insight:** A queda drástica de inércia desacelera a partir de **$K = 5$**, indicando a quantidade ideal de agrupamentos sem gerar sobre-segmentação.

---

### 📍 2. Localização dos Centróides & Fronteiras de Decisão
![Fronteiras e Centróides](centroids_boundaries.png)

> **Mapeamento de Centróides:** Cada centróide representa o ponto médio matemático de cada perfil/grupo de dados. As coordenadas exatas ($X_1, X_2$) definem o centro geométrico do cluster.

---

### 📊 3. Visualização dos Clusters Finais
![Visualização dos Clusters](cluster_visualization.png)

> **Métrica de Desempenho:** O modelo alcançou um **Score de Silhueta de 0.7215**, demonstrando alta separação espacial dos clusters e forte coesão interna.

---

## 🛠️ Tecnologias & Ferramentas
- **Linguagem**: Python 3
- **Machine Learning**: `Scikit-Learn` (`KMeans`, `silhouette_score`, `make_blobs`)
- **Manipulação de Dados**: `Pandas`, `NumPy`
- **Visualização**: `Matplotlib`, `Seaborn`

---

## 📂 Estrutura do Repositório

```text
kmeans-clustering-scikit-learn/
├── README.md                                 <-- Apresentação com gráficos incorporados
├── KMeans_Clusterizacao_ScikitLearn.ipynb   <-- Notebook formatado e documentado
├── kmeans_clustering.py                      <-- Script Python executável
├── elbow_method.png                          <-- Imagem do gráfico do cotovelo
├── centroids_boundaries.png                  <-- Imagem detalhada das coordenadas dos centróides
└── cluster_visualization.png                 <-- Imagem da visualização dos clusters
```

---

## 🚀 Como Executar Localmente

```bash
# 1. Clonar o repositório
git clone https://github.com/victorauso/kmeans-clustering-scikit-learn.git

# 2. Instalar dependências
pip install scikit-learn pandas numpy matplotlib seaborn

# 3. Executar o script
python kmeans_clustering.py
```

---

## 🎓 Contexto Acadêmico
Projeto baseado nos estudos práticos da **Pós-Graduação em Ciência de Dados e Inteligência Artificial** (Universidade São Judas).

---

## 📬 Contato
- **Victor Oliveira**
- 💼 **LinkedIn:** [linkedin.com/in/victor-oliveira](https://www.linkedin.com/in/victor-oliveira)
- ✉️ **Email:** victorauso@gmail.com
