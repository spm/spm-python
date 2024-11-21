from spm.__wrapper__ import Runtime


def spm_BIDS(*args, **kwargs):
    """
      Parse and query a directory structure formatted according to the BIDS standard  
        FORMAT BIDS = spm_BIDS(root)  
        root   - directory formatted according to BIDS [Default: pwd]  
        BIDS   - structure containing the BIDS file layout  
         
        FORMAT result = spm_BIDS(BIDS,query,...)  
        BIDS   - BIDS directory name or BIDS structure (from spm_BIDS)  
        query  - type of query: {'data', 'metadata', 'sessions', 'subjects',  
                 'runs', 'tasks', 'runs', 'types', 'modalities'}  
        result - outcome of query  
       __________________________________________________________________________  
         
        BIDS (Brain Imaging Data Structure): https://bids.neuroimaging.io/  
          The brain imaging data structure, a format for organizing and  
          describing outputs of neuroimaging experiments.  
          K. J. Gorgolewski et al, Scientific Data, 2016.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_BIDS.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_BIDS", *args, **kwargs)
