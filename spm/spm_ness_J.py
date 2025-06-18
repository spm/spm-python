from mpython import Runtime


def spm_ness_J(*args, **kwargs):
    """
      Return the Jacobian given a polynomial parameterisation
        FORMAT J = spm_ness_J(P,M,X)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_ness_J.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_ness_J", *args, **kwargs)
