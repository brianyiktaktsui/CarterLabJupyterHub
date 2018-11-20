FROM jupyter/minimal-notebook:177037d09156
RUN pip install nbgitpuller
RUN jupyter serverextension enable --py nbgitpuller --sys-prefix
# -n skymap 
RUN conda create -p /home/jovyan/conda_user/skymap --yes jupyter python=3.6 pandas=0.23.4 seaborn=0.8.1 scikit-learn=0.19.1
RUN conda install --yes -p /home/jovyan/conda_user/skymap  nb_conda_kernels
RUN conda install --yes nb_conda_kernels
RUN conda install --yes -p /home/jovyan/conda_user/skymap -c bioconda kallisto=0.44.0
RUN conda install --yes -p /home/jovyan/conda_user/skymap -c  bioconda trim-galore=0.4.1
#RUN conda install -c conda-forge rsync
#RUN conda install -c anaconda ssh 
RUN conda install --yes -p /home/jovyan/conda_user/skymap -c plotly plotly
##install ipywidget
#RUN conda install --yes -p /home/jovyan/conda_user/skymap ipywidgets
RUN conda install --yes ipywidgets

RUN jupyter nbextension enable --py widgetsnbextension --sys-prefix && \
    # Also activate ipywidgets extension for JupyterLab
    # Check this URL for most recent compatibilities
    # https://github.com/jupyter-widgets/ipywidgets/tree/master/packages/jupyterlab-manager
    jupyter labextension install @jupyter-widgets/jupyterlab-manager && \
    jupyter labextension install jupyterlab_bokeh && \
    npm cache clean --force
    
USER root
RUN apt-get update && \
    apt-get install -y rsync openssh-client
USER $NB_UID

RUN conda install -c conda-forge jupyter_nbextensions_configurator
RUN conda install -c conda-forge jupyter_contrib_nbextensions 
RUN jupyter contrib nbextension install --user 
RUN jupyter nbextension enable --user init_cell/main
ADD https://raw.githubusercontent.com/brianyiktaktsui/CarterLabJupyterHub/master/start.sh /home/jovyan/start.sh

USER root
RUN chmod 777 /home/jovyan/start.sh
USER $NB_UID
#ENV PATH="/home/jovyan/conda_user/skymap/bin/:${PATH}"

