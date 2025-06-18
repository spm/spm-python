from mpython import Runtime


def spm_gen_erp(*args, **kwargs):
    """
      Generate a prediction of trial-specific source activity
        FORMAT [y,pst] = spm_gen_erp(P,M,U)

        P - parameters
        M - neural-mass model structure
        U - trial-effects
          U.X  - between-trial effects (encodes the number of trials)
          U.dt - time bins for within-trial effects

        y   - {[ns,nx];...} - predictions for nx states {trials}
                            - for ns samples
        pst - peristimulus time (seconds)

       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_gen_erp.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_gen_erp", *args, **kwargs)
