from spm._runtime import Runtime


def spm_voice_iQ(*args, **kwargs):
    r"""
      Discrete cosine transform of formant coefficients  
        FORMAT [W] = spm_voice_iQ(Q)  
         
        Q     - log formant frequencies  
        G(1)  - log formant (pitch) Tu  
        G(2)  - log timing  (pitch) Tv  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/spm_voice_iQ.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_voice_iQ", *args, **kwargs)
