from spm.__wrapper__ import Runtime


def _clusterstat(*args, **kwargs):
    """
      CLUSTERSTAT computers cluster statistic for multidimensional channel-freq-time or  
        volumetric source data  
         
        See also TFCESTAT, FINDCLUSTER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/clusterstat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("clusterstat", *args, **kwargs)
