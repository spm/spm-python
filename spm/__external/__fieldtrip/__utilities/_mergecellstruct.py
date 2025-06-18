from mpython import Runtime


def _mergecellstruct(*args, **kwargs):
    """
      MERGECELLSTRUCT is a helper function for FT_TEST


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/mergecellstruct.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mergecellstruct", *args, **kwargs)
