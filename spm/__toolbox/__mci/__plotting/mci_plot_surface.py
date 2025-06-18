from mpython import Runtime


def mci_plot_surface(*args, **kwargs):
    """
      Plot log probability surface
        FORMAT [log_prob,S,E] = mci_plot_surface (P,M,U,Y,S,dist)

        P         Parameters
        M         Model structure
        U         Inputs
        Y         Data
        S         Surface data structure
        dist      'prior', 'like' or 'post'
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/plotting/mci_plot_surface.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mci_plot_surface", *args, **kwargs)
