from spm._runtime import Runtime


def spm_update(*args, **kwargs):
    r"""
      Check (and install) SPM updates from the FIL server  
        FORMAT spm_update  
        This function will contact the FIL server, compare the version number of  
        the updates with the one of the SPM installation currently in the MATLAB  
        path and display the outcome.  
         
        FORMAT spm_update(update)  
        Invoking this function with any input parameter will do the same as  
        above but will also attempt to download and install the updates.  
        Note that it will close any open window and clear the workspace.  
         
        FORMAT [sts, msg] = spm_update(update)  
        sts  - status code:  
               NaN - SPM server not accessible  
               Inf - no updates available  
               0   - SPM installation up to date  
               n   - new revision <n> is available for download  
        msg  - string describing outcome, that would otherwise be displayed.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_update.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_update", *args, **kwargs)
