from mpython import Runtime


def spm_dcm_lock(*args, **kwargs):
    """
      Lock experimental effects by introducing prior correlations
        FORMAT [pC] = spm_dcm_lock(pV)
       __________________________________________________________________________

        pV   - prior variance
        pC   - prior covariance
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_lock.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_lock", *args, **kwargs)
