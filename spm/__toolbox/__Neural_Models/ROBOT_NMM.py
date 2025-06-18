from mpython import Runtime


def ROBOT_NMM(*args, **kwargs):
    """
      Tests routines in neural mass model (NMM) GUI
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Neural_Models/ROBOT_NMM.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ROBOT_NMM", *args, **kwargs)
