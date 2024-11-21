from spm.__wrapper__ import Runtime


def spm_dcm_ind_data(*args, **kwargs):
    """
      Get time-frequency amplitude at specified sources for DCM  
        FORMAT DCM = spm_dcm_ind_data(DCM)  
        DCM    -  DCM structure  
        requires:  
         
           DCM.xY.Dfile       - Data file  
           DCM.options.trials - Trial indices, array(m)  
           DCM.Lpos           - Priors on source location, array(3, n)  
         
        optional:  
           DCM.options.Fmodes   - Number of frequency modes, default 8  
           DCM.options.Tdcm     - Peristimulus time window, array(2)   
                                    default: [D.time(1) + 512 D.time(end) - 512]  
           DCM.options.Fdcm     - Frequency window, array(2)  
                                    default: see line 178  
           DCM.options.D        - Downsampling factor, default 2  
           DCM.options.Rft      - Number of wavelet coefficients, default 6  
           DCM.options.h        - Order of the polynomial basis for detrending  
                                   default 1 (mean and linear trend)  
           DCM.options.baseline - Baseline window, array(2), [start(ms) end(ms)]  
                                   default, first eighth of pst bins   
         
        sets  
         
           DCM.xY.pst     - Peristimulus Time [ms] of time-frequency data  
           DCM.xY.dt      - sampling in seconds [s]  
           DCM.xY.y       - concatenated induced response over sources  
           DCM.xY.xf      - induced response over sources  
           DCM.xY.It      - Indices of time bins  
           DCM.xY.Ic      - Indices of good channels  
           DCM.xY.Hz      - Frequency bins (for Wavelet transform)  
           DCM.xY.Mz      - Mean frequency response over trial and sources  
           DCM.xY.Rft     - wavelet coefficient  
           DCM.xY.Nm      - number of frequency modes  
           DCM.xY.U       - Frequency modes  
           DCM.xY.S       - and their singular values  
         
           DCM.xY.y{i}(k,l)    = l-th region X frequency mode (fast over regions)  
                                 k-th time-bin  
                                 i-th trial  
         
           DCM.xY.xf{i,j}(k,l) = l-th frequency mode  
                                 k-th time-bin  
                                 j-th region  
                                 i-th trial  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_ind_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_ind_data", *args, **kwargs)
