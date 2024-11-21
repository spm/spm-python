from spm.__wrapper__ import Runtime


def spm_bms_ttest(*args, **kwargs):
    """
      Log Bayes Factor against null for one sample t-test  
        FORMAT [logbf,t] = spm_bms_ttest(y,prior)  
          
        y         [N x 1] data vector  
        prior     'jzs' (default), 'unit'  
         
        logbf     Log Bayes Factor   
        t         t-statistic  
         
        Default prior is 'jzs'. The different priors are described in  
        [1] Rouder et al. (2009) Psych Bull Rev, 16(2),225-237.  
         
        These tests consider the quantity d = mean / standard deviation.   
        The unit information prior, 'unit', uses a zero mean unit variance   
        Gaussian prior over d (the prior variance of d, sig_d^2, is unity).  
         
        The (Jeffreys-Zellner-Snow) JZS prior, 'jzs', uses a Cauchy over d   
        and an inverse chi^2 over sig_d^2.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bms_ttest.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_bms_ttest", *args, **kwargs)
