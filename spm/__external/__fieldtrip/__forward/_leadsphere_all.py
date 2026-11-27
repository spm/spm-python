from spm._runtime import Runtime


def _leadsphere_all(*args, **kwargs):
    r"""
      usage: out=leadsphere_all(xloc,sensorloc,sensorori)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/leadsphere_all.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("leadsphere_all", *args, **kwargs)
