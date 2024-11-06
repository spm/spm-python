from spm.__wrapper__ import Runtime


def spm_mci_sens_init(*args, **kwargs):
    """
      Compute sensitivity to initial state   
        FORMAT [y,sy,st] = spm_mci_sens_init (R,P,M,U)  
         
        R         Initial state  
        P         Parameters  
        M         Model structure  
        U         Inputs  [Nin x N]  
              
        y         Outputs     [N x Nout]  
        sy        Output Sensitivity, dy/dP [N x Nout x Nparams]  
        st        Status flag (0 for OK, -1 for problem)  
                  ... evaluated at the N time points in M.t  
         
        M.f       Flow function dx/dt=f(x,u,P,M)  
        M.g       Observation function y=g(x,u,P,M)  
         
        This function uses Matlab's ODE suite   
         
        B. Sengupta, K. Friston and W. Penny (2014) Efficient Gradient  
        Computation for Dynamical Models. Neuroimage,98, 521-527.   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_sens_init.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_sens_init", *args, **kwargs)
