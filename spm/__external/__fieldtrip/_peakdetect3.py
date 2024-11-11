from spm.__wrapper__ import Runtime


def _peakdetect3(*args, **kwargs):
    """
      PEAKDETECT3 detects peaks above a certain threshold in single-channel data  
         
        Use as  
          [pindx, pval] = peakdetect3(dat, threshold, mindist)  
         
        See also PEAKDETECT, PEAKDETECT2  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/peakdetect3.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("peakdetect3", *args, **kwargs)
