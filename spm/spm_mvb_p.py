from mpython import Runtime


def spm_mvb_p(*args, **kwargs):
    """
      Classical p-value for MVB using null distribution of log-odds ratio
        FORMAT [p] = spm_mvb_p(MVB,k)

        MVB - Multivariate Bayes structure
        k   - number of samples > 20

        p   - p-value: of (relative) F using an empirical null distribution

        spm_mvb_p evaluates an empirical null distribution for the (fee-energy)
        difference in log-evidences (the log odds ratio) by phase-shuffling the
        target vector and repeating the greedy search. It adds the p-value as a
        field (p_value) to MVB.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_mvb_p.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mvb_p", *args, **kwargs)
