from spm.__wrapper__ import Runtime


def spm_reml_A(*args, **kwargs):
    """
      ReML estimation of covariance components from y*y' - factored components  
        FORMAT [C,h,Ph,F,Fa,Fc] = spm_reml_A(YY,X,Q,N,[hE,hC,V])  
         
        YY  - (m x m) sample covariance matrix Y*Y'  {Y = (m x N) data matrix}  
        X   - (m x p) design matrix  
        Q   - {1 x q} covariance components (factors)  
        N   - number of samples  
         
        hE  - hyperprior expectation [default = 0]  
        hC  - hyperprior covariance  [default = 256]  
        V   - fixed covariance component  
         
        C   - (m x m) estimated errors: C = A*A': A = h(1)*Q{1} + h(2)*Q{2} + ...  
        h   - (q x 1) ReML hyperparameters h  
        Ph  - (q x q) conditional precision of h  
         
        F   - [-ve] free energy F = log evidence = p(Y|X,Q) = ReML objective  
         
        Fa  - accuracy  
        Fc  - complexity (F = Fa - Fc)  
         
        Performs a Fisher-Scoring ascent on F to find MAP variance parameter  
        estimates. NB: uses weakly informative normal hyperpriors on the factors.  
         
       __________________________________________________________________________  
         
        SPM ReML routines:  
         
             spm_reml:    no positivity constraints on covariance parameters  
             spm_reml_sc: positivity constraints on covariance parameters  
             spm_sp_reml: for sparse patterns (c.f., ARD)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_reml_A.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_reml_A", *args, **kwargs)
