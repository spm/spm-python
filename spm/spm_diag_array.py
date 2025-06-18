from mpython import Runtime


def spm_diag_array(*args, **kwargs):
    """
      Extract diagonal from 3-D arrays
        FORMAT D = spm_diag_array(X)

        X(:,i,i) -> D(:,i);
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_diag_array.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_diag_array", *args, **kwargs)
