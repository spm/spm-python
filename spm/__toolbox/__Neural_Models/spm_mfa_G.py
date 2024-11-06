from spm.__wrapper__ import Runtime


def spm_mfa_G(*args, **kwargs):
    """
      Create a structure for a Gibb's ensemble  
        FORMAT [G] = spm_mfa_G(M,x)  
       --------------------------------------------------------------------------  
        M   - model specification structure  
        Required fields:  
           M.f   - dx/dt    = f(x,u,P)                {function string or m-file}  
           M.g   - y(t)     = l(x,P)                  {function string or m-file}  
           M.m   - m inputs  
           M.n   - n states  
           M.l   - l ouputs  
           M.x   - (n x 1) = x(0) = expansion point  
           M.W   - (n x n) - covariance matrix of deterministic noise  
        x    -  {1 x d cell}    - range of state [d]-space  
         
        G   - ensemble specification structure  
        fields  
          G.M:  [1 x 1 struct]  - dynamic model structure  
          G.J0: [n x n double]  - Jacobian  
          G.J1: {1 x M.m cell}  - dJ0/du  
          G.L : [l x n double]  - d<y>/dp  
          G.u:  [n x m double]  - probability modes  
          G.v:  [m x n double]  - v*u = 1  
          G.X:  [n x d double]  - evaluation points of state [d]-space  
          G.x:  {1 x d cell}    - range of state [d]-space  
          G.p0: [n x 1 sparse]  - expansion point  
          G.q0: [n x 1 sparse]  - equilibrium density  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_mfa_G.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mfa_G", *args, **kwargs)
