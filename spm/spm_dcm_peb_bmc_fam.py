from spm.__wrapper__ import Runtime


def spm_dcm_peb_bmc_fam(*args, **kwargs):
    """
      Bayesian model selection and averaging over families of PEB models  
         
        BMA - Bayesian model average (see spm_dcm_peb_bmc)  
          
                   BMA.K       - model space [models x parameters]  
                   BMA.Pnames  - parameter names  
                   BMA.Ep      - averaged parameters (for inferring #covariates)  
         
        BMR - model space (see spm_dcm_peb_bmc)  
         
                   BMR{i,j}    - model i of commonalities and j of differences  
                   BMR{i,j}.Ep - expectations of second level parameters  
                   BMR{i,j}.Cp - covariance of second level parameters  
                   BMR{i,j}.F  - free energy relative to full model  
         
        families - [1 x Nm] vector of family membership where families(i)=x,  
                   for model i and family x. For example, families=[1 1 2]  
                   means that models 1 and 2 are in family 1 and model 3 is in  
                   family 2.  
         
        bma_option - String specifying option for Bayesian Model Averaging  
         
                   'ALL'     - average over all models (under family priors)  
                   'WINNING' - average models in the best family only  
                   'NONE'    - don't average  
         
        Returns:  
         
        BMA - Bayesian Model Average over models (specified by bma_option)  
         
        fam - Bayesian model selection results:  
            
                  .model.post   - Posterior probability of each model  
                  .model.prior  - Prior probability of each model  
                  .family.post  - Posterior probability of each family  
                  .family.prior - Prior probability of each family  
                  .famdef       - Input vector of family assignments  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_peb_bmc_fam.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_peb_bmc_fam", *args, **kwargs)
