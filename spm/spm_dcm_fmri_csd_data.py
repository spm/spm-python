from spm._runtime import Runtime


def spm_dcm_fmri_csd_data(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_fmri_csd_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_fmri_csd_data", *args, **kwargs)
