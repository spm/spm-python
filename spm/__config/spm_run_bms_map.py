from spm.__wrapper__ import Runtime


def spm_run_bms_map(*args, **kwargs):
    """
      Run Bayesian Model Selection Maps  
        SPM job execution function  
        takes a harvested job data structure and calls SPM functions to perform  
        Bayesian Inference for Model Selection of Log. Evidence Maps    
        Input:  
        job    - harvested job data structure (see matlabbatch help)  
        Output:  
        out    - computation results, usually a struct variable.  
         
         
        Bayesian Inference on Model Space:  
         
        The Random-effects 'RFX' method is described in Stephan et al. [1]   
        'Bayesian Model Selection for Group Studies'.  
        Output files (for each model):   
              BMS.mat   
              Exceedance Probability Maps (*epm.<ext>),  
              Posterior Probability Maps (*ppm.<ext>),  
              Dirichlet Parameters (alpha) Maps (*alpha.<ext>).  
         
        The Fixed-effects 'FFX' method adds together the log-evidences over   
        subjects/sessions for each group, then compares the group log-ev's.   
        This is also known as the Group Bayes Factor (GBF) approach [2].   
        Output files (for each model):  
              BMS.mat   
              Posterior Probability Maps (*ppm.<ext>).  
         
        BMS contains:  
            BMS.fname  
            BMS.map.ffx(rfx).data  
            BMS.map.ffx(rfx).ppm   
            BMS.map.ffx(rfx).xppm     - only for RFX (this is the expected posterior  
                                        probability map ie. posterior mean)  
            BMS.map.ffx(rfx).epm      - only for RFX (optional) - this is the   
                                        exceedance probability map   
            BMS.map.ffx(rfx).alpha    - only for RFX  
         
        [1] Rosa et al., 2009, Bayesian Model Selection Maps for Group Studies,  
        NeuroImage.  
        [2] Stephan et al., 2009, Bayesian Model Selection for Group Studies,  
        NeuroImage.  
        [3] Penny et al., 2004, Comparing Dynamic Causal Models, NeuroImage.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_run_bms_map.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_run_bms_map", *args, **kwargs)
