from spm._runtime import Runtime


def mci_ramsay_gen(*args, **kwargs):
    """
      Generate data from Ramsay model  
        FORMAT [Y] = mci_ramsay_gen (P,M,U)  
         
        P         Parameters  
        M         Model structure  
        U         Inputs  
         
        Y         Data  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/ramsay/mci_ramsay_gen.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_ramsay_gen", *args, **kwargs)
