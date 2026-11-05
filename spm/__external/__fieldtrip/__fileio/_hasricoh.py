from spm._runtime import Runtime


def _hasricoh(*args, **kwargs):
    r"""
      HASRICOH tests whether the official toolbox for RICOH MEG systems by  
        Ricoh Company, Ltd. is installed or not.  
        Use as  
          string  = hasricoh;  
        which returns a string describing the toolbox version '1.0'.  
        An empty string is returned if the toolbox is not installed.  
        The string "unknown" is returned if it is installed but  
        the version is unknown.  
         
        Alternatively you can use it as  
          [boolean] = hasricoh(desired);  
        where desired is a string with the desired version.  
         
        See also READ_RICOH_HEADER, READ_RICOH_DATA, READ_RICOH_EVENT, RICOH2GRAD  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/hasricoh.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("hasricoh", *args, **kwargs)
