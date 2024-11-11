from spm.__wrapper__ import Runtime


def spm_dcm_erp_data(*args, **kwargs):
    """
      Prepare structures for forward model(EEG, MEG and LFP)  
        FORMAT DCM = spm_dcm_erp_data(DCM,ERP)  
        DCM  - DCM structure  
        ERP  - switch to average over trials (default)  
         
        requires  
         
           DCM.xY.Dfile        - data file  
           DCM.options.trials  - trial codes  
           DCM.options.Tdcm    - Peri-stimulus time window  
           DCM.options.D       - Down-sampling  
           DCM.options.han     - Hanning  
           DCM.options.h       - Order of (DCT) detrending  
         
        sets  
           DCM.xY.modality - 'MEG','EEG' or 'LFP'  
           DCM.xY.Time     - Time [ms] data  
           DCM.xY.pst      - Time [ms] of down-sampled data  
           DCM.xY.dt       - sampling in seconds (s)  
           DCM.xY.y        - cell array of trial-specific response {[ns x nc]}  
           DCM.xY.It       - Indices of (ns) time bins  
           DCM.xY.Ic       - Indices of (nc) good channels  
           DCM.xY.name     - names of (nc) channels  
           DCM.xY.scale    - scalefactor applied to raw data  
           DCM.xY.coor2D   - 2D coordinates for plotting  
           DCM.xY.X0       - (DCT) confounds  
           DCM.xY.R        - Residual forming matrix (with hanning)  
           DCM.xY.Hz       - Frequency bins (for Wavelet transform)  
           DCM.options.h  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_erp_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_erp_data", *args, **kwargs)
