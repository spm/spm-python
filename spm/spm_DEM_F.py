from spm._runtime import Runtime


def spm_DEM_F(*args, **kwargs):
    r"""
      Free-energy as a function of conditional parameters  
        FORMAT [F,p] = spm_DEM_F(DEM,ip)  
         
        DEM    - hierarchical model  
         
        F(i)   - free-energy at <q(P(ip))> = p(i)  
         
        where p(i) is the ip-th free-parameter. This is a bound on   
        the log-likehood (log-evidence) conditioned on the expected parameters.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_DEM_F.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_DEM_F", *args, **kwargs)
