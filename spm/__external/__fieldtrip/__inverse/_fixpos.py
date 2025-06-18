from mpython import Runtime


def _fixpos(*args, **kwargs):
    """
      FIXPOS helper function to ensure that meshes are described properly


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/fixpos.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixpos", *args, **kwargs)
