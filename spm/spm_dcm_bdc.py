from spm.__wrapper__ import Runtime


def spm_dcm_bdc(*args, **kwargs):
    """
      Compare datasets using DCM and PEB (Bayesian data comparison)  
        FORMAT [d,BMA,PEBs] = spm_dcm_bdc(GCMs,field,M,ynames,models,noplot)  
         
        Performs the following procedure:  
         
        1. Identifies the optimum reduced model (PEB) collapsed over datasets.  
        2. For each dataset, creates reduced GCMs based on the optimum model  
           above and estimates a per-dataset PEB model.  
        3. Computes a series of measures on each dataset's PEB model  
         
        Inputs:  
         
        GCMs   - {1 x ny} cell array of filenames, each of which is a GCM file.  
        field  - {1 x nf} cell array of field names, e.g. {'A','B'}  
        M      - (Optional) struct for configuring PEB. See spm_dcm_peb.m .  
        M.gamma- (Optional) prior variance for switched off parameters when   
                 automatically forming a model space for KL-over-models.  
        M.bmr  - (Optional) if true, searches for an optimal model across all  
                 datasets before performing BDC. If false, all parameters from  
                 the DCM are included. [default: true];  
        ynames - (Optional) {1 x ny} cell array of names for each dataset  
        models - (Optional) model space to use for computing the information gain  
                 over models. Accepts a nested cell array of parameter names, or  
                 a binary matrix (models x parameters) with which parameters  
                 to switch on or off in each model.  
        noplot - (Optional) if true, does not show plots.  
         
        ny = number of datasets, nf = number of DCM fields, nm = number of models  
          
        Returns:  
          
        d.precisions - [np x ny] Precision of each DCM parameter in each dataset  
        d.dcm_negent - [1 x ny]  Negative entropy (certainty) of DCM parameters  
        d.rfx_negent - [1 x ny]  Negative entropy (certainty) of the estimated  
                                 between-subject variability  
        d.complexity - [1 x ny]  Number of effective parameters in the model  
        d.model_F    - [nm x ny] Free energy of each candidate model  
        d.model_P    - [nm x ny] Posterior probability of each candidate model  
        d.model_KL   - [1 x ny]  Ability to disriminate between similar models  
         
        BMA        - Bayesian model average across all datasets  
        PEBs       - [1 x ny] PEB for each dataset  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_bdc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_bdc", *args, **kwargs)
