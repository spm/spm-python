from mpython import Runtime


def ADEM_SHC_demo(*args, **kwargs):
    """
      This demo illustrates the use of Lotka-Volterra form SHCs (Stable
        heteroclinic channel) to prescribe active sampling (inference). In this
        example each (unstable) fixed point in the SHC attracts the agent to
        points on the circumference of a circle.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DEM/ADEM_SHC_demo.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ADEM_SHC_demo", *args, **kwargs, nargout=0)
