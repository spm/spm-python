from spm._runtime import Runtime


def spm_vb_roi_anova(*args, **kwargs):
    r"""
      Bayesian ANOVA for a region of interest  
        FORMAT [post,model] = spm_vb_roi_anova (VOI_fname,SPM,factor)  
         
        VOI_fname   - VOI filename  
        SPM         - SPM data structure  
        factor      - data structure relating conditions to levels of factors  
         
        model       - data structure describing models  
                      (m).F             model evidence  
                      (m).X             design matrix  
        post        - Posterior probabilities of  
                      .factor1        main effect of factor 1  
                      .factor2        main effect of factor 2  
                      .interaction    interaction  
                      .average        average  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_vb_roi_anova.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_roi_anova", *args, **kwargs)
