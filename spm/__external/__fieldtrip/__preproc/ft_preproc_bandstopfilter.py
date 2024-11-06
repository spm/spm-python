from spm.__wrapper__ import Runtime


def ft_preproc_bandstopfilter(*args, **kwargs):
    """
      FT_PREPROC_BANDSTOPFILTER applies a band-stop filter to the data and thereby  
        removes the spectral components in the specified frequency band  
         
        Use as  
          [filt] = ft_preproc_bandstopfilter(dat, Fs, Fbp, order, type, dir, instabilityfix, df, wintype, dev, plotfiltresp, usefftfilt)  
        where  
          dat             data matrix (Nchans X Ntime)  
          Fs              sampling frequency in Hz  
          Fbp             frequency band, specified as [Fhp Flp] in Hz  
          N               optional filter order, default is 4 (but) or dependent on frequency band and data length (fir/firls)  
          type            optional filter type, can be  
                            'but'       Butterworth IIR filter (default)  
                            'firws'     FIR filter with windowed sinc  
                            'fir'       FIR filter using MATLAB fir1 function  
                            'firls'     FIR filter using MATLAB firls function (requires MATLAB Signal Processing Toolbox)  
                            'brickwall' frequency-domain filter using forward and inverse FFT  
          dir             optional filter direction, can be  
                            'onepass'                   forward filter only  
                            'onepass-reverse'           reverse filter only, i.e. backward in time  
                            'onepass-zerophase'         zero-phase forward filter with delay compensation (default for firws, linear-phase symmetric FIR only)  
                            'onepass-reverse-zerophase' zero-phase reverse filter with delay compensation  
                            'onepass-minphase'          minimum-phase converted forward filter (non-linear, only for firws)  
                            'twopass'                   zero-phase forward and reverse filter (default, except for firws)  
                            'twopass-reverse'           zero-phase reverse and forward filter  
                            'twopass-average'           average of the twopass and the twopass-reverse  
          instabilityfix  optional method to deal with filter instabilities  
                            'no'       only detect and give error (default)  
                            'reduce'   reduce the filter order  
                            'split'    split the filter in two lower-order filters, apply sequentially  
          df              optional transition width (only for firws)  
          wintype         optional window type (only for firws), can be  
                            'hamming' (default)    maximum passband deviation 0.0022 [0.22%], stopband attenuation -53dB  
                            'hann'                 maximum passband deviation 0.0063 [0.63%], stopband attenuation -44dB  
                            'blackman'             maximum passband deviation 0.0002 [0.02%], stopband attenuation -74dB  
                            'kaiser'  
          dev             optional max passband deviation/stopband attenuation (only for firws with kaiser window, default = 0.001 [0.1%, -60 dB])  
          plotfiltresp    optional, 'yes' or 'no', plot filter responses (only for firws, default = 'no')  
          usefftfilt      optional, 'yes' or 'no', use fftfilt instead of filter (only for firws, default = 'no')  
         
        Note that a one- or two-pass filter has consequences for the strength of the  
        filter, i.e. a two-pass filter with the same filter order will attenuate the signal  
        twice as strong.  
         
        Further note that the filter type 'brickwall' filters in the frequency domain,  
        but may have severe issues. For instance, it has the implication that the time  
        domain signal is periodic. Another issue pertains to that frequencies are  
        not well defined over short time intervals; particularly for low frequencies.  
         
        If the data contains NaNs, these will affect the output. With an IIR  
        filter, and/or with FFT-filtering, local NaNs will spread to the whole  
        time series. With a FIR filter, local NaNs will spread locally, depending  
        on the filter order.  
         
        See also PREPROC  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_bandstopfilter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_bandstopfilter", *args, **kwargs)
