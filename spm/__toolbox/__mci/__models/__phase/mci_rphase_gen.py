from spm._runtime import Runtime


def mci_rphase_gen(*args, **kwargs):
    r"""
      Generate data from reduced WCO model  
        FORMAT [Y] = mci_rphase_gen (P,M,U)  
         
        P     parameters  
        M     model structure  
        U     inputs  
         
        Y     data  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/phase/mci_rphase_gen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_rphase_gen", *args, **kwargs)
