from mpython import Runtime


def spm_reorder_contrasts(*args, **kwargs):
    """
      Recompute contrasts allowing for permutation and deletion
        FORMAT batch = spm_reorder_contrasts(SPM,order)
        SPM   - SPM data structure
        order - array of contrast indices

        batch - batch job
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_reorder_contrasts.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_reorder_contrasts", *args, **kwargs)
