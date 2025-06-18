from mpython import Runtime


def expmall(*args, **kwargs):
    """
    expmall is a function.
          dx = expmall(J, f, t, EP)


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/expmall.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("expmall", *args, **kwargs)
