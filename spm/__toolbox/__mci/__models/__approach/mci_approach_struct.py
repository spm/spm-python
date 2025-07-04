from spm._runtime import Runtime


def mci_approach_struct(*args, **kwargs):
    """
      Approach model structure  
        FORMAT [M,U] = mci_approach_struct (Nobs)  
         
        Nobs      Number of observations  
        M         Model structure  
        U         Input structure  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/approach/mci_approach_struct.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_approach_struct", *args, **kwargs)
