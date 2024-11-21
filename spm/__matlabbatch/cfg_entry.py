from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_entry(MatlabClassWrapper):
    def __init__(self, *args, **kwargs):
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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/cfg2struct.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/fieldnames.m )

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
            stopspec - match spec to stop forced setting of eflag  
            dflag    - (not used here)  
            clvl     - current level in tree  
            mlvl     - maximum level to force settings - range 1 (top level only) to  
                       Inf (all levels)  
            cnt      - item count - used for unique tags  
            mcnt     - (not evaluated here)  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/gencode_item.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("gencode_item", self._as_matlab_object(), *args, **kwargs)

    def match(self, *args, **kwargs):
        """
          sts = match(item, spec)  
            Spec must be a cell array of struct arrays with one or more fields. Each  
            struct must contain two fields - 'name' and 'value'.  
            An item matches, if it has a field with the specified field name and the  
            contents of this field equals the contents of spec.value. If the field  
            name is 'class', an item matches, if its class name is equal to  
            spec.value.  
            Matches within each struct array are OR-concatenated, while matches  
            between struct arrays are AND-concatenated.  
            An empty spec always matches.  
            Special matching rules for cfg_entries apply to the .strtype field.  
            An item.strtype  
            'e' - matches any strtype  
            'n' - matches strtype 'n'  
            'w' - matches strtype 'n', 'w'  
            'i' - matches strtype 'n', 'w', 'i'  
            'r' - matches strtype 'n', 'w', 'i', 'r'  
            Any other strtype matches only on equality.  
            An item with strtype 's+' also matches file lists.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/match.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("match", self._as_matlab_object(), *args, **kwargs)

    def showdetail(self, *args, **kwargs):
        """
          function str = showdetail(item)  
            Display details for a cfg_files item.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/showdetail.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("showdetail", self._as_matlab_object(), *args, **kwargs)

    def showdoc(self, *args, **kwargs):
        """
          function str = showdoc(item, indent)  
            Display help text for a cfg_entry item.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/showdoc.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/subs_fields.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/subsasgn.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsasgn_check(self, *args, **kwargs):
        """
          function [sts, val] = subsasgn_check(item,subs,val)  
            Perform validity checks for cfg_entry inputs. Does not yet support  
            evaluation of inputs.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/subsasgn_check.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_entry/subsref.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

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
        return Runtime.call("mysubs_fields", self._as_matlab_object(), *args, **kwargs)
