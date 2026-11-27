from spm._runtime import Runtime


def spm_shp_install(*args, **kwargs):
    r"""
      Download files required for Shape PCA model  
         
        FORMAT datadir = spm_shp_install(datadir,[force=true])  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_shp_install.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_shp_install", *args, **kwargs)
