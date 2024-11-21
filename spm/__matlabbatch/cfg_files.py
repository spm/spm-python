from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_files(MatlabClassWrapper):
    def __init__(self, *args, **kwargs):
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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/cfg2struct.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/fieldnames.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/gencode_item.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("gencode_item", self._as_matlab_object(), *args, **kwargs)

    def match(self, *args, **kwargs):
        """
          function sts = match(item, spec)  
            This function is an implementation of find to search the cfg tree for  
            certain entries.  
             
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
            Special matching rules for cfg_files apply to the .filter field, if  
            both item.filter and spec.value are one of the special types 'any',  
            'image', 'nifti', 'mat', 'xml', 'batch', 'dir':  
            A .filter 'any' matches any spec.value. All other filters only match if  
            strcmpi(item.filter,spec.value) is true. Currently, 'nifti' and 'image'  
            filters are treated as equivalent.  
            Checking the equivalence of two regular expressions is a demanding  
            task. Therefore, no matching is performed if item.filter or spec.value  
            are regular expressions and this match will always be true.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/match.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/showdetail.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("showdetail", self._as_matlab_object(), *args, **kwargs)

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/subs_fields.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/subsasgn.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsasgn_check(self, *args, **kwargs):
        """
          function [sts, val] = subsasgn_check(item,subs,val)  
            Perform assignment checks for .num field. Checks for .val field could  
            include filtering and numel checks, if inputs are not passed as  
            reference.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/subsasgn_check.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_files/subsref.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

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
        return Runtime.call("mysubs_fields", self._as_matlab_object(), *args, **kwargs)
