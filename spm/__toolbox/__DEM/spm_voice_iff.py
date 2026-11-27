from spm._runtime import Runtime


def spm_voice_iff(*args, **kwargs):
    r"""
      Inverse decomposition at fundamental frequency  
        FORMAT [Y,W] = spm_voice_iff(xY)  
         
        xY    -  cell array of word structures  
        xY.W  -  parameters - lexical  
        xY.P  -  parameters - prosody  
        xY.R  -  parameters - speaker  
          
        xY.P.amp - log amplitude  
        xY.P.dur - log duration (sec)  
        xY.P.lat - log latency  (sec)  
        xY.P.tim - timbre     (a.u.)  
        xY.P.inf - inflection (a.u.)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_voice_iff.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_voice_iff", *args, **kwargs)
