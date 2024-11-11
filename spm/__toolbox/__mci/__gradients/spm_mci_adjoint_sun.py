from spm.__wrapper__ import Runtime


def spm_mci_adjoint_sun(*args, **kwargs):
    """
      Gradient of log joint from adjoint method (via Sundials)  
        FORMAT [dLdp] = spm_mci_adjoint_sun (Pr,M,U,Y)  
         
        Pr        Parameters (vectorised and in M.V subspace)  
        M         Model structure  
        U         Inputs  [Nin x N]  
        Y         Data  
              
        dLdp      Gradient [Np x 1]  
         
        For M.adjlike=1, dLdp is gradient of log likelihood not log joint  
        (useful for debugging).  
         
        For M.backint=1 (default), compute the integral underlying dLdp  
        *during* backwards integration of adjoint. For M.backint=0, this   
        integral is computed *after* adjoint (useful for debugging).  
         
        B. Sengupta, K. Friston and W. Penny (2014) Efficient Gradient  
        Computation for Dynamical Models. Neuroimage,98, 521-527.   
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/gradients/spm_mci_adjoint_sun.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_adjoint_sun", *args, **kwargs)
