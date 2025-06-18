from mpython import Runtime


def spm_shp_install(*args, **kwargs):
    """
      Download files required for Shape PCA model

        FORMAT datadir = spm_shp_install(datadir,[force=true])
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_shp_install.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_shp_install", *args, **kwargs)
