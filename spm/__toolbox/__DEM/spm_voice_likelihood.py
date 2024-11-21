from spm.__wrapper__ import Runtime


def spm_voice_likelihood(*args, **kwargs):
    """
      Return the lexical likelihood  
        FORMAT [L,M,N] = spm_voice_likelihood(xY,w)  
         
        xY   - word structure array  
        w    - indices of words in VOX.LEX to consider  
         
        assumes the following structures are in the global structure VOX  
        VOX.LEX  - lexical structure array  
        VOX.PRO  - prosody structure array  
        VOX.WHO  - speaker structure array  
         
        L    - log likelihood over lexicon  
        M    - log likelihood over prodidy  
        M    - log likelihood over speaker  
         
        This routine returns the log likelihood of a word and prosody based upon  
        a Gaussian mixture model; specified in terms of a prior expectation and  
        precision for each word (or prosody).  Prosody is categorised over  
        several  dimensions (i.e., eigenmodes).  For both lexical and prosody,  
        likelihoods are evaluated based upon the deviations from the expected  
        parameters, over all words and prosody dimensions.  
         
        The likelihood can be estimated directly under the assumption of  
        negligible random fluctuations on acoustic samples. Alternatively,  
        parametric empirical Bayes (PEB) can be used to estimate observation  
        noise, followed by Bayesian model reduction (BMR) to evaluate the  
        (marginal) likelihood. In normal operation, the explicit likelihood  
        scheme is used, with the opportunity to model the effects of (speech) in  
        noise with an additional variable: VOX.noise (see main body of script).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_likelihood.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_likelihood", *args, **kwargs)
