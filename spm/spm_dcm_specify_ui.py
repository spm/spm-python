from spm.__wrapper__ import Runtime


def spm_dcm_specify_ui(*args, **kwargs):
    """
      Interface for stepping the user through creating a DCM  
        FORMAT DCM = spm_dcm_specify_ui(SPM,xY)  
         
        SPM      - SPM structure from SPM.mat  
        xY       - (optional) VOI structures to be inserted into the DCM  
                   accepts a cell array of VOI structures (see spm_regions.m)  
                   or a nested cell array for multiple sessions (DCM for CSD)  
        settings - (optional) Structure of pre-populated settings for testing the  
                   GUI without mouse clicks.  
         
                    .delays      vector of delays [1 x n]  
                    .TE          echo time  
                    .nonlinear   non-linear DCM  
                    .two_state   two-state DCM  
                    .stochastic  stochastic DCM  
                    .centre      mean-centring of inputs  
                    .induced     induced responses)  
                    .a .b .c .d  connectivity matrices  
         
                    .cond(k).name    desired name for the k-th condition (input)  
                    .cond(k).spmname corresponding condition name in SPM.Sess.U,  
                                     or cell array of names to binarize and merge  
         
                 	  .u(i,j)          whether to include condition i regressor j  
                                     (as an alternative to .cond)  
         
        DCM      - DCM structure (see spm_dcm_ui)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_specify_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_specify_ui", *args, **kwargs)
