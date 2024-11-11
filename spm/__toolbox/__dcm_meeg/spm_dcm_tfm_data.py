from spm.__wrapper__ import Runtime


def spm_dcm_tfm_data(*args, **kwargs):
    """
      Get cross-spectral density data-features using a wavelet transform  
        FORMAT DCM = spm_dcm_tfm_data(DCM)  
        DCM    -  DCM structure  
        requires  
         
           DCM.xY.Dfile        - name of data file  
           DCM.M.U             - channel subspace  
           DCM.options.trials  - trial to evaluate  
           DCM.options.Tdcm    - time limits  
           DCM.options.Fdcm    - frequency limits  
           DCM.options.D       - Down-sampling  
         
        sets  
         
           DCM.xY.pst     - Peristimulus Time [ms] sampled  
           DCM.xY.dt      - sampling in seconds [s] (down-sampled)  
           DCM.xY.U       - channel subspace  
           DCM.xY.y       - cross spectral density over channels  
           DCM.xY.csd     - cross spectral density over channels  
           DCM.xY.erp     - event-related average over channels  
           DCM.xY.It      - Indices of time bins  
           DCM.xY.Ic      - Indices of good channels  
           DCM.xY.Hz      - Frequency bins  
           DCM.xY.code    - trial codes evaluated  
           DCM.xY.scale   - scalefactor applied to data  
           DCM.xY.Rft     - Wavelet number or ratio of frequency to time  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_tfm_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_tfm_data", *args, **kwargs)
