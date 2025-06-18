from mpython import Runtime


def spm_vb_w(*args, **kwargs):
    """
      Variational Bayes for GLM-AR modelling in a block - update w
        FORMAT [block] = spm_vb_w (Y,block)

        Y          - [T x N] time series
        block      - data structure (see spm_vb_glmar)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_w.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_vb_w", *args, **kwargs)
