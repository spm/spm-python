from spm.__wrapper__ import Runtime


def _tfcestat(*args, **kwargs):
    """
      TFCESTAT computes threshold-free cluster statistic multidimensional channel-freq-time or  
        volumetric source data  
         
        See also CLUSTERSTAT, FINDCLUSTER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/tfcestat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tfcestat", *args, **kwargs)
