from spm.__wrapper__ import Runtime


def spm_dcm_bmc(*args, **kwargs):
    """
      Bayesian model comparison  
        FORMAT [post,exp_r,xp,pxp,bor,F] = spm_dcm_bmc(DCM)  
         
        DCM     - {subjects x models} cell array of DCMs  
        ------------------------------------------------  
            DCM{i,j}.F  - free energy  
         
        OUTPUTS  
        -------  
        post    - FFX posterior model probabilities p(m|y)  
        exp_r   - RFX expectation of the posterior  p(m|y)  
        xp      - RFX exceedance probabilities  
        pxp     - RFX protected exceedance probabilities  
        bor     - RFX Bayes Omnibus Risk (probability that model frequencies   
                  are equal)  
        F       - matrix of free energies (subjects x models)  
         
        This routine computes fixed and random effects posterior probabilities  
        over models. It also returns exceedance  probabilities and protected  
        statistics.  
          
        See also: spm_dcm_bma.m and spm_BMS.m  
       __________________________________________________________________________  
          
        References:  
         
        Stephan KE, Penny WD, Daunizeau J, Moran RJ, Friston KJ (2009)  
        Bayesian Model Selection for Group Studies. NeuroImage 46:1004-1017  
         
        Rigoux, L, Stephan, KE, Friston, KJ and Daunizeau, J. (2014)  
        Bayesian model selection for group studies - Revisited.   
        NeuroImage 84:971-85. doi: 10.1016/j.neuroimage.2013.08.065  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_bmc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_bmc", *args, **kwargs)
