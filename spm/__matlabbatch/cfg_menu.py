from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_menu(MatlabClassWrapper):
    def __init__(self, *args, **kwargs):
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
        super().__init__()

    def cfg2struct(self, *args, **kwargs):
        """
          function sitem = cfg2struct(item)  
            Return a struct containing all fields of item plus a field type. This is  
            the method suitable for entry classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/cfg2struct.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("cfg2struct", self._as_matlab_object(), *args, **kwargs)

    def fieldnames(self, *args, **kwargs):
        """
          function fn = fieldnames(item)  
            Return a list of all (inherited and non-inherited) field names.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/fieldnames.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fieldnames", self._as_matlab_object(), *args, **kwargs)

    def gencode_item(self, *args, **kwargs):
        """
          function [str, tag, cind, ccnt] = gencode_item(item, tag, tagctx, stoptag, tropts)  
            Generate code to recreate a generic item. This code does not deal with  
            arrays of cfg_items, such a configuration should not exist with the  
            current definition of a configuration tree.  
             
            Traversal options  
            struct with fields  
            stopspec - match spec to stop code generation  
            dflag    - (not used here)  
            clvl     - current level in tree  
            mlvl     - maximum level to generate - range 1 (top level only) to  
                       Inf (all levels)  
            cnt      - item count - used for unique tags  
            mcnt     - (not evaluated here)  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/gencode_item.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("gencode_item", self._as_matlab_object(), *args, **kwargs)

    def setval(self, *args, **kwargs):
        """
          function item = setval(item, val, dflag)  
            set item.val{1} to item.values{val}. If val == {}, set item.val to {}  
            If dflag is true, and item.cfg_item.def is not empty, set the default setting for  
            this item instead by calling feval(item.cfg_item.def{:}, val). If val == {}, use  
            the string '<UNDEFINED>' as in a harvested tree. If dflag is true, but  
            no item.cfg_item.def defined, set item.val{1} instead.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/setval.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("setval", self._as_matlab_object(), *args, **kwargs)

    def showdetail(self, *args, **kwargs):
        """
          function str = showdetail(item)  
            Display details for a cfg_menu and all of its options.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/showdetail.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("showdetail", self._as_matlab_object(), *args, **kwargs)

    def showdoc(self, *args, **kwargs):
        """
          function str = showdoc(item, indent)  
            Display help text for a cfg_menu and all of its options.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/showdoc.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("showdoc", self._as_matlab_object(), *args, **kwargs)

    def subs_fields(self, *args, **kwargs):
        """
          function fnames = subs_fields(item)  
            This function works as a "class-based switch" to return the value of  
            the private mysubs_fields function for the appropriate class.   
            This function is identical for all classes derived from cfg_item, but  
            it has to be in the class directory to access the proper private  
            function mysubs_fields.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/subs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subs_fields", self._as_matlab_object(), *args, **kwargs)

    def subsasgn(self, *args, **kwargs):
        """
          function item = subsasgn(item, subs, varargin)  
            This function implements subsasgn for all classes derived from cfg_item.  
            It relies on the capability of each class constructor to re-classify a  
            struct object after a new value has been assigned to its underlying  
            struct (This capability has to be implemented in the derived class).  
            The structure of a configuration tree does not permit any arrays of  
            cfg_item objects. Therefore, the only subscript reference and  
            assignment within an cfg_item is a dot assignment to fields of this  
            cfg_item.   
            Subscript references we have to deal with are:  
            one level  
            item.(field)   - i.e. struct('type',{'.'} ,'subs',{field})  
             
            to be dealt with elsewhere  
            item.(field){fidx}  
              
            In a future version, '()' and '{}' subscripts may be supported to  
            access val fields of a cfg_item tree as if they were part of a  
            harvested job. For cfg_branch objects (where dot assignments are used  
            for val fields in their job tree) it is mandatory to index the job as a  
            struct array to access harvested fields.  
            This function is identical for all classes derived from cfg_item. A  
            copy of it must be present in each derived class to be able to access  
            derived fields.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/subsasgn.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsasgn_check(self, *args, **kwargs):
        """
          function [sts, val] = subsasgn_check(item,subs,val)  
            Perform assignment checks for .val, .labels and .values field.   
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/subsasgn_check.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn_check", self._as_matlab_object(), *args, **kwargs)

    def subsref(self, *args, **kwargs):
        """
          function varargout = subsref(item, subs)  
            subscript references we have to deal with are:  
            one level  
            item.(field)   - i.e. struct('type',{'.'} ,'subs',{field})  
            item(idx)      - i.e. struct('type',{'()'},'subs',{idx})  
            two levels  
            item(idx).(field)  
             
            to be dealt with elsewhere  
            item.(field){fidx}  
            three levels  
            item(idx).(field){fidx}  
            This function is identical for all classes derived from cfg_item, but it  
            needs to be present in the class folder to access fields added by the  
            derived class.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_menu/subsref.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

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
        return Runtime.call("mysubs_fields", self._as_matlab_object(), *args, **kwargs)
