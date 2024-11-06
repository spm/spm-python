from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_branch(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          This is the branch configuration item class for non-executable  
            branches. It implements branch harvest, all_set, get_strings.  
             
            Data structure  
            ==============  
            Description fields  
               * name  - display name of config item  
               * tag   - tag of the menu item  
               * val   - 1xn cell array of cfg_item objects  
               * check - (optional) function handle to implement configuration  
                         specific subsasgn checks based on the harvested subtree  
                         rooted at this node  
               * help  - help text  
            GUI/job manager fields  
               * expanded  
               * hidden  
            All fields are inherited from the generic configuration item class.  
             
            Public Methods  
            ==============  
               * get_strings - returns name of object  
               * gettag      - returns tag  
               * help        - returns help text  
               * harvest     - returns struct, field names correspond to tags of  
                               items in .val field  
               * all_set     - returns all(all_set(item.val{...}))  
             
            Output in Job Structure (harvest)  
            =================================  
            The resulting structure is a struct. Its fieldnames correspond to the  
            tags of the cfg_items in item.val, the value of each field is the  
            harvested data of the corresponding child item.  
             
            The layout of the configuration tree and the types of configuration items  
            have been kept compatible to a configuration system and job manager  
            implementation in SPM5 (Statistical Parametric Mapping, Copyright (C)  
            2005 Wellcome Department of Imaging Neuroscience). This code has been  
            completely rewritten based on an object oriented model of the  
            configuration tree.  
             
              The resulting data structure is a struct, with fieldnames according  
              to the 'tag's of the child nodes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
            
              Documentation for cfg_branch  
                 doc cfg_branch  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_branch/cfg_branch.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("cfg_branch", *args, **kwargs)
            
        super().__init__(_objdict)

    def _mysubs_fields(self, *args, **kwargs):
        """
          function [fnames, defaults] = mysubs_fields  
            Additional fields for class cfg_branch. See help of  
            @cfg_item/subs_fields for general help about this function.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_branch/private/mysubs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mysubs_fields", *args, **kwargs)
