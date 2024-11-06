from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_exbranch(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          This is the exbranch configuration item class  
             
            Data structure  
            ==============  
            Description fields  
               * name  - display name of config item  
               * tag   - tag of the menu item  
               * val   - 1xn cell array of cfg_items  
               * check - (optional) function handle to implement configuration  
                         specific subsasgn checks based on the harvested subtree  
                         rooted at this node  
               * help  - help text  
            GUI/job manager fields  
               * expanded  
               * hidden  
            All fields above are inherited from the branch configuration item class.  
               * prog  
               * vfiles  
               * modality  
               * vout  - function handle that generates sout struct  
               * sout  - source dependency description  
               * jout  - saved output (will be referenced by harvest of a dependency  
                         target for dependency resolution at job runtime)  
               * tdeps - list where this branch is target of a dependency  
               * sdeps - list where this branch is source of a dependency  
               * chk   - field to save check status from cfg_item.check callbacks  
               * id    - id of this cfg_exbranch. This is used to reference the  
                         cfg_exbranch in cfg_dep objects.  
             
            Public Methods  
            ==============  
               * get_strings - returns name of object  
               * gettag      - returns tag  
               * help        - returns help text  
               * harvest  
               * all_set  
             
            * 'executable branch'  - See branch for details on inherited fields  
             
            The layout of the configuration tree and the types of configuration items  
            have been kept compatible to a configuration system and job manager  
            implementation in SPM5 (Statistical Parametric Mapping, Copyright (C)  
            2005 Wellcome Department of Imaging Neuroscience). This code has been  
            completely rewritten based on an object oriented model of the  
            configuration tree.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
            
              Documentation for cfg_exbranch  
                 doc cfg_exbranch  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_exbranch/cfg_exbranch.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("cfg_exbranch", *args, **kwargs)
            
        super().__init__(_objdict)

    def _mysubs_fields(self, *args, **kwargs):
        """
          function [fnames, defaults] = mysubs_fields  
            Additional fields for class cfg_exbranch. See help of  
            @cfg_item/subs_fields for general help about this function.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_exbranch/private/mysubs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mysubs_fields", *args, **kwargs)
