from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_menu(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          This is the menu configuration item class  
             
            Data structure  
            ==============  
            Description fields  
               * name  - display name of config item  
               * tag   - tag of the menu item  
               * val   - 1x1 cell array  
               * check - (optional) function handle to implement configuration  
                         specific subsasgn checks based on the harvested subtree  
                         rooted at this node  
               * help  - help text  
            GUI/job manager fields  
               * expanded  
               * hidden  
            All fields above are inherited from the generic configuration item class.  
               * labels - cell array of label strings  
               * values - cell array of values  
               * def  
             
            Public Methods  
            ==============  
               * get_strings - returns name of object  
               * gettag      - returns tag  
               * help        - returns help text  
               * harvest     - returns item.val{1}, or '<UNDEFINED>' if empty, see below  
               * all_set     - returns ~isempty(item.val)  
             
            Output in Job Structure (harvest)  
            =================================  
            cfg_menu uses cfg_item/harvest.  
             
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
            
              Documentation for cfg_menu  
                 doc cfg_menu  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/cfg_menu.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("cfg_menu", *args, **kwargs)
            
        super().__init__(_objdict)

    def _mysubs_fields(self, *args, **kwargs):
        """
          function [fnames, defaults] = mysubs_fields  
            Additional fields for class cfg_menu. See help of  
            @cfg_item/subs_fields for general help about this function.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/private/mysubs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mysubs_fields", *args, **kwargs)
