from spm.__wrapper__ import Runtime


def spm_mci_fwd(*args, **kwargs):
    """
      Integrate dynamics and apply observation model  
        FORMAT [y,x,st] = spm_mci_fwd (P,M,U)  
         
        P         Parameters  
        M         Model structure  
        U         Inputs  [Nin x N]  
              
        y         Outputs     [N x Nout]  
        x         States      [N x Nstates]  
                  ... evaluated at the N time points in M.t  
        st        status flag (0 for OK, -1 for problem)  
         
        M.f       Flow function dx/dt=f(x,u,P,M)  
        M.g       Observation function y=g(x,u,P,M)  
        M.int     Integrator option   
                  eg. 'euler', 'ode15', 'sundials'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_fwd.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_fwd", *args, **kwargs)
