FROM jupyter/minimal-notebook:177037d09156
RUN pip install nbgitpuller
RUN jupyter serverextension enable --py nbgitpuller --sys-prefix
RUN conda create --yes -n skymap jupyter python=3.6 pandas=0.23.4 seaborn=0.8.1 scikit-learn=0.19.1
RUN conda install --yes -n skymap nb_conda_kernels
RUN conda install --yes nb_conda_kernels
RUN conda install --yes -n skymap -c bioconda kallisto=0.44.0
RUN conda install --yes -n skymap -c  bioconda trim-galore=0.4.1


#RUN mkdir efs

#RUN conda install --yes astropy
