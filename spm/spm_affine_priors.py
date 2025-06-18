from mpython import Runtime


def spm_affine_priors(*args, **kwargs):
    """
      Distribution of the priors used in affine registration

        The parameters for this distribution were derived empirically from 227
        scans, that were matched to the ICBM space.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_affine_priors.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_affine_priors", *args, **kwargs)
