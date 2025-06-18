from mpython import Runtime


def spm_dcm_symm(*args, **kwargs):
    """
      Lock ECD orientations by introducing prior correlations
        FORMAT [pC] = spm_dcm_symm(pV,pE)
       __________________________________________________________________________

        pE   - prior expectation
        pV   - prior variance
        pC   - prior covariance
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_meeg/spm_dcm_symm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_symm", *args, **kwargs)
