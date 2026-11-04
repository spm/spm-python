from spm._runtime import Runtime


def ROBOT_NMM(*args, **kwargs):
    r"""
      Tests routines in neural mass model (NMM) GUI  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Neural_Models/ROBOT_NMM.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ROBOT_NMM", *args, **kwargs)
