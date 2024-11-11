from spm.__wrapper__ import Runtime


def _add_mex_source(*args, **kwargs):
    """
      function L = add_mex_source(L, directory, relName, matchPlatform, excludePlatform, extras)  
         
        Input + output argument L is a structure array of directory names, source file names,  
        and extra arguments required for the compilation of MEX files. This function will  
        create a new element of this structure and append it to L.  
         
        Further inputs:  
          directory  
             target directory of the mex-file  
          relName  
             source file relative to 'directory'  
          matchPlatform  
             list of platforms this MEX file should only be compiled for.  
             use an empty matrix [] to compile for all platforms  
          excludePlatform  
             list of platforms this MEX file should NOT be compiled for.  
          extras  
             extra arguments to the MEX command, e.g. additional source files  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/add_mex_source.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("add_mex_source", *args, **kwargs)
