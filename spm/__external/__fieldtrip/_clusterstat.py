from spm._runtime import Runtime


def _clusterstat(*args, **kwargs):
    r"""
      CLUSTERSTAT computers cluster statistic for multidimensional channel-freq-time or  
        volumetric source data  
         
        See also TFCESTAT, FINDCLUSTER  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/clusterstat.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("clusterstat", *args, **kwargs)
