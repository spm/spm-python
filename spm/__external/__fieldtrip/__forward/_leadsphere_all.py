from spm.__wrapper__ import Runtime


def _leadsphere_all(*args, **kwargs):
    """
      usage: out=leadsphere_all(xloc,sensorloc,sensorori)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/leadsphere_all.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("leadsphere_all", *args, **kwargs)
