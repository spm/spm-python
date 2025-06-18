from mpython import Runtime


def end2end_attention(*args, **kwargs):
    """
      End-to-end test for attention dataset
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/end2end_attention.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("end2end_attention", *args, **kwargs)
