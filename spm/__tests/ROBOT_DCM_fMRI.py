from spm.__wrapper__ import Runtime


def ROBOT_DCM_fMRI(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/ROBOT_DCM_fMRI.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ROBOT_DCM_fMRI", *args, **kwargs)
