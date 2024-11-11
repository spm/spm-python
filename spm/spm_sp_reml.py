from spm.__wrapper__ import Runtime


def spm_sp_reml(*args, **kwargs):
    """
      ReML estimation of covariance components from y*y' (for sparse patterns)  
        FORMAT [C,h,Ph,F,Fa,Fc] = spm_sp_reml(YY,X,Q,N);  
         
        YY  - (m x m) sample covariance matrix Y*Y'  {Y = (m x N) data matrix}  
        X   - (m x p) design matrix  
        Q   - {1 x q} components Q.q = eigenvectors; Q.v = eigenvalues  
                      or (m x n) matrix of n basis functions  
        N   - number of samples  
         
        C   - (m x m) estimated errors = h(1)*Q{1} + h(2)*Q{2} + ...  
        h   - (q x 1) ReML hyperparameters h  
        Ph  - (q x q) conditional precision of log(h)  
         
        F   - [-ve] free energy F = log evidence = p(Y|X,Q) = ReML objective  
         
        Fa  - accuracy  
        Fc  - complexity (F = Fa - Fc)  
         
        Performs a Fisher-Scoring ascent on F to find ReML variance parameter  
        estimates, using uninformative hyperpriors (this is effectively an ARD  
        scheme).  The specification of components differs from spm_reml and  
        spm_reml_sc.  
         
       __________________________________________________________________________  
         
        SPM ReML routines:  
         
             spm_reml:    no positivity constraints on covariance parameters  
             spm_reml_sc: positivity constraints on covariance parameters  
             spm_sp_reml: for sparse patterns (c.f., ARD)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sp_reml.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sp_reml", *args, **kwargs)
