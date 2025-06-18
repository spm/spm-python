from mpython import Runtime


def spm_MH_reml_likelihood(*args, **kwargs):
    """
      Likelihood function for spm_MH_reml
        FORMAT [L] = spm_MH_reml_likelihood(h,Y,M)

        h - hyperparameters
        Y - residual covariance

        L - likelihood p(Y,P)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_MH_reml_likelihood.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_MH_reml_likelihood", *args, **kwargs)
