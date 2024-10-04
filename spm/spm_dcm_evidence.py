from spm.__wrap__ import _Runtime


def spm_dcm_evidence(*args, **kwargs):
  """  Compute evidence of DCM model  
    FORMAT evidence = spm_dcm_evidence(DCM)  
     
    DCM       - DCM data structure  
     
    evidence  - structure with the following fields  
      .region_cost(i)  - The cost of prediction errors in region i  
      .bic_penalty     - Bayesian information criterion penalty  
      .bic_overall     - The overall BIC value  
      .aic_penalty     - Akaike's information criterion penalty  
      .aic_overall     - The overall AIC value  
     
    All of the above are in units of NATS (not bits).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_dcm_evidence.m)
  """

  return _Runtime.call("spm_dcm_evidence", *args, **kwargs)
