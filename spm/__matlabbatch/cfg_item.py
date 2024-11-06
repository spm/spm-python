from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_item(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          This is the generic configuration item class, from which all other  
            classes are derived.   
             
            Data structure  
            ==============  
            Description fields  
               * name  - display name of config item  
               * tag   - tag of the menu item  
               * val   - (optional) val field: cell array  
               * check - (optional) function handle to implement configuration  
                         specific checks based on the harvested subtree rooted at  
                         this node. It will be evaluated during harvest if all  
                         dependencies in the harvested subtree are resolved and all  
                         val's are set.   
                         This function should return an empty string on success and  
                         a string explaining why it failed otherwise.  
               * rewrite_job - (optional) function handle to rewrite a job prior to  
                         initialisation. This function will be called during  
                         initialise(), before any validity checks, subtree  
                         initialisation or value assignments are made. The function  
                         takes a proposed subjob as input, and should return a valid  
                         subjob as output. rewrite_job can be used to implement  
                         silent upgrades to jobs when configuration trees have  
                         changed.  
               * help  - help text  
               * def   - defaults setting (only evaluated for cfg_leaf items),  
                         holding a function handle. This function handle should  
                         accept both an empty and a non-empty argument list.  
                         If there is no .val{1} set for an cfg_leaf item,  
                         feval(def, {}) will be evaluated to retrieve a default value.  
                         Any value returned that does not match the size/type/filter  
                         etc. requirements of the item, will resolve to <UNDEFINED>.  
                         To change a default value, feval(def, {newval}) will be  
                         called. It is up to the defaults function to decide whether  
                         this value will be stored permanently or just for the  
                         current instance of the configuration tree. Only values  
                         which are valid entries for this field are accepted. If the  
                         value is not valid, it will not be changed.  
                         To use a registry like defaults function with key/value  
                         pairs as arguments, construct the function handle like this:  
                         @(defval)get_defaults('some.key', defval{:})  
                         This will result in 'get_defaults' being called with the key  
                         argument only for retrieving defaults, and with key plus  
                         defval arguments to set defaults.  
               * preview - (optional) A function callback that accepts the  
                         harvested configuration subtree rooted at this  
                         cfg_item. It is evaluated from the GUI and can be used to  
                         display information about the entered data. The GUI only  
                         calls this callback if the entire subtree is complete  
                         (all_leafs/all_set) and contains no dependency objects.  
            GUI/job manager fields  
               * expanded  
               * hidden  
             
            Public Methods  
            ==============  
               * get_strings - returns name of object  
                               No validity check performed here, this needs to be  
                               added in child class method.  
               * gettag      - returns tag  
               * help        - returns help text  
               * harvest     - returns item.val{1}, or '<UNDEFINED>' if empty, see below  
               * all_set     - returns ~isempty(item.val)  
             
            Public internal Methods  
            =======================  
               * subsasgn  
               * subsref  
               * display  
               * disp  
             
            Output in Job Structure (harvest)  
            =================================  
            cfg_item/harvest returns item.val{1}. If this is a dependency object  
            and dependencies shall and can be resolved the contents of the  
            dependencies will be returned. Otherwise the dependency object(s) will  
            be returned. This is the default behaviour for all cfg_leaf items.   
             
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
            
              Documentation for cfg_item  
                 doc cfg_item  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/cfg_item.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("cfg_item", *args, **kwargs)
            
        super().__init__(_objdict)

    def _mysubs_fields(self, *args, **kwargs):
        """
          function [fnames, defaults] = mysubs_fields  
            This function returns a cell string of names containing the fields  
            implemented by a derived class and their default values. It is called  
            from the class constructor directly and indirectly for subsasgn/subsref  
            via the subs_fields public function of each class.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/private/mysubs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mysubs_fields", *args, **kwargs)
