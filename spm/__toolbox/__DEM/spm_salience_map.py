from spm._runtime import Runtime


def spm_salience_map(*args, **kwargs):
    r"""
      creates a salience map  
        FORMAT [S L] = spm_salience_map(M,n)  
         
        S  - Salience (n x n,1)  
        L  - list of (fictive) hidden control states (range of S)  
         
        M  - generative model (with M(2).v and M(1).xo encoding location (L)  
        n  - dimension of map (S)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_salience_map.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_salience_map", *args, **kwargs)
