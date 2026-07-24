"""
=============================================================================
PROJETO: Machine Learning - Segmentação de Dados com K-Means (Scikit-Learn)
Autor: Victor Oliveira
Ferramentas: Python, Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn
=============================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

# Configuração visual
sns.set_theme(style="whitegrid")

def executar_clusterizacao():
    print("1. Gerando dados para segmentação por clusters...")
    blob_centers = np.array([
        [0.2, 2.3],
        [-1.5, 2.3],
        [-2.8, 1.8],
        [-2.8, 2.8],
        [-2.8, 0.8]
    ])
    blob_std = np.array([0.4, 0.3, 0.1, 0.1, 0.1])
    X, y_true = make_blobs(n_samples=2000, centers=blob_centers, cluster_std=blob_std, random_state=42)
    
    # Método do Cotovelo
    print("2. Calculando a Inércia (Método do Cotovelo)...")
    inercias = []
    k_range = range(1, 10)
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        inercias.append(kmeans.inertia_)
        
    # Treino com K=5
    k_ideal = 5
    print(f"3. Treinando modelo K-Means com K={k_ideal}...")
    kmeans_final = KMeans(n_clusters=k_ideal, random_state=42, n_init=10)
    labels = kmeans_final.fit_predict(X)
    centroides = kmeans_final.cluster_centers_
    
    score = silhouette_score(X, labels)
    print(f"   Score de Silhueta: {score:.4f}")
    
    # Salvando Gráfico 1: Cotovelo
    plt.figure(figsize=(9, 5))
    plt.plot(k_range, inercias, 'bo-', linewidth=2, markersize=8)
    plt.xlabel('Número de Clusters (k)', fontsize=12)
    plt.ylabel('Inércia (Soma das Distâncias Quadráticas)', fontsize=12)
    plt.title('Método do Cotovelo (Elbow Method) para Escolha do K Ideal', fontsize=13, fontweight='bold')
    plt.axvline(x=5, color='r', linestyle='--', label='K Ideal = 5')
    plt.legend()
    plt.tight_layout()
    plt.savefig(r"G:\Meu Drive\Cursos\Projetos Práticos\kmeans-clustering-scikit-learn\elbow_method.png", dpi=150)
    plt.close()
    
    # Salvando Gráfico 2: Clusters
    plt.figure(figsize=(10, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='tab10', s=15, alpha=0.7, label='Observações / Clientes')
    plt.scatter(centroides[:, 0], centroides[:, 1], c='red', marker='X', s=200, label='Centróides dos Clusters')
    plt.xlabel('Recurso X1 (Feature 1)', fontsize=12)
    plt.ylabel('Recurso X2 (Feature 2)', fontsize=12)
    plt.title(f'Resultado da Clusterização K-Means (K={k_ideal})', fontsize=13, fontweight='bold')
    plt.legend()
    plt.tight_layout()
    plt.savefig(r"G:\Meu Drive\Cursos\Projetos Práticos\kmeans-clustering-scikit-learn\cluster_visualization.png", dpi=150)
    plt.close()

    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    executar_clusterizacao()
