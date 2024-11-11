from spm.__wrapper__ import Runtime


def spm_matlab_version_chk(*args, **kwargs):
    """
      Check a version number against a Toolbox version  
        FORMAT [status, fieldsUsed] = spm_matlab_version_chk(chk,tbx)  
        chk        - Version number to be checked {string}  
        tbx        - Name of toolbox to check [Default: 'MATLAB']  
         
        status     - Defines the outcome of the comparison  
                     -1: Toolbox version is earlier than the user supplied version  
                      0: Toolbox and user versions are the same  
                      1: Toolbox version is later than the user supplied version  
                         Think of it this way, the sign of status is determined  
                         by MATLAB_TOOLBOX_VERSION - USER_VERSION (i.e., THE   
                         VERSION YOU INPUT).  
        fieldsUsed - deprecated [Returns {}]  
       __________________________________________________________________________  
         
        This function is deprecated, use SPM_CHECK_VERSION instead.  
       __________________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_matlab_version_chk.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_matlab_version_chk", *args, **kwargs)
