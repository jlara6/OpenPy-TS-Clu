from openpy_ts_clu import clustering_kmeans, scenarios
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

path_AMI = r"G:\Mi unidad\UNSJ-IEE\Estudio PhD REID\Avances de Tesis PhD\3. Pseudomedicones para EESD\Data BBDD\London_Low_Carbon\dataset_imputation_30min.csv"
dict_sce = scenarios.dictionary()
dict_sce['seasons'] = ['Summer']  # ['Summer', 'Fall', 'Winter', 'Spring']
dict_sce['month'] = ['January']  # ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
dict_sce['year'] = [2013]  # [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
dict_sce['day_name'] = ['Monday']  # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict_sce['day_type'] = ['working']  # ['working', 'non-working']

df_multi = scenarios.multiple_users(
        file_path=path_AMI,
        dict_scenario=dict_sce,
        id_col_users='LCLid',
        variable='energy(kWh/hh)'
    )

model = clustering_kmeans(
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

