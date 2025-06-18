from mpython import Runtime


def spm_lfp_mtf_sample(*args, **kwargs):
    """
      Spectral response of a NMM (transfer function x noise spectrum)
        FORMAT [G,w] = spm_lfp_mtf_sample(P,M,U)

        P - parameters
        M - neural mass model structure
        U - trial-specific effects

        G - {G(N,nc,nc}} - cross-spectral density for nc channels {trials}
                         - for N frequencies in M.Hz [default 1:64Hz]
        w - frequencies
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/NMDA_NMM_MFM/spm_lfp_mtf_sample.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_lfp_mtf_sample", *args, **kwargs)
