from spm._runtime import Runtime


def cfg_getfile_pathparts(*args, **kwargs):
    r"""
      Split paths in cellstr inpaths into cellstr lists of directories  
        FORMAT pathparts = cfg_getfile_pathparts(inpaths)  
        inpaths          - cellstr list of pathnames  
        pathparts        - cell array of cellstr list, containing the directory  
                           names of each inpath path  
        returns cell array of path component cellstr arrays  
        For PC (WIN) targets, both '\' and '/' are accepted as filesep, similar  
        to MATLAB fileparts  
       ____________________________________________________________________________  
        Copyright (C) 2005 Wellcome Department of Imaging Neuroscience  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_getfile_pathparts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_getfile_pathparts", *args, **kwargs)
