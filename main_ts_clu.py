from openpy_ts_clu import clustering_ts, scenarios
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path_AMI = r"G:\Mi unidad\UNSJ-IEE\Estudio PhD REID\Avances de Tesis PhD\3. Pseudomedicones para EESD\Data BBDD\London_Low_Carbon\dataset_imputation_30min.csv"
dict_sce = scenarios.dictionary()
dict_sce['seasons'] = ['Summer']
dict_sce['day_name'] = ['Monday']
#dict_sce['day_type'] = ['working']

df_multi = scenarios.multiple_users(
        file_path=path_AMI,
        dict_scenario=dict_sce,
        id_col_users='LCLid',
        variable='energy(kWh/hh)'
    )

# models clustering
kmeans = 1
dict_models = {
    'KMeans': True,
    # 'MeanShift': True,  # OK
    # 'DBSCAN': True,  # OK
    # 'MiniBatchKMeans': True,  # OK
    # 'Birch': True,  # OK
    # 'GaussianMixture': True,  # OK
    # 'OPTICS': True,  # OK
    # 'AffinityPropagation': True,  # OK
    # 'Agglomerative': True,  # OK
    # 'Spectral': True,  # OK
    # 'SOM': True,
    # 'TSKMeans': False
}

model = clustering_ts(
    model='KMeans',
    users=None,
    metric='dtw',
    df_sce=df_multi,
    type_dr='mds'
)

model.optimal_number_of_clusters(max_clusters=3, plt_metrics=True)
model.get_dendograma(n_cluster=3)
dict_results = model.train_clu_model(n_clusters=3, acum_bar=True, view_clu=True, points_2d=True)
model.cluster_ts_extraction(n_clusters=3, all_barycenters=True, plt_all_graphs=True)

