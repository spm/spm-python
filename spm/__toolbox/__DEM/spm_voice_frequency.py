from spm.__wrapper__ import Runtime


def spm_voice_frequency(*args, **kwargs):
    """
      Segmentation of timeseries at fundamental frequency  
        FORMAT [I] = spm_voice_frequency(Y,FS,F0)  
         
        Y    - timeseries  
        FS   - sampling frequency  
        F0   - fundamental frequency (glottal pulse rate)  
         
        I    - intervals (time bins): mean(I) = DI = FS/F0  
         
        This routine  identifies the the sampling intervals at the fundamental  
        frequency, based upon the maxima after band-pass filtering around F0;  
        namely, inflection or fluctuations in fundamental wavelength (i.e.,  
        glottal pulse rate).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_frequency.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_frequency", *args, **kwargs)
