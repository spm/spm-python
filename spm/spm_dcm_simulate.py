from spm.__wrapper__ import Runtime


def spm_dcm_simulate(*args, **kwargs):
    """
      Populate the given group DCM array (GCM) with simulated data  
        FORMAT [GCM,gen] = spm_dcm_simulate(GCM, mode, noise, gen_idx)  
          
        If each subject has M models, any one of these M can be chosen to be the  
        generative model, and all models for the same subject will be assigned  
        the same simulated data.  
         
        GCM  - subjects x model cell array where the Ep structure contains  
               connection strengths  
         
        mode - zero-mean Gaussian noise is added, defined by one of:  
               'SNR_var' - signal-to-noise ratio based on the variance  
               'SNR_std' - signal-to-noise ratio based on the standard deviation  
               'var'     - variance of the observation noise to be added  
               'Ce'      - picks up the log noise precision from GCM{x}.Ce  
                          [default]  
         
        noise - real-valued added noise (interpretation depends on mode, above)  
                if mode is set to 'hE' then this can be empty  
         
        gen_idx - index of the generative model  
         
        Returns:  
         
        GCM  - DCM array populated with simulated data  
        gen  - vector of generative models for each subject  
         
        Example:  
        DCM = spm_dcm_simulate(GCM, 'SNR_std', 1);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_simulate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_simulate", *args, **kwargs)
