from spm._runtime import Runtime


def _hcp_getopt(*args, **kwargs):
    r"""
      HCP_GETOPT parses the command line to the megconnectome executable  
        application, separating the options that start with -- from the file  
        names of the scripts to be executed.  
         
        Use as  
          megconnectome.exe --option1 arg1 --option2 arg2 scriptA.m scriptB.m  
        splits the command line arguments into a cell-array with key-value pairs  
        and a cell-array with the filenames.  
         
        In this example the hcp_getopt function returns  
          opts = {'option1', arg1, 'option2', arg2};  
          args = {'scriptA.m', 'scriptB.m'}  
         
        See also FT_GETOPT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/hcp_getopt.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("hcp_getopt", *args, **kwargs)
