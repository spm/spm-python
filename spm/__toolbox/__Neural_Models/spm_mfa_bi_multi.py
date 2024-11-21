from spm.__wrapper__ import Runtime


def spm_mfa_bi_multi(*args, **kwargs):
    """
      Bilinear form for multiple Gibb's ensembles  
        FORMAT [M0,M1,L,M2] = spm_mfa_bi_multi(S,C)  
       --------------------------------------------------------------------------  
        S(s)   - MFA system specification structure for s ensembles  
        Required fields:  
            S(i).M:  [1x1 struct]    - dynamic model structure  
            S(i).J0: [n x n double]  - Jacobian  
            S(i).J1: {1 x M.m cell}  - dJ0/du  
            S(i).L : [l x n double]  - d<y>/dp  
            S(i).u:  [n x m double]  - probability modes  
            S(i).v:  [m x n double]  - v*u = 1  
            S(i).X:  [n x d double]  - evaluation points of state [d]-space  
            S(i).x:  {1 x d cell}    - range of state [d]-space  
            S(i).p0: [n x 1 sparse]  - expansion point  
         
        C{s x s cell} - coupling cell = dP/d<y> (change in parameters of S(i).M with  
                                          mean outputs of S(j).M - [p x l double])  
         
        M0  [ns + 1 x ns + 1double]  - 1st order Bilinear matrix dq/dt;  
        M1  {M.m x s}                - 2nd order Bilinear matrix dM0/du  
        M2  {s x s}                  - 2nd order Bilinear matrix dM0/dC  
        L   [1s x ns + 1 double]     - output matrix          <y> = L*q;  
         
        Transformed probability states:  q = [1; v*(p(X) - p0)];  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_mfa_bi_multi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mfa_bi_multi", *args, **kwargs)
