from spm._runtime import Runtime


def ROBOT_DCM_fMRI(*args, **kwargs):
    r"""
      test routine to check current implementations of DCM for fMRI  
       ==========================================================================  
         
        Options  
       --------------------------------------------------------------------------  
        DCM.options.two_state              % two regional populations (E and I)  
        DCM.options.stochastic             % fluctuations on hidden states  
        DCM.options.nonlinear              % interactions among hidden states  
        DCM.options.nograph                % graphical display  
        DCM.options.centre                 % mean-centre inputs  
        DCM.options.P                      % starting estimates for parameters  
        DCM.options.hidden                 % indices of hidden regions  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/tests/ROBOT_DCM_fMRI.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ROBOT_DCM_fMRI", *args, **kwargs)
