from spm._runtime import Runtime


def spm_vpca_update(*args, **kwargs):
    r"""
      Update VPCA parameters  
        FORMAT [pca,c] = spm_vpca_update (T,S,pca,c,m)  
         
        T     [d x N] matrix containing N d-dimensional data vectors  
              The nth data sample, t_n, is nth column of T  
        S  
        pca   data structure (see eg. spm_vpca.m)  
        c     information about single component  
        m     cluster number (used for mixtures of VPCA model)  
         
        pca,c updated info  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mlm/spm_vpca_update.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vpca_update", *args, **kwargs)
