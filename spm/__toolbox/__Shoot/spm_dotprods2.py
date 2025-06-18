from mpython import Runtime


def spm_dotprods2(*args, **kwargs):
    """
      Generate a kernel from dot-products of images
        FORMAT spm_dotprods(job)
        job.images  - Images to use
        job.dotprod - Part of filename for results
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_dotprods2.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dotprods2", *args, **kwargs)
