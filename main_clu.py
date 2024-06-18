#%% md
# # Importing libraries
#%%
from openpy_ts_clu import clustering_kmeans, scenarios
import matplotlib.pyplot as plt
#%% md
# # Load scenarios
#%%
dict_sce = scenarios.dictionary()
dict_sce['seasons'] = ['Winter']  # ['Summer', 'Fall', 'Winter', 'Spring']
# dict_sce['month'] = ['January']  # ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# dict_sce['year'] = [2013]  # [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
dict_sce['day_name'] = ['Monday']  # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
dict_sce['day_type'] = ['working']  # ['working', 'non-working']
#%%
dict_sce
#%% md
# # Create dataset with multiple users
#%%
df_multi = scenarios.multiple_users(
        # file_path=path_AMI,
        dict_scenario=dict_sce,
        id_col_users='LCLid',
        variable='energy(kWh/hh)'
    )
#%%
df_multi.head()
#%%
df_multi.shape
#%% md
# # Clustering using KMeans
#%% md
# ## Init class to clustering
#%%
model = clustering_kmeans(
    model='KMeans',
    users=None,
    metric='dtw',
    df_sce=df_multi,
    type_dr='mds'
)

#%% md
# ## Optimal number of clusters
#%%
model.optimal_number_of_clusters(max_clusters=8, plt_metrics=True)
#%% md
# ## Get dendogram
#%%
model.get_dendograma(n_cluster=4)
#%% md
# ## Train clustering model
#%%
dict_clu = model.train_clu_model(n_clusters=4, acum_bar=True, points_2d=True)
#%%
dict_clu.keys()
#%%
dict_clu['dataset']
#%% md
# ## Extract time series of clusters
#%%
dict_clu = model.cluster_ts_extraction(n_clusters=4, all_barycenters=True, plt_all_graphs=True)
#%%
dict_clu.keys()
#%%
len(dict_clu['dataset'])
#%%
len(dict_clu['euclidean'])
#%% md
# ## Plot time series of clusters and barycenters
#%% md
# ### Centroids
#%%
for i in range(len(dict_clu['centroid'])):
    plt.plot(dict_clu['centroid'][i], label='Cluster ' + str(i + 1))
plt.legend()
#%%
dict_clu['centroid'][0].T
#%% md
# ### Euclidean
#%%
for i in range(len(dict_clu['euclidean'])):
    plt.plot(dict_clu['euclidean'][i], label='Cluster ' + str(i + 1))
plt.legend()
#%%
dict_clu['euclidean'][0].T
#%%
