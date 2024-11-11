from spm.__wrapper__ import Runtime


def mne_license(*args, **kwargs):
    """
      MNE_LICENSE prints the license only once upon the first call to  
        this function. If the user does a "clear all", the license will  
        again be shown.  This function should be included in every openmeeg  
        function to ensure that the license is displayed at least once.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/mne_license.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mne_license", *args, **kwargs, nargout=0)
