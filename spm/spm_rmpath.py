from spm._runtime import Runtime


def spm_rmpath(*args, **kwargs):
    r"""
      Recursively remove SPM paths from the MATLAB path  
          SPM_RMPATH checks if the file spm.m is found and removes the  
          path to that file and any subdirectories below it from the MATLAB  
          path.  
         
          P = SPM_RMPATH performs the same function as above and returns the  
          cleaned path string in P.  
         
          SPM_RMPATH(D) strips the path string D from the MATLAB path.  
         
          P = SPM_RMPATH(D) strips the path string D from the MATLAB path and  
          returns the cleaned path string in P.  
         
          See also PATH, ADDPATH, RMPATH, GENPATH, PATHTOOL, SAVEPATH.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_rmpath.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_rmpath", *args, **kwargs)
