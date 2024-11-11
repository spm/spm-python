from spm.__wrapper__ import Runtime


def mci_nmm_params(*args, **kwargs):
    """
      Generate parameters for two region NMM   
        FORMAT [P] = mci_nmm_params (M,U)  
         
        M         Model structure  
        U         Inputs  
         
        P         Parameters  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_params.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_nmm_params", *args, **kwargs)
