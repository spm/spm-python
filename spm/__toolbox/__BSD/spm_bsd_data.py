from spm._runtime import Runtime


def spm_bsd_data(*args, **kwargs):
    r"""
      Cross-spectral density data-features using a VAR model  
        FORMAT BSD = spm_BSD_csd_data(BSD)  
        BSD    -  BSD structure  
        requires  
         
           BSD.xY.Dfile        - name of data file  
           BSD.M.U             - channel subspace  
           BSD.options.trials  - trial to evaluate  
           BSD.options.Tdcm    - time limits  
           BSD.options.Fdcm    - frequency limits  
           BSD.options.D       - Down-sampling  
         
        sets  
         
           BSD.xY.pst     - Peristimulus Time [ms] sampled  
           BSD.xY.dt      - sampling in seconds [s] (down-sampled)  
           BSD.xY.U       - channel subspace  
           BSD.xY.y       - cross spectral density over sources  
           BSD.xY.csd     - cross spectral density over sources  
           BSD.xY.It      - Indices of time bins  
           BSD.xY.Ic      - Indices of good channels  
           BSD.xY.Hz      - Frequency bins  
           BSD.xY.code    - trial codes evaluated  
       __________________________________________________________________________  
         
        Original code: spm_dcm_csd.m - Karl Friston  
        Adapted by: Johan Medrano  
        Copyright (C) 2024-2025 Wellcome Centre for Human Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/spm_bsd_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bsd_data", *args, **kwargs)
