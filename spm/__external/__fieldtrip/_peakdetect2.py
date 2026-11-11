from spm._runtime import Runtime


def _peakdetect2(*args, **kwargs):
    r"""
      PEAKDETECT2 detects peaks above a certain threshold in single-channel data  
         
        Use as  
          [pindx, pval] = peakdetect(signal, min, mindist)  
         
        mindist is optional, default is 1  
         
        See also PEAKDETECT, PEAKDETECT3  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/peakdetect2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("peakdetect2", *args, **kwargs)
