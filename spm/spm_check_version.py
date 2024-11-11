from spm.__wrapper__ import Runtime


def spm_check_version(*args, **kwargs):
    """
      Check a version number against a Toolbox version  
         
        FORMAT tbx = spm_check_version  
        tbx    - toolbox name {'matlab','octave',...}  
         
        FORMAT v = spm_check_version(tbx)  
        tbx    - toolbox name {'matlab','octave','spm','signal',...}  
         
        v      - version number {string}  
         
        FORMAT status = spm_check_version(tbx,chk)  
        tbx    - toolbox name {'matlab','octave','signal',...}  
        chk    - version number to be checked {string}  
         
        status - outcome of the comparison:  
                 -1: Toolbox version is earlier than the user supplied version  
                  0: Toolbox and user versions are the same  
                  1: Toolbox version is later than the user supplied version  
                     Think of it this way, the sign of status is determined by  
                     MATLAB_TOOLBOX_VERSION - USER_VERSION (i.e., THE VERSION YOU  
                     INPUT).  
         
        FORMAT status = spm_check_version('matlab','online')  
        status - 1 if running in MATLAB Online (checks for '/MATLAB Drive' drive)  
       __________________________________________________________________________  
         
        This function checks if a user supplied version number is less than,  
        equal to or greater than the version number of specified toolbox. If no  
        toolbox is specified the function checks the version of MATLAB. User  
        defined toolboxes can be checked but the Contents.m file must conform  
        to the specification defined in ver.m  
         
        This function assumes that the version number is really a text string  
        with fields major.minor.revision.build. Other formats are not supported.  
        Checking is done to the level specified by the input version. Thus an  
        input of '7' will be rated as the same version as 7.1, but 7.0 would be  
        rated as earlier than 7.1.  
       __________________________________________________________________________  
         
        EXAMPLES:  
         
        If the MATLAB version is 7.1.0.83, and the user supplied version is '7':  
        status = spm_check_version('matlab','7');  
        returns status == 0   : major revision numbers are the same.  
         
        If the MATLAB version is 7.1.0.0, and the user supplied version is '7.1':  
        status = spm_check_version('matlab','7');  
        returns status == 0   : major and minor revision numbers are the same.  
         
        If the MATLAB version is 7.1.0.83, and the user supplied version is '7.2':  
        status = spm_check_version('matlab','7.2');  
        returns status == -1   : major + minor revision is earlier for MATLAB.  
         
        If the MATLAB version is 6.5.1, and the user supplied version is '6.5.0'.  
        status = spm_check_version('matlab','6.5.0');  
        returns status == 1     : major + minor + release revision is later  
                                  for MATLAB  
        The statement ( spm_check_version('matlab','6.5.0') > 0 ) is true for  
        all MATLAB Toolbox versions after 6.5.0.  
       __________________________________________________________________________  
         
        See also VERSION, VER, VERLESSTHAN, ISMATLABRELEASEOLDERTHAN  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_check_version.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_check_version", *args, **kwargs)
