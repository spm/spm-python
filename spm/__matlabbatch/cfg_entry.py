from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_entry(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          This is the entry configuration item class  
             
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
               * strtype  
               * num     - A 1-by-ndims vector of non-negative numbers, describing  
                           the expected dimensions of the input. Dimensions with a  
                           .num value of 0 or Inf can have an arbitrary number of  
                           elements. In case of 2 dimensions, .val inputs will be  
                           tried to match in un-transposed order first. If this  
                           does not work, then .val inputs will be transposed and  
                           matched again. If num is an empty matrix, no dimension  
                           and size checks will be performed.  
                           If strtype is 's' and num has 2 elements, these 2  
                           elements code the min/max length of a string. This is a  
                           workaround - in future versions num may be changed to a  
                           2-by-ndims array encoding min/max values for each  
                           dimension.  
                           If strtype is 's+' and num has 2 elements, these 2  
                           elements code the min/max number of lines in the cell  
                           array. The length of each line is not checked.  
               * def  
               * extras  - Extra information used for content checks of item.val{1}. The  
                           following strtypes can use this extra information:  
                           's' - a cell array of regular expressions. The val  
                           string must match at least one of the regular  
                           expressions.  
                           'e' - a function handle [sts val] = f(val, item.num)  
             
            Public Methods  
            ==============  
               * get_strings - returns name of object  
               * gettag      - returns tag  
               * help        - returns help text  
               * harvest     - returns item.val{1}, or '<UNDEFINED>' if empty, see below  
               * all_set     - returns ~isempty(item.val), checks numel(item.val{1})  
                               against item.num  
             
            Public internal Methods  
            =======================  
               * subsasgn  
               * subsref  
             
            'strtype'  
            The type of values that are entered by typing.  e.g. 'e' for evaluated.  
            The valid value types are:  
              's'   string  
              's+'  multi-line string, returned as cellstr  
              'e'   evaluated expression - this can be any expression, even a struct  
                     or cell  
              'f'   function or function handle  
              'n'   natural number (1..n)  
              'w'   whole number (0..n)  
              'i'   integer  
              'r'   real number  
              The following types are supported too, but there are no special  
              checks for validity of contents   
              'c'   indicator vector (e.g., 0101... or abab...)  
              'x'   contrast matrix  
              'p'   permutation  
             
            Subscript Assignment Checks  
            ===========================  
            .num must conform to the semantics described above.  
            The contents of item.val{1} will be checked to match .num and .strtype  
            restrictions.   
             
            Output in Job Structure (harvest)  
            =================================  
            cfg_entry uses cfg_item/harvest. If multiple dependencies are present  
            and all can be resolved, the result will be a concatenation of all  
            inputs. If concatenation fails, dependencies will not be resolved.  
             
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
            
              Documentation for cfg_entry  
                 doc cfg_entry  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/cfg_entry.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("cfg_entry", *args, **kwargs)
            
        super().__init__(_objdict)

    def _mysubs_fields(self, *args, **kwargs):
        """
          function [fnames, defaults] = mysubs_fields  
            Additional fields for class cfg_entry. See help of  
            @cfg_item/subs_fields for general help about this function.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/private/mysubs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mysubs_fields", *args, **kwargs)
