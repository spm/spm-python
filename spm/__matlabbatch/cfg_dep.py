from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_dep(MatlabClassWrapper):
    def __init__(self, *args, _objdict=None, **kwargs):
        """
          This is the configuration dependency class  
             
            Data structure  
            ==============  
            Description fields  
               * sname        - display name of dependency source  
               * src_exbranch - subsref/subsasgn struct referencing the dependency  
                                source exbranch  
               * src_output   - subsref/subsasgn struct referencing the dependency  
                                source output item  
               * tname        - display name of dependency target  
               * tgt_exbranch - subsref/subsasgn struct referencing the dependency  
                                target exbranch in the config tree  
               * tgt_input    - subsref/subsasgn struct referencing the dependency  
                                target item in the config tree  
               * tgt_spec     - an cfg_findspec that can be used to restrict matches  
                                of this dependency to certain input items - this will  
                                be checked in subsasgn checks for cfg_items. Defaults  
                                to {} - match all cfg_items.  
               * jtsubs       - subsref/subsasgn struct referencing the dependency  
                                target item in the job tree (this is currently not  
                                used and may be removed in future)  
             
            Public Methods  
            ==============  
             
            Public internal Methods  
            =======================  
               * subsasgn  
               * subsref  
               * display  
               * disp  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
            
              Documentation for cfg_dep  
                 doc cfg_dep  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/cfg_dep.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        if _objdict is None:
            _objdict = Runtime.call("cfg_dep", *args, **kwargs)
            
        super().__init__(_objdict)

    def _mysubs_fields(self, *args, **kwargs):
        """
          function fnames = mysubs_fields(dep)  
            This function returns a cell string of names containing the fields  
            implemented by the cfg_dep class. It is called from @cfg_dep/subsasgn  
            and @cfg_item/subsref to allow references to valid fields for this class.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/private/mysubs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mysubs_fields", *args, **kwargs)
