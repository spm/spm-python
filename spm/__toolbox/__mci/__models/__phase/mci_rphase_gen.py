from spm.__wrapper__ import Runtime


def mci_rphase_gen(*args, **kwargs):
    """
      Generate data from reduced WCO model  
        FORMAT [Y] = mci_rphase_gen (P,M,U)  
         
        P     parameters  
        M     model structure  
        U     inputs  
         
        Y     data  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_rphase_gen.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_rphase_gen", *args, **kwargs)
