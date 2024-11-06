from spm.__wrapper__ import Runtime


def spm_fn_reml(*args, **kwargs):
    """
      ReML estimation of covariance components from y*y'  
        FORMAT [C,h,Ph,F] = spm_fn_reml(YY,X,Q,N,hE,K);  
         
        YY  - (m x m) sample covariance matrix Y*Y'  {Y = (m x N) data matrix}  
        X   - (m x p) design matrix  
        Q   - inline function or script C = Q(h,m)  
        N   - number of samples  
         
        hE  - prior expectation (& starting estimate for Q(h,m))  
        K   - maxmium number of iterations  
         
        C   - (m x m) estimated errors: C = Q(h)  
        h   - (q x 1) ReML hyperparameters h  
        Ph  - (q x q) conditional precision of h  
         
        F   - [-ve] free energy F = log evidence = p(Y|X,Q) = ReML objective  
         
        Performs a Fisher-Scoring ascent on F to find ReML variance parameter  
        estimates.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fn_reml.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_fn_reml", *args, **kwargs)
