OpenPy-TS-Clu
===========================================
OpenPy-TS-Clu es una aplicación que permite mediante técnicas de minería de datos obtener modelos y patrones representativos de grupos de usuarios
consumidores de energía eléctrica, a partir de una infraestructura avanzada de medición inteligente.
Siendo su principal función la clasificación en grupos de usuarios que consumen la energía de forma similar
y definir una curva de carga típica que caracterice al grupo. Desarrollada en el marco del proyecto
OpenREiD (c) (Software integral de simulación y optimización de redes eléctricas de distribución), del
Instituto de Energía Eléctrica (IEE), UNSJ - CONICET, San Juan - Argentina.
Versión
## Installation

With pip

``pip install openpy-ts-clu``

Without pip, clone or download the repository, in the dist folder is the .whl file, copy the location of the file, and in the CMD:

``pip install {path-save-files}/openpy_ts_clu-{version}-py3-none-any.whl’``

<div id='id2'/>

If you have installation problems, you can contact us by email (**jlara@iee.unsj.edu.ar**) or through the same GitHub and according to the error that appears in the console we can give the necessary technical support.

## How to use  <a name="id1"></a>

First, in the IDE (Integrated Development Environment) of preference, we import the library:

```Python
from openpy_ts_clu import clustering_kmeans, scenarios
```

## License

License: CC BY-NC-SA 4.0

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />

This work has a license <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
