from spm.__wrapper__ import Runtime


def spm_ar_reml(*args, **kwargs):
    """
      ReML estimation of covariance components from y*y'  
        FORMAT [C,h,Ph,F] = spm_ar_reml(YY,X,m,N)  
         
        YY  - (m x m) sample covariance matrix Y*Y'  {Y = (m x N) data matrix}  
        X   - (m x p) design matrix  
        m   - (1) order of AR(m) model  
        N   - number of samples  
         
         
        C   - (m x m) estimated errors = h(1)*Q{1} + h(2)*Q{2} + ...  
        h   - (q x 1) ReML hyperparameters h: normalised AR coefficients  
        Ph  - (q x q) conditional precision of h (unnormalised)  
         
        F   - [-ve] free energy F = log evidence = p(Y|X,Q) = ReML objective  
         
        Performs a Fisher-Scoring ascent on F to find ReML variance parameter  
        estimates.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ar_reml.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_ar_reml", *args, **kwargs)
