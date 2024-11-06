from spm.__wrapper__ import Runtime


def spm_dcm_sessions(*args, **kwargs):
    """
      Apply contrast vector to multiple DCM models  
        FORMAT spm_dcm_sessions  
         
        Contrasts are specified interactively and applied to a  
        number of DCM models. This routine can be used, for example,  
        to do Bayesian fixed or random effects analysis on   
        contrasts of DCM parameters.  
         
        This function returns p-values for one-sided t-tests. The Bayesian   
        probabilities are p(effect_size > threshold) where the   
        threshold is specified by the user. If you wish to test for   
        effects being smaller than a threshold you can use negative   
        values when you specify the contrasts. p-values for two-sided  
        tests are twice as large.  
         
        In Bayesian fixed effects analysis the mean estimates from  
        each DCM are weighted by their relative precision. Bayesian  
        random effects analysis is based on the between-model variance.  
        If the threshold is 0, and p is the random effects p-value   
        from classical inference then the Bayesian RFX probability value  
        is 1-p. As usual, only the random effects procedures allow   
        you to make an inference about the population from which the   
        data (eg. subjects) are drawn.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_sessions.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_sessions", *args, **kwargs, nargout=0)
