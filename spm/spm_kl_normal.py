from mpython import Runtime


def spm_kl_normal(*args, **kwargs):
    """
      KL divergence between two multivariate normal densities
        FORMAT [d] = spm_kl_normal(m_q,c_q,m_p,c_p)

        KL (Q||P) = <log Q/P> where avg is wrt Q

        between two Normal densities Q and P

        m_q, c_q    Mean and covariance of first Normal density
        m_p, c_p    Mean and covariance of second Normal density
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_kl_normal.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_kl_normal", *args, **kwargs)
