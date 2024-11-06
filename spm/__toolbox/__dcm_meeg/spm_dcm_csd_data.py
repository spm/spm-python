from spm.__wrapper__ import Runtime


def spm_dcm_csd_data(*args, **kwargs):
    """
      Cross-spectral density data-features using a VAR model  
        FORMAT DCM = spm_dcm_csd_data(DCM)  
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
           DCM.xY.y       - cross spectral density over sources  
           DCM.xY.csd     - cross spectral density over sources  
           DCM.xY.It      - Indices of time bins  
           DCM.xY.Ic      - Indices of good channels  
           DCM.xY.Hz      - Frequency bins  
           DCM.xY.code    - trial codes evaluated  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_csd_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_csd_data", *args, **kwargs)
