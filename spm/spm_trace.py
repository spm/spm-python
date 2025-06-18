from mpython import Runtime


def spm_trace(*args, **kwargs):
    """
      Fast trace for large matrices: C = spm_trace(A,B) = trace(A*B)
        FORMAT [C] = spm_trace(A,B)

        C = spm_trace(A,B) = trace(A*B) = sum(sum(A'.*B));
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_trace.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_trace", *args, **kwargs)
