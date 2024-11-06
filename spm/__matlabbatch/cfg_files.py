from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_files(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          This is the file configuration item class  
             
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
               * filter  - cellstr of filter expressions, default {'any'}  
               * num     - default [0 Inf]  
               * dir     - default ''  
               * ufilter - default '.*'  
               * def  
             
            Public Methods  
            ==============  
               * get_strings - returns name of object  
               * gettag      - returns tag  
               * help        - returns help text  
               * harvest     - returns item.val{1}, or '<UNDEFINED>' if empty, see below  
               * all_set     - returns ~isempty(item.val), checks numel(item.val{1})  
                               against item.num  
             
            Subscript Assignment Checks  
            ===========================  
            Values assigned to the .num field must be a 2-vector.  
            Values assigned to the .val{1} field must be either  
            - empty  
            - an array of cfg_dep objects  
            - a cell string of file names.  
            In the latter case, the cell string will be filtered using   
            cfg_getfile('filter', item.val{1}, item.filter, '.*', 1:inf) and only  
            files matching item.filter will be assigned.  
             
            GUI Input  
            =========  
            The GUI uses   
            cfg_getfile(item.num, item.filter, item.name, item.val{1}, '.', item.ufilter)  
            to select files. The filter in item.filter can not be overridden by the  
            GUI.  
             
            Output in Job Structure (harvest)  
            =================================  
            cfg_files uses cfg_item/harvest. If multiple dependencies are present  
            and all can be resolved, the result will be a cell string containing a  
            concatenated list of files.  
             
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
            
              Documentation for cfg_files  
                 doc cfg_files  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/cfg_files.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("cfg_files", *args, **kwargs)
            
        super().__init__(_objdict)

    def _mysubs_fields(self, *args, **kwargs):
        """
          function [fnames, defaults] = mysubs_fields  
            Additional fields for class cfg_files. See help of  
            @cfg_item/subs_fields for general help about this function.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/private/mysubs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mysubs_fields", *args, **kwargs)
