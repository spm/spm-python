from mpython import Runtime


def spm_pinv(*args, **kwargs):
    """
      Pseudo-inverse for sparse matrices
        FORMAT X = spm_pinv(A,TOL)

        A   - matrix
        TOL - Tolerance to force singular value decomposition
        X   - generalised inverse
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_pinv.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_pinv", *args, **kwargs)
