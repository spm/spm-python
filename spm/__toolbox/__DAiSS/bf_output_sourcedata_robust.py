from spm._runtime import Runtime


def bf_output_sourcedata_robust(*args, **kwargs):
    r"""
      Extract source data, handling bad data segments  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_output_sourcedata_robust.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_output_sourcedata_robust", *args, **kwargs)
