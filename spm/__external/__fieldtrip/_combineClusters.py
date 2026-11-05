from spm._runtime import Runtime


def _combineClusters(*args, **kwargs):
    r"""
      COMBINECLUSTERS is a helper function for FINDCLUSTER. It searches for  
        adjacent clusters in neighbouring channels and combines them.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/combineClusters.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("combineClusters", *args, **kwargs)
