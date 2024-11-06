from spm.__wrapper__ import Runtime


def _peakdetect2(*args, **kwargs):
    """
      PEAKDETECT2 detects peaks above a certain threshold in single-channel data  
         
        Use as  
          [pindx, pval] = peakdetect(signal, min, mindist)  
         
        mindist is optional, default is 1  
         
        See also PEAKDETECT, PEAKDETECT3  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/peakdetect2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("peakdetect2", *args, **kwargs)
