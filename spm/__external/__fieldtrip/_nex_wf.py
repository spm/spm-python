from spm._runtime import Runtime


def _nex_wf(*args, **kwargs):
    r"""
      nex_wf(filename, varname): Read waveform variable from a .nex file  
         
        [adfreq, n, ts, nf, w] = nex_wf(filename, varname)  
         
        INPUT:  
          filename - if empty string, will use File Open dialog  
          varname - variable name  
         
                    
        OUTPUT:  
          n - number of waveforms  
          ts - array of waveform timestamps (in seconds)  
          nf - number of data points in each waveform  
          w - matrix of waveform a/d values [n nf] (in millivolts)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/nex_wf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("nex_wf", *args, **kwargs)
