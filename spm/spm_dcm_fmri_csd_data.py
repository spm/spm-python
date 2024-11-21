from spm.__wrapper__ import Runtime


def spm_dcm_fmri_csd_data(*args, **kwargs):
    """
      Get cross-spectral density data-features using a VAR model  
        FORMAT DCM = spm_dcm_fmri_csd_data(DCM)  
        DCM    -  DCM structure or fMRI  
         
        sets  
         
           DCM.Y.pst     - Peristimulus Time [ms] sampled  
           DCM.Y.dt      - sampling in seconds [s] (down-sampled)  
           DCM.Y.csd     - cross spectral density over sources  
           DCM.Y.Hz      - Frequency bins  
         
           DCM.U.csd     - cross spectral density of inputs  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_fmri_csd_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fmri_csd_data", *args, **kwargs)
