from spm._runtime import Runtime


def spm_eeg_downsample(*args, **kwargs):
    r"""
      Downsample M/EEG data  
        FORMAT D = spm_eeg_downsample(S)  
         
        S               - optional input struct  
        (optional) fields of S:  
          S.D           - MEEG object or filename of M/EEG mat-file  
          S.method      - resampling method. Can be  'resample' [default],  
                          'decimate', 'downsample', 'fft'  
          S.fsample_new - new sampling rate, must be lower than the original one  
          S.prefix      - prefix for the output file [default: 'd']  
         
        D               - MEEG object (also written on disk)  
       __________________________________________________________________________  
         
        This function uses the Signal Processing toolbox from The MathWorks:  
                      http://www.mathworks.com/products/signal/  
        (function resample.m) if present and spm_timeseries_resample.m otherwise.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_downsample.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_downsample", *args, **kwargs)
