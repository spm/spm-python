from mpython import Runtime


def _ama2headmodel(*args, **kwargs):
    """
      AMA2HEADMODEL converts a dipoli structure with boundary geometries
        and a boundary element method transfer matrix to a volume conduction
        model.

        Use as
          headmodel = ama2headmodel(ama)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/ama2headmodel.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ama2headmodel", *args, **kwargs)
