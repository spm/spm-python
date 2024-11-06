from spm.__wrapper__ import Runtime


def mci_phase_fx(*args, **kwargs):
    """
      Flow function for phase model  
        FORMAT [f] = mci_phase_fx (x,u,P,M)  
         
        x      state vector  
        u      inputs  
        P      parameter vector  
        M      model structure  
         
        f      dx/dt  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_phase_fx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mci_phase_fx", *args, **kwargs)
