from spm.__wrapper__ import Runtime


def spm_bms_anova(*args, **kwargs):
    """
      Log Bayes factor against null for one-way ANOVA  
        FORMAT [logBF,F] = spm_bms_anova(y,group,prior)  
         
        y         [n x 1] data vector  
        group     [n x 1] vector with elements 1,2,3 etc. indicating group  
                  membership  
        prior     'jzs' (default) or 'unit'  
         
        logBF     LogBayesFactor in favour of alternative  
                  logBF < -3 : Accept null (no effect)  
                  logBF > +3 : Accept alternative (an effect)  
        F         F-statistic  
         
        Bayesian ANOVA from [1]  
        [1] Wetzels et al 2012, A default Bayesian Hypothesis test  
        for ANOVA designs, American Statistical Association, 66(2), 104-111.  
         
        For a single group this function calls spm_bms_ttest.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bms_anova.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_bms_anova", *args, **kwargs)
