from spm._runtime import Runtime


def cfg_getfile_cpath(*args, **kwargs):
    r"""
      Canonicalise paths  
        FORMAT cpaths = cfg_getfile_cpath(inpaths, basedir)  
        inpaths       - cell array of (relative or absolute) paths  
        basedir       - single cell containing the base path of relative input paths  
        cpaths        - cell array of canonical paths, one for each element of  
                        inpaths  
        This function canonicalises paths by  
        - removing /./ and /../ constructs  
        - prepending basedir to relative pathnames  
       ____________________________________________________________________________  
        Copyright (C) 2005 Wellcome Department of Imaging Neuroscience  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_getfile_cpath.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_getfile_cpath", *args, **kwargs)
