from spm.__wrapper__ import Runtime


def mci_nmm_gen(*args, **kwargs):
    """
      Generate data from two region NMM   
        FORMAT [Y] = mci_nmm_gen (M,U,P)  
         
        M         Model structure  
        U         Inputs  
        P         Parameters  
         
        Y         Data  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_nmm_gen", *args, **kwargs)
