from spm.__wrapper__ import Runtime


def spm_dcm2ssm(*args, **kwargs):
    """
      linearises a dynamic causal model about an expansion point  
        FORMAT [dfdx,dfdu,dgdx] = spm_dcm2ssm(P,M)  
         
        P - model parameters  
        M - model (with flow M.f and expansion point M.x and M.u)  
           M.f     - dx/dt = f(x,u,P,M)  {function string or m-file}  
           M.g     - y     = g(x,u,P,M)  {function string or m-file}  
           M.x [default: sparse(M.n,1)]  
           M.u [default: sparse(M.m,1)]  
          
        dfdx - Jacobian  
        dfdu - input  matrix  
        dgdx - output matrix  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_dcm2ssm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm2ssm", *args, **kwargs)
