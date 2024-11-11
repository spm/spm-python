from spm.__wrapper__ import Runtime


def spm_voice_ff(*args, **kwargs):
    """
      Decomposition at fundamental frequency  
        FORMAT [xY] = spm_voice_ff(Y,FS)  
         
        Y      - timeseries  
        FS     - sampling frequency  
         
        requires the following in the global VOX structure:  
        VOX.F0 - fundamental frequency (glottal pulse rate)  
        VOX.F1 - format frequency  
         
        output structure  
       --------------------------------------------------------------------------  
        xY.Y   - timeseries  
        xY.W   - parameters - lexical  
        xY.P   - parameters - prosody  
          
        xY.P.amp - log amplitude  
        xY.P.dur - log duration (sec)  
        xY.P.lat - log latency  (sec)  
        xY.P.tim - log timbre (a.u.)  
        xY.P.pch - log pitch  (a.u.)  
        xY.P.inf - inflection (a.u.)  
         
        xY.R.F0  - fundamental frequency (Hz)  
        xY.R.F1  - format frequency (Hz  
         
        This routine transforms a timeseries using a series of discrete cosine  
        transforms and segmentations into a set of lexical and prosody  
        parameters. Effectively, this is a rather complicated sequence of  
        straightforward operations that constitute a parameterised nonlinear  
        mapping from a parameter space to a timeseries corresponding to a spoken  
        word. In brief, the transform involves identifying the interval  
        containing the words spectral energy and dividing it up into a sequence  
        of  fundamental segments (at the fundamental frequency or glottal pulse  
        rate). The spectral content (or form of transient) for each segment is  
        characterised in terms of the cross covariance function whose length is  
        determined by the fundamental format frequency. The resulting matrix  its  
        parameterised with even functions based upon a discrete cosine transform.  
        Because the basis functions are even (i.e., symmetrical) the resulting  
        coefficients are nonnegative. In turn, this allows a log transform  and  
        subsequent normalisation, by a scaling (timbre) parameter. The normalised  
        log format coefficients are finally parameterised using two discrete  
        cosine transforms over time, within and between segments, respectively.  
        This provides a sufficiently rich parameterisation to generate reasonably  
        realistic timeseries. The  fluctuations in the fundamental frequency  
        between segments are parameterised with another discrete cosine  
        transform. This has two key parameters that model inflection. Please see  
        the annotated code below for further details.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/spm_voice_ff.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_voice_ff", *args, **kwargs)
