from spm._runtime import Runtime


def _compile_mex_list(*args, **kwargs):
    """
      function compile_mex_list(L, baseDir)  
         
        Compile a list of MEX files as determined by the input argument L.  
        The second argument 'baseDir' is the common base directory for the  
        files listed in L. The third argument is a flag that determines  
        whether to force (re-)compilation even if the MEX file is up-to-date.  
         
        See also ft_compile_mex, add_mex_source.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/compile_mex_list.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("compile_mex_list", *args, **kwargs, nargout=0)
