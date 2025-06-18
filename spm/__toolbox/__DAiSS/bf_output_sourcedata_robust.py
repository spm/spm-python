from mpython import Runtime


def bf_output_sourcedata_robust(*args, **kwargs):
    """
      Extract source data, handling bad data segments
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_output_sourcedata_robust.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_output_sourcedata_robust", *args, **kwargs)
