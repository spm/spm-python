from spm.__wrapper__ import Runtime


def spm_compare_families(*args, **kwargs):
    """
      Bayesian comparison of model families for group studies   
        FORMAT [family,model] = spm_compare_families(lme,family)  
         
        INPUT:  
         
        lme           - array of log model evidences   
                          rows: subjects  
                          columns: models (1..N)  
         
        family        - data structure containing family definition and inference parameters:  
                         .infer='RFX' or 'FFX' (default)  
                         .partition  [1 x N] vector such that partition(m)=k signifies that  
                                     model m belongs to family k (out of K) eg. [1 1 2 2 2 3 3]  
                         .names      cell array of K family names eg, {'fam1','fam2','fam3'}  
                         .Nsamp      RFX only: Number of samples to get (default=1e4)  
                         .prior      RFX only: 'F-unity' alpha0=1 for each family (default)  
                                     or 'M-unity' alpha0=1 for each model (not advised)  
         
        OUTPUT:  
         
        family        - RFX only:    
                          .alpha0       prior counts   
                          .exp_r        expected value of r  
                          .s_samp       samples from posterior  
                          .xp           exceedance probs  
                       - FFX only:   
                          .prior        family priors  
                          .post         family posteriors  
         
        model          - RFX only:   
                          .alpha0        prior counts  
                          .exp_r         expected value of r  
                          .r_samp        samples from posterior  
                       - FFX only:   
                          .subj_lme      log model ev without subject effects  
                          .prior         model priors  
                          .like          model likelihoods   
                                         (likelihood scaled to unity for most  
                                         likely model)  
                          .posts         model posteriors  
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_compare_families.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_compare_families", *args, **kwargs)
