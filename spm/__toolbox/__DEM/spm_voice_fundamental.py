from spm.__wrapper__ import Runtime


def spm_voice_fundamental(*args, **kwargs):
    """
      Estimate and plot fundamental and format frequencies  
        FORMAT [F0,F1] = spm_voice_fundamental(Y,FS)  
         
        Y    - timeseries  
        FS   - sampling frequency  
         
        F0   - fundamental frequency (glottal pulse rate)  
        F1   - fundamental frequency (formant)  
         
        This auxiliary routine identifies the fundamental and formant  
        frequencies. The fundamental frequency is the lowest frequency (between  
        85 Hz and 300 Hz) that corresponds to the glottal pulse rate. the  
        fundamental frequency is identified as the frequency containing the  
        greatest spectral energy over the first few harmonics. The first format  
        frequency is based upon the frequency with the maximum spectral energy of  
        transients, centred on the fundamental intervals.  
         
        This routine is not used for voice recognition but can be useful for  
        diagnostic purposes.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_fundamental.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_fundamental", *args, **kwargs)
