from spm._runtime import Runtime


def spm_julia(*args, **kwargs):
    r"""
      Run Julia code from SPM  
        FORMAT s = spm_julia('settings')  
            s - a structure containing various settings  
         
        FORMAT sts = spm_julia('install')  
        Install Julia within SPM. If it exists already, then do nothing.  
         
        FORMAT sts = spm_julia('install','force')  
        Install Julia within SPM - irrespective of whether it seems to be  
        there or not.  
         
        FORMAT sts = spm_julia('add-package', package1, package2, ...)  
        Add Julia packages, where package1, package2, etc are names of registered  
        packages.  Unregistered packages can be installed by giving their url  
        within a structure. Note that fields 'rev' and 'version' can also be  
        included in the structure, where 'version' could be e.g. 'v0.2.1'  
        (v"0.2.1" in Julia) or '0.2' ("0.2" in Julia).  For example:  
            pkg_spec = struct('url','https://github.com/spm/PushPull.jl');  
            sts      = spm_julia('add-package', pkg_spec)  
         
        FORMAT [sts,result] = spm_julia('run', cmd)  
        Execute a command with julia -e  
         
        FORMAT [sts,result] = spm_julia('run', cmd, package1, package2, ...)  
        Checks for presence of packages, and installs them if necessary.  
        Prepends use of packages before cmd.  
         
        For more information about the Julia language, see https://julialang.org/  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/spm_julia.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_julia", *args, **kwargs)
