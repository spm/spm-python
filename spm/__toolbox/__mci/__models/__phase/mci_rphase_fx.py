from spm._runtime import Runtime


def mci_rphase_fx(*args, **kwargs):
    r"""
      Flow function for phase model  
        FORMAT [f] = mci_rphase_fx (x,u,P,M)  
         
        x      state vector  
        u      inputs  
        P      parameter vector  
        M      model structure  
         
        f      dx/dt  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/models/phase/mci_rphase_fx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_rphase_fx", *args, **kwargs)
