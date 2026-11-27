from spm._runtime import Runtime


def spm_vpca_f(*args, **kwargs):
    r"""
      Compute free energy of VPCA model  
        FORMAT [Fm] = spm_vpca_f (pca,c)  
         
        pca   data structure (see eg. spm_vpca.m)  
        c     information about single component  
         
        Fm    negative free energy of model  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mlm/spm_vpca_f.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vpca_f", *args, **kwargs)
