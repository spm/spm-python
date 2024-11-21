from spm.__wrapper__ import Runtime


def bf_inverse_deflect(*args, **kwargs):
    """
      Used DeFleCT framework to compute spatial filters  
         
        Please cite:  
        Hauk O, Stenroos M.  
        A framework for the design of flexible cross-talk functions for spatial  
        filtering of EEG/MEG data: DeFleCT.  
        Human Brain Mapping 2013  
        http://imaging.mrc-cbu.cam.ac.uk/meg/AnalyzingData/DeFleCT_SpatialFiltering_Tools  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_inverse_deflect.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("bf_inverse_deflect", *args, **kwargs)
