from spm.__wrapper__ import Runtime


def spm_mfa_bi(*args, **kwargs):
    """
      Bilinear form as a function of coupling parameters  
        FORMAT [M0,M1,L1] = spm_mfa_bi(M,P)  
       --------------------------------------------------------------------------  
        M  - MFA network specification structure  
        Required fields:  
          N.bi  - 'spm_mfa_bi';  
          N.M0  - 1st order bilinear operator;  
          N.M1  - dM1/dPu;  
          N.M2  - dM0/dPc;  
          N.L   - d<y>/dq;  
        P     - input and coupling parameters P = [Pu, Pc]  
         
        M0 [n x n double] - 1st order Lie matrix   
        M1 {1 x m cell}   - 2nd order Lie matrix   
        L1 {l x n cell}   - output matrix (1st order)    <y> = L1*q   
         
        Transformed states     q = [1; v*(p(X) - p0)];  
         
                       dq/dt = M0*q + u(1)*M1{1}*q + ...;  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/spm_mfa_bi.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mfa_bi", *args, **kwargs)
