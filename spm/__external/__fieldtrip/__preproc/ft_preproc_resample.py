from spm.__wrapper__ import Runtime


def ft_preproc_resample(*args, **kwargs):
    """
      FT_PREPROC_RESAMPLE resamples all channels in the data matrix  
         
        Use as  
          dat = ft_preproc_resample(dat, Fold, Fnew, method)  
        where  
          dat    = matrix with the input data (Nchans X Nsamples)  
          Fold   = scalar, original sampling frequency in Hz  
          Fnew   = scalar, desired sampling frequency in Hz  
          method = string, can be 'resample', 'decimate', 'downsample', 'fft'  
         
        The resample method applies an anti-aliasing (lowpass) FIR filter to  
        the data during the resampling process, and compensates for the filter's  
        delay. For the other two methods you should apply an anti-aliassing  
        filter prior to calling this function.  
         
        If the data contains NaNs, these are ignored for the computation, but  
        retained in the output.  
         
        See also PREPROC, FT_PREPROC_LOWPASSFILTER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_resample.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_resample", *args, **kwargs)
