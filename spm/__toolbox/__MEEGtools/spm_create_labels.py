from spm._runtime import Runtime


def spm_create_labels(*args, **kwargs):
    r"""
      Create n  numbered labels using a base string as template  
        FORMAT labels = spm_create_labels(S)  
          S           - input structure  
          Fields of S:  
          S.base      - Template string     - Default: 'T'  
          S.n         - number of labels    - Default:  1   
         
        Output:  
         labels       - cell array of labels  
         
        Example:  
              S = [];  
              S.base = 'TRIG';  
              S.n = 100;  
              labels = spm_create_labels(S);  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_create_labels.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_create_labels", *args, **kwargs)
