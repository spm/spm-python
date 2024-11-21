from spm.__wrapper__ import Runtime


def spm_voice_iff(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_iff.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_iff", *args, **kwargs)
