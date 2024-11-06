from spm.__wrapper__ import Runtime


def spm_voice_iQ(*args, **kwargs):
    """
      Discrete cosine transform of formant coefficients  
        FORMAT [W] = spm_voice_iQ(Q)  
         
        Q     - log formant frequencies  
        G(1)  - log formant (pitch) Tu  
        G(2)  - log timing  (pitch) Tv  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_iQ.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_iQ", *args, **kwargs)
