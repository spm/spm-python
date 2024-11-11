from spm.__wrapper__ import Runtime


def spm_dcm_phase_data(*args, **kwargs):
    """
      Get data for DCM for phase coupling  
        FORMAT [DCM] = spm_dcm_phase_data(DCM)  
         
        DCM    -  DCM structure  
         
        Requires/requests:  
         
           DCM.xY.Dfile   - M/EEG data filename  
           DCM.Lpos       - Matrix of source locations  
           DCM.options.trials - To select particular trials (otherwise all selected)  
           DCM.options.Fdcm   - to select frequency window for analysis  
           DCM.options.Hdcm - to select time window for filtering and Hilbert transform  
                              default=[beginning of epoch, end of epoch]   
           DCM.options.Tdcm - to select time window for phase-coupling analysis  
           DCM.options.filter_order - order of bandpass filter  
           DCM.options.Nmodes - specify sub-sampling of trials eg  
                                  Nmodes=2 to use every other trial. This can  
                                  speed up model fitting. Default value=1.  
         
        Sets  
         
           DCM.xY.pst     - Peristimulus Time [ms] of time-frequency data  
           DCM.xY.dt      - sampling in seconds [s]  
           DCM.xY.y       - concatenated induced response over sources  
           DCM.xY.Ic      - Indices of good channels  
         
           DCM.xY.y{i}(k,l) - Phase data for i-th trial,l-th source,k-th time-bin  
         
         
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_phase_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_phase_data", *args, **kwargs)
