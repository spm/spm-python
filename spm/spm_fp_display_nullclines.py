from mpython import Runtime


def spm_fp_display_nullclines(*args, **kwargs):
    """
      Nullcline plot of flow and sample trajectory
        FORMAT spm_fp_display_nullclines(M,x)

        M   - model specifying flow; M(1).f;
        x   - cell array of domain or support

        f   - derivative of x(2)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_fp_display_nullclines.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fp_display_nullclines", *args, **kwargs)
