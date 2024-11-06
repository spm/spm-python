from spm.__wrapper__ import Runtime


def spm_reml(*args, **kwargs):
    """
      ReML estimation of [improper] covariance components from y*y'  
        FORMAT [C,h,Ph,F,Fa,Fc] = spm_reml(YY,X,Q,N,t,hE,hP)  
         
        YY  - (m x m) sample covariance matrix Y*Y'  {Y = (m x N) data matrix}  
        X   - (m x p) design matrix  
        Q   - {1 x q} covariance components  
         
        N   - number of samples                 [default: 1]  
        t   - regularisation                    [default: 4]  
        hE  - hyperprior                        [default: 0]  
        hP  - hyperprecision                    [default: exp(-8)]  
         
        C   - (m x m) estimated errors = h(1)*Q{1} + h(2)*Q{2} + ...  
        h   - (q x 1) posterior expectation of h  
        Ph  - (q x q) posterior precision of h  
         
        F   - [-ve] free energy F = log evidence = p(Y|X,Q) = ReML objective  
         
        Fa  - accuracy  
        Fc  - complexity (F = Fa - Fc)  
         
        Performs a Fisher-Scoring ascent on F to find ReML variance parameter  
        estimates.  
         
        see also: spm_reml_sc for the equivalent scheme using log-normal  
        hyperpriors  
       __________________________________________________________________________  
         
        SPM ReML routines:  
         
             spm_reml:    no positivity constraints on covariance parameters  
             spm_reml_sc: positivity constraints on covariance parameters  
             spm_sp_reml: for sparse patterns (c.f., ARD)  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_reml.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_reml", *args, **kwargs)
