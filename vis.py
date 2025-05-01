def Visualisation(df_processed):


    if 'df_processed' not in locals():
        print("Erreur : Le DataFrame 'df_processed' n'a pas été trouvé. Veuillez exécuter la cellule de prétraitement (Cellule 4) d'abord.")
    else:
        print("Génération des visualisations pour le dataset prétraité...")

        # --- Distribution de la variable cible ---
        plt.figure(figsize=(6, 4))
        sns.countplot(x='depression', data=df_processed)
        plt.title('Distribution de la variable cible (Depression)')
        plt.xlabel('Depression (0: Non, 1: Oui)')
        plt.ylabel('Nombre')
        plt.xticks([0, 1], ['Non', 'Oui'])
        plt.show()

    # --- Histogrammes pour les variables numériques ---
    numerical_cols_plot = df_processed.select_dtypes(include=np.number).columns.tolist()
    if 'depression' in numerical_cols_plot:
        numerical_cols_plot.remove('depression') # Exclure la cible des histogrammes/boxplots séparés

    print(f"\nHistogrammes pour: {numerical_cols_plot}")
    n_cols_hist = 3 # Nombre de colonnes pour l'affichage des histogrammes
    n_rows_hist = (len(numerical_cols_plot) + n_cols_hist - 1) // n_cols_hist # Calculer le nombre de lignes nécessaires
    fig_hist, axes_hist = plt.subplots(n_rows_hist, n_cols_hist, figsize=(15, 4 * n_rows_hist))
    axes_hist = axes_hist.flatten() # Aplatir pour itérer facilement

    for i, col in enumerate(numerical_cols_plot):
        sns.histplot(df_processed[col], kde=True, ax=axes_hist[i])
        axes_hist[i].set_title(f'Histogramme de {col}')
    # Cacher les axes vides s'il y en a
    for j in range(i + 1, len(axes_hist)):
        fig_hist.delaxes(axes_hist[j])

    plt.suptitle('Histogrammes des variables numériques', y=1.02)
    plt.tight_layout()
    plt.show()

    # --- Boxplots pour les variables numériques ---
    print(f"\nBoxplots pour: {numerical_cols_plot}")
    n_cols_box = 3 # Nombre de colonnes pour l'affichage des boxplots
    n_rows_box = (len(numerical_cols_plot) + n_cols_box - 1) // n_cols_box # Calculer le nombre de lignes nécessaires
    fig_box, axes_box = plt.subplots(n_rows_box, n_cols_box, figsize=(15, 4 * n_rows_box))
    axes_box = axes_box.flatten() # Aplatir pour itérer facilement

    for i, col in enumerate(numerical_cols_plot):
        sns.boxplot(y=df_processed[col], ax=axes_box[i])
        axes_box[i].set_title(f'Boxplot de {col}')
        axes_box[i].set_ylabel('') # Optionnel: enlever le nom de la colonne comme ylabel

    # Cacher les axes vides s'il y en a
    for j in range(i + 1, len(axes_box)):
        fig_box.delaxes(axes_box[j])

    plt.suptitle('Boxplots des variables numériques', y=1.02)
    plt.tight_layout()
    plt.show()


    # --- Bar charts (Countplots) pour les variables catégorielles importantes ---
    categorical_cols_plot = ['gender', 'sleep_duration', 'dietary_habits',
                             'have_you_ever_had_suicidal_thoughts', 'family_history_of_mental_illness']
    # Filtrer au cas où une colonne n'existerait pas dans df_processed
    categorical_cols_plot = [col for col in categorical_cols_plot if col in df_processed.columns]

    print(f"\nDiagrammes à barres pour: {categorical_cols_plot}")
    n_cols_cat = 2 # Nombre de colonnes pour l'affichage
    n_rows_cat = (len(categorical_cols_plot) + n_cols_cat - 1) // n_cols_cat
    fig_cat, axes_cat = plt.subplots(nrows=n_rows_cat, ncols=n_cols_cat, figsize=(12, 5 * n_rows_cat)) # Ajuster la disposition
    axes_cat = axes_cat.flatten() # Aplatir

    for i, col in enumerate(categorical_cols_plot):
        sns.countplot(y=col, data=df_processed, ax=axes_cat[i], order = df_processed[col].value_counts().index)
        axes_cat[i].set_title(f'Distribution de {col}')
        axes_cat[i].set_xlabel('Nombre')
        axes_cat[i].set_ylabel('') # Enlever le nom de colonne comme ylabel

    # Cacher les axes vides
    for j in range(i + 1, len(axes_cat)):
        fig_cat.delaxes(axes_cat[j])

    plt.suptitle('Distribution des variables catégorielles sélectionnées', y=1.02)
    plt.tight_layout()
    plt.show()

    # --- Matrice de corrélation (Heatmap) ---
    print("\nHeatmap de Corrélation des variables numériques:")
    plt.figure(figsize=(12, 10))
    # Inclure la cible 'depression' si elle est numérique pour voir ses corrélations
    numerical_cols_corr = df_processed.select_dtypes(include=np.number).columns.tolist()
    if not numerical_cols_corr:
        print("Aucune colonne numérique trouvée pour la matrice de corrélation.")
    else:
        correlation_matrix = df_processed[numerical_cols_corr].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title('Matrice de Corrélation des variables numériques (y compris la cible)')
        plt.show()

    print("\n--- Fin des Visualisations ---")