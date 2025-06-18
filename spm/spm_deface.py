from mpython import Runtime


def spm_deface(*args, **kwargs):
    """
      Face strip images
        FORMAT names = spm_deface(job)
        job.images   - cell array of NIfTI file names

        names        - cell array of de-faced images

        This is a little routine for attempting to strip the face from images,
        so individuals are more difficult to identify from surface renderings.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_deface.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_deface", *args, **kwargs)
