from spm.__wrapper__ import Runtime


def spm_hdm_priors(*args, **kwargs):
    """
      Return priors for a hemodynamic dynamic causal model  
        FORMAT [pE,pC] = spm_hdm_priors(m,[h])  
        m   - number of inputs  
        h   - number of hemodynamic modes (default = 3)  
         
        pE  - prior expectations  
        pC  - prior covariances  
         
        (5) biophysical parameters  
           P(1) - signal decay                  d(ds/dt)/ds)  
           P(2) - autoregulation                d(ds/dt)/df)  
           P(3) - transit time                  (t0)  
           P(4) - exponent for Fout(v)          (alpha)  
           P(5) - resting oxygen extraction     (E0)  
           P(6) - ratio of intra- to extra-     (epsilon)  
                  vascular components of the  
                  gradient echo signal     
         
        plus (m) efficacy priors  
           P(7) - ....  
         
       ___________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_hdm_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_hdm_priors", *args, **kwargs)
