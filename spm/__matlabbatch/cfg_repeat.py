from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_repeat(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          This is the repeat configuration item class  
             
            Data structure  
            ==============  
            Description fields  
               * name  - display name of config item  
               * tag   - tag of the menu item  
               * val   - cell array of cfg_items (not set initially)  
               * check - (optional) function handle to implement configuration  
                         specific subsasgn checks based on the harvested subtree  
                         rooted at this node  
               * help  - help text  
            GUI/job manager fields  
               * expanded  
               * hidden  
            All fields are inherited from the generic configuration item class.  
            Added fields  
               * values  
               * num  - defaults to [0 Inf]  
               * forcestruct - force creation of cellstruct fields in job tree, even  
                 if values has only one item  
             
            Public Methods  
            ==============  
               * get_strings - returns name of object  
               * gettag      - returns tag  
               * help        - returns help text  
               * harvest     - see below  
               * all_set     - true, if .num check passes and all items in .val are  
                               all_set   
             
            Output in Job Structure (harvest)  
            =================================  
            If the number of elements in the 'values' field is greater than one,  
            then the resulting data structure is a cell array.  Each element of the  
            cell array is a struct with a single field, where the name of the field  
            is given by the 'tag' of the child node.  
            If the 'values' field only contains one element, which is a 'branch',  
            then the data structure is a struct array (in which case the 'tag' of  
            the current node can be ignored).  
            If the 'values' field only contains one element, which is not a branch,  
            then the data structure is a cell array, where each element is the  
            value of the child node ((in which case the 'tag' of the current node  
            can be ignored).  
             
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
            
              Documentation for cfg_repeat  
                 doc cfg_repeat  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_repeat/cfg_repeat.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("cfg_repeat", *args, **kwargs)
            
        super().__init__(_objdict)

    def _mysubs_fields(self, *args, **kwargs):
        """
          function [fnames, defaults] = mysubs_fields  
            Additional fields for class cfg_repeat. See help of  
            @cfg_item/subs_fields for general help about this function.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_repeat/private/mysubs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mysubs_fields", *args, **kwargs)
