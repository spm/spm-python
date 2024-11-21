from spm.__wrapper__ import Runtime


def spm_BMS_bor(*args, **kwargs):
    """
      Compute Bayes Omnibus Risk  
        FORMAT [bor,F0,F1] = spm_BMS_bor(L,posterior,priors,C)  
         
        L         Log model evidence table (models x  subjects)  
        posterior .a model counts, .r model-subject probs  
        priors    .a model counts  
        C         if this field is specified then BOR under family prior   
                  is computed, otherwise BOR under model prior is computed.  
                  C(k,f) = 1 if model k belongs to family f (0 otherwise)  
         
        REFERENCES:  
         
        Rigoux, L, Stephan, KE, Friston, KJ and Daunizeau, J. (2014)  
        Bayesian model selection for group studies - Revisited.   
        NeuroImage 84:971-85. doi: 10.1016/j.neuroimage.2013.08.065  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_BMS_bor.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_BMS_bor", *args, **kwargs)
