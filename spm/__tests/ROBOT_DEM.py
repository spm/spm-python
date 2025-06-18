from mpython import Runtime


def ROBOT_DEM(*args, **kwargs):
    """
      Tests routines in DEM GUI
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/ROBOT_DEM.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ROBOT_DEM", *args, **kwargs)
