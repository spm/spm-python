from spm.__wrapper__ import Runtime


def spm_voice_Q(*args, **kwargs):
    """
      Inverse discrete cosine transform of formant coefficients  
        FORMAT [Q,U,V] = spm_voice_Q(W,G,Ni,ni)  
         
        W     - log formant coefficients (weights)  
        G(1)  - log formant (pitch) Tu  
        G(2)  - log timing  (pitch) Tv  
        G(3)  - amplitude   (pitch) Tw  
        Ni    - number of formant frequencies  
        ni    - number of timing  intervals  
         
        Q     - formants (time-frequency representation): Q = U*xY.W*V'  
        U     - DCT over frequency  
        V     - DCT over intervals  
         
        This  auxiliary routine scales and transforms log formant coefficients  
        using a pair of discrete cosine transforms with logarithmic scaling.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_Q.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_Q", *args, **kwargs)
