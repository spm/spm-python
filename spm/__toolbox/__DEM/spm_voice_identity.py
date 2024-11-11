from spm.__wrapper__ import Runtime


def spm_voice_identity(*args, **kwargs):
    """
      Evaluate the fundamental and formant frequencies of a speaker  
        FORMAT [F0,F1] = spm_voice_identity(wfile,P)  
         
        wfile  - .wav file, audiorecorder object or (double) time series  
        P      - prior probability of first word  
         
        F0     - fundamental frequency  
        F1     - expected format frequency  
         
        NB: automatically updates VOX.F0 and VOX.F1 when called  
         
        This routine estimates the fundamental and formant frequencies based upon  
        a spoken word source. This routine is used in conjunction with  
        spm_voice_fundamental to provide a more refined estimate of fundamental  
        and first formant frequencies based upon speech with known lexical  
        content.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_identity.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_identity", *args, **kwargs)
