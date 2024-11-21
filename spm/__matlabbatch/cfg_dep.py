from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_dep(MatlabClassWrapper):
    def __init__(self, *args, **kwargs):
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
        super().__init__()

    def add_to_source(self, *args, **kwargs):
        """
          Add foreign target dependencies to own source dependencies  
            function [cj tdeps cflag dflag] = add_to_source(tdeps, cj)  
            This function adds target dependencies to the corresponding source  
            exbranches. If a source exbranch can not be found at the exact location  
            specified (e.g. because it has moved to a different level of the  
            configuration hierarchy), it will try to find the corresponding exbranch  
            and update the dependencies accordingly. If the dependencies can not be  
            found, they will be marked for deletion. Note that update and deletion of  
            dependencies for the current target item has to be done in the calling  
            cfg_exbranch/harvest call.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/add_to_source.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("add_to_source", self._as_matlab_object(), *args, **kwargs)

    def ctranspose(self, *args, **kwargs):
        """
          function b = ctranspose(a)  
            Transpose a configuration dependency  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2016 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/ctranspose.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("ctranspose", self._as_matlab_object(), *args, **kwargs)

    def del_in_source(self, *args, **kwargs):
        """
          function cj = del_in_source(tdeps, cj)  
            delete foreign target dependencies from own source dependencies.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/del_in_source.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("del_in_source", self._as_matlab_object(), *args, **kwargs)

    def del_in_target(self, *args, **kwargs):
        """
          function cj = del_in_target(sdeps, cj)  
            If a dependency source has changed, drop all dependent (target)  
            references. Since dependencies only depend on input structure, this does  
            not require recursive updates - the input structure of the dependent  
            cfg_exbranch does not change if one of its inputs is missing.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/del_in_target.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("del_in_target", self._as_matlab_object(), *args, **kwargs)

    def dep_add(self, *args, **kwargs):
        """
          augment cdep tsubs references, and add them to dependency list  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/dep_add.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("dep_add", self._as_matlab_object(), *args, **kwargs)

    def disp(self, *args, **kwargs):
        """
          function disp(obj)  
            Disp a configuration dependency  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/disp.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("disp", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def display(self, *args, **kwargs):
        """
          function display(dep)  
            Display a configuration dependency  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/display.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("display", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def gencode(self, *args, **kwargs):
        """
          function [str, tag, cind] = gencode(item, tag, tagctx)  
            Generate code to recreate an cfg_dep object.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/gencode.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("gencode", self._as_matlab_object(), *args, **kwargs)

    def isequalsource(self, *args, **kwargs):
        """
          function sts = isequalsource(dep1, dep2)  
            Compare source references of two dependencies and return true if both  
            point to the same object. If multiple dependencies are given, the  
            number and order of dependencies must match.  
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/isequalsource.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("isequalsource", self._as_matlab_object(), *args, **kwargs)

    def isequaltarget(self, *args, **kwargs):
        """
          function sts = isequaltarget(dep1, dep2)  
            Compare source references of two dependencies and return true if both  
            point to the same object. If multiple dependencies are given, the  
            number and order of dependencies must match.  
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/isequaltarget.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("isequaltarget", self._as_matlab_object(), *args, **kwargs)

    def subs_fields(self, *args, **kwargs):
        """
          function fnames = subs_fields(item)  
            This function works as a "class-based switch" to return the value of  
            the private mysubs_fields function for the appropriate class. It is  
            identical for each class, but it has to be in the class directory to  
            access the proper private function mysubs_fields.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/subs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subs_fields", self._as_matlab_object(), *args, **kwargs)

    def subsasgn(self, *args, **kwargs):
        """
          function dep = subsasgn(dep, subs, varargin)  
            subscript references we have to deal with are:  
            one level  
            dep.(field)   - i.e. struct('type',{'.'} ,'subs',{field})  
            dep(idx)      - i.e. struct('type',{'()'},'subs',{idx})  
            two levels  
            dep(idx).(field)  
             
            to be dealt with elsewhere  
            dep.(field){fidx}  
            three levels  
            dep(idx).(field){fidx}  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/subsasgn.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsref(self, *args, **kwargs):
        """
          function varargout = subsref(dep, subs)  
            subscript references we have to deal with are:  
            one level  
            dep.(field)   - i.e. struct('type',{'.'} ,'subs',{field})  
            dep(idx)      - i.e. struct('type',{'()'},'subs',{idx})  
            two levels  
            dep(idx).(field)  
             
            to be dealt with elsewhere  
            dep.(field){fidx}  
            three levels  
            dep(idx).(field){fidx}  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/subsref.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

    def update_deps(self, *args, **kwargs):
        """
          function dep = update_deps(dep, oid, nid)  
            go through an array of dependencies and update tgt_exbranch and src_exbranch entries.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_dep/update_deps.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("update_deps", self._as_matlab_object(), *args, **kwargs)

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
        return Runtime.call("mysubs_fields", self._as_matlab_object(), *args, **kwargs)
