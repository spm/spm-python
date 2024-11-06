from spm.__wrapper__ import Runtime


def spm_tbx_config2cfg(*args, **kwargs):
    """
      Convert SPM5 toolbox configuration to Matlabbatch  
        FORMAT spm_tbx_config2cfg(c)  
        Input:  
        c      - SPM5 toolbox configuration structure  
        Output: (written to disk in the current working directory)  
        tbx_cfg_<toolboxtag>.m - Code to generate a Matlabbatch configuration  
                                 tree similar to the SPM5 configuration struct  
        tbx_def_<toolboxtag>.m - Code to set toolbox defaults.  
         
        Both files should be placed in the root directory of the toolbox  
        instead of the old config file. They will be picked up during spm  
        initialisation by spm_cfg.m.  
        The full subscript reference path will become   
        spm.tools.<toolboxtag> in the configuration tree.  
         
        CAVE: No code is generated for subfunctions that are present in the old  
        config file. This code has to be transferred manually. A transition  
        from .vfiles to .vout callbacks is strongly encouraged. This requires  
        - computation functions to return a single results variable (any kind  
          of MATLAB variable allowed, but struct or cell preferred to combine  
          multiple results)  
        - a .vout callback to describe subscript references into this output  
          variable for each individual output.  
         
        Note that it is no longer possible to open a non-cfg_exbranch node in the  
        GUI. In SPM5, a call like  
        spm_jobman('interactive','','tools.vgtbx_Volumes')  
        would have opened the top level choice for the Volumes toolbox. In SPM8,  
        this call will generate a warning and open the GUI with an empty job.  
        Users then have to select the tools from the "SPM->Tools" menu.  
        If one wants to open a dummy job consisting of more than one module in  
        a toolbox, one could use code like this  
         
        % Generate dummy job with default settings for estimate/write  
        % The struct([]) is necessary to avoid a warning during initialisation   
        j{1}.spm.spatial.realign.estimate = struct([]);  
        j{2}.spm.spatial.realign.write = struct([]);  
        % Load this job into spm_jobman  
        spm_jobman('interactive',j)  
       _______________________________________________________________________  
        Copyright (C) 2008 Wellcome Trust Centre for Neuroimaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/compat/spm_tbx_config2cfg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_tbx_config2cfg", *args, **kwargs)
