from spm.__wrapper__ import Runtime


def spm_ness_Lap(*args, **kwargs):
    """
      Nonequilibrium steady-state under a Helmholtz decomposition  
        FORMAT [NESS] = spm_ness_Lap(M,x)  
       --------------------------------------------------------------------------  
        M   - model specification structure  
        Required fields:  
           M.f   - dx/dt   = f(x,u,P)  {function string or m-file}  
           M.pE  - P       = parameters of equation of motion  
           M.x   - (n x 1) = x(0) = expansion point  
           M.W   - (n x n) - precision matrix of random fluctuations  
        x    - cell array of vectors specifying evaluation grid  
         
        p0      - nonequilibrium steady-state  
        X       - evaluation points of state space  
        F       - expected flow  
        f       - original flow  
         
        NESS.H  - expected Hessian  
        NESS.J  - expected Jacobian  
        NESS.E  - Lyapunov exponents  
        NESS.H2 - expected Euclidean norm of Hessian  
        NESS.J2 - expected Euclidean norm of Jacobian  
        NESS.D2 - correlation dimension  
        NESS.bS - p0 = spm_softmax(spm_dctmtx(nx,nb)*bS);  
        NESS.nb - number of basis functions  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ness_Lap.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ness_Lap", *args, **kwargs)
