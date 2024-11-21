from spm.__wrapper__ import Runtime


def spm_voice_onset(*args, **kwargs):
    """
      Identify intervals containing acoustic energy and post onset minima  
        FORMAT [i] = spm_voice_onset(Y,FS,u,v)  
         
        Y    - timeseries  
        FS   - sampling frequency  
        u,v  - thresholds for onset and offset [default: 1/16]  
         
        i    - intervals (time bins) containing spectral energy  
         
        This routine identifies epochs constaining spectral energy in the power  
        envelope, defined as the root mean square (RMS) power. The onset and  
        offset of words is evaluated in terms of the first and last threshold  
        crossings.  
         
        This routine is a simple version of spm_voice_onset and is retained for  
        diagnostic purposes.  
         
        see also: spm_voice_onsets.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_onset.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_onset", *args, **kwargs)
