from spm.__wrapper__ import Runtime


def mci_approach_gen(*args, **kwargs):
    """
      Approach to limit model  
        FORMAT [y] = mci_approach_gen (P,M,U)  
         
        P         parameters  
        M,U       as usual  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/approach/mci_approach_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_approach_gen", *args, **kwargs)
