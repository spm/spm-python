from spm._runtime import Runtime


def mci_phase_dfdp(*args, **kwargs):
    """
      Parameter sensitivity for phase model  
        FORMAT [dfdp] = mci_phase_dfdp (x,u,P,M)  
         
        x      State vector  
        u      inputs  
        P      parameter vector  
        M      model structure  
         
        dfdp   Jacobian wrt. parameters, df/dp  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_phase_dfdp.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_phase_dfdp", *args, **kwargs)
