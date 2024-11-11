from spm.__wrapper__ import Runtime


def spm_salience_map(*args, **kwargs):
    """
      creates a salience map  
        FORMAT [S L] = spm_salience_map(M,n)  
         
        S  - Salience (n x n,1)  
        L  - list of (fictive) hidden control states (range of S)  
         
        M  - generative model (with M(2).v and M(1).xo encoding location (L)  
        n  - dimension of map (S)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_salience_map.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_salience_map", *args, **kwargs)
