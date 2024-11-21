from spm.__wrapper__ import Runtime


def spm_vpca_f(*args, **kwargs):
    """
      Compute free energy of VPCA model  
        FORMAT [Fm] = spm_vpca_f (pca,c)  
         
        pca   data structure (see eg. spm_vpca.m)  
        c     information about single component  
         
        Fm    negative free energy of model  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mlm/spm_vpca_f.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vpca_f", *args, **kwargs)
