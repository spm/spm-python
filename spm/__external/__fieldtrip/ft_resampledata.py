from spm.__wrapper__ import Runtime


def ft_resampledata(*args, **kwargs):
    """
      FT_RESAMPLEDATA performs a resampling or downsampling of the data to a specified  
        new sampling frequency, or an inperpolation of the data measured with one sampling  
        frequency to another. The latter is useful when merging data measured on two  
        different acquisition devices, or when the samples in two recordings are slightly  
        shifted.  
         
        Use as  
          [data] = ft_resampledata(cfg, data)  
         
        The data should be organised in a structure as obtained from the FT_PREPROCESSING  
        function. The configuration should contain  
          cfg.resamplefs      = frequency at which the data will be resampled  
          cfg.method          = resampling method, see RESAMPLE, DOWNSAMPLE, DECIMATE (default = 'resample')  
          cfg.detrend         = 'no' or 'yes', detrend the data prior to resampling (no default specified, see below)  
          cfg.demean          = 'no' or 'yes', whether to apply baseline correction (default = 'no')  
          cfg.baselinewindow  = [begin end] in seconds, the default is the complete trial (default = 'all')  
          cfg.feedback        = 'no', 'text', 'textbar', 'gui' (default = 'text')  
          cfg.trials          = 'all' or a selection given as a 1xN vector (default = 'all')  
          cfg.sampleindex     = 'no' or 'yes', add a channel with the original sample indices (default = 'no')  
         
        Rather than resapling to a specific sampling frequency, you can also specify a time  
        axis on which you want the data to be resampled. This is useful for merging data  
        from two acquisition devices, after resampledata you can call FT_APPENDDATA to  
        concatenate the channels from the different acquisition devices.  
          cfg.time        = cell-array with one time axis per trial (i.e., from another dataset)  
          cfg.method      = interpolation method, see INTERP1 (default = 'pchip')  
          cfg.extrapval   = extrapolation behaviour, scalar value or 'extrap' (default is as in INTERP1)  
         
        The default method is 'resample' when you specify cfg.resamplefs, and 'pchip' when  
        you specify cfg.time.  
         
        The methods 'resample' and 'decimate' automatically apply an anti-aliasing low-pass  
        filter. You can also explicitly specify an anti-aliasing low pass filter. This is  
        particularly adviced when downsampling using the 'downsample' method, but also when  
        strong noise components are present just above the new Nyquist frequency.  
          cfg.lpfilter    = 'yes' or 'no' (default = 'no')  
          cfg.lpfreq      = scalar value for low pass frequency (there is no default, so needs to be always specified)  
          cfg.lpfilttype  = string, filter type (default is set in ft_preproc_lowpassfilter)  
          cfg.lpfiltord   = scalar, filter order (default is set in ft_preproc_lowpassfilter)  
         
        More documentation about anti-alias filtering can be found in this <a href="matlab:  
        web('https://www.fieldtriptoolbox.org/faq/resampling_lowpassfilter')">FAQ</a> on the FieldTrip website.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        See also FT_PREPROCESSING, FT_APPENDDATA, FT_PREPROC_LOWPASSFILTER, RESAMPLE, DOWNSAMPLE, DECIMATE, INTERP1  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_resampledata.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_resampledata", *args, **kwargs)
