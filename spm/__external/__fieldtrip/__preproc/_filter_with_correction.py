from spm.__wrapper__ import Runtime


def _filter_with_correction(*args, **kwargs):
    """
      FILTER_WITH_CORRECTION applies the filter to the data and corrects  
        edge-artifacts for one-pass filtering.  
         
        Use as  
          [filt] = filter_with_correction(B,A,dat,dir);  
        where  
          B,A        filter coefficients  
          dat        data matrix (Nchans X Ntime)  
          dir        optional filter direction, can be  
                       'onepass'                   forward filter only  
                       'onepass-reverse'           reverse filter only, i.e. backward in time  
                       'twopass'                   zero-phase forward and reverse filter (default)  
                       'twopass-reverse'           zero-phase reverse and forward filter  
                       'twopass-average'           average of the twopass and the twopass-reverse  
                       'onepass-zerophase'         zero-phase forward filter with delay compensation (default for firws, linear-phase symmetric FIR only)  
                       'onepass-reverse-zerophase' zero-phase reverse filter with delay compensation  
                       'onepass-minphase'          minimum-phase converted forward filter (non-linear!, firws only)  
         
        Note that a one- or two-pass filter has consequences for the  
        strength of the filter, i.e. a two-pass filter with the same filter  
        order will attenuate the signal twice as strong.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/private/filter_with_correction.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("filter_with_correction", *args, **kwargs)
