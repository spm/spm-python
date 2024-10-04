from spm.__wrap__ import _Runtime


def spm_vb_roi_anova(*args, **kwargs):
  """  Bayesian ANOVA for a region of interest  
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
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_roi_anova.m)
  """

  return _Runtime.call("spm_vb_roi_anova", *args, **kwargs)
