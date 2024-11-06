from spm.__wrapper__ import Runtime


def spm_DEM_F(*args, **kwargs):
    """
      Free-energy as a function of conditional parameters  
        FORMAT [F,p] = spm_DEM_F(DEM,ip)  
         
        DEM    - hierarchical model  
         
        F(i)   - free-energy at <q(P(ip))> = p(i)  
         
        where p(i) is the ip-th free-parameter. This is a bound on   
        the log-likehood (log-evidence) conditioned on the expected parameters.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_DEM_F.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_DEM_F", *args, **kwargs)
