from mpython import Runtime


def _leadsphere_all(*args, **kwargs):
    """
      usage: out=leadsphere_all(xloc,sensorloc,sensorori)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/leadsphere_all.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("leadsphere_all", *args, **kwargs)
