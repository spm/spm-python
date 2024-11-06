from spm.__wrapper__ import Runtime


def spm_mci_adjoint(*args, **kwargs):
    """
      Gradient of log joint from adjoint method   
        FORMAT [dLdp,g,x] = spm_mci_adjoint (Pr,M,U,Y)  
         
        Pr        Parameters (vectorised and in M.V subspace)  
        M         Model structure  
        U         Inputs  [Nin x N]  
        Y         Data  
              
        dLdp      Gradient    [Np x 1]  
        g         Outputs     [N x Nout]  
        x         States      [N x Nstates]  
         
        If M.adjlike=1 this function returns gradient of log likelihood  
         
        This function uses integrators from MATLAB's ODE Suite  
         
        B. Sengupta, K. Friston and W. Penny (2014) Efficient Gradient  
        Computation for Dynamical Models. Neuroimage,98, 521-527.   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_adjoint.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_adjoint", *args, **kwargs)
