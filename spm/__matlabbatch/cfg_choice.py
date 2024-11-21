from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_choice(MatlabClassWrapper):
    def __init__(self, *args, **kwargs):
        """
          This is the choice configuration item class  
             
            Data structure  
            ==============  
            Description fields  
               * name  - display name of config item  
               * tag   - tag of the menu item  
               * val   - 1x1 cell array of cfg_items (not set initially)  
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
             
            Public Methods  
            ==============  
               * get_strings - returns name of object  
               * gettag      - returns tag  
               * help        - returns help text  
               * harvest     - a struct with a single field (see below)  
               * all_set     - returns all_set(item.val)  
             
            Output in Job Structure (harvest)  
            =================================  
            The resulting data structure is a struct with a single field.  The  
            name of the field is given by the 'tag' of the specified value.  
             
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
            
              Documentation for cfg_choice  
                 doc cfg_choice  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/cfg_choice.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        super().__init__()

    def all_leafs(self, *args, **kwargs):
        """
          function ok = all_leafs(item)  
            Return true, if all child items in item.val{:} consist of subtrees  
            ending in leaf nodes. Leaf nodes do not have to be set at this time and  
            no checks on their contents will be performed.  
            This function is identical for all in-tree items.   
             
            This code is part of a batch job configuration system for MATLAB. See  
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/all_leafs.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("all_leafs", self._as_matlab_object(), *args, **kwargs)

    def all_set(self, *args, **kwargs):
        """
          function ok = all_set(item)  
            Return true, if all child items in item.val{:} are set and item specific  
            criteria (i.e. number of element in .val) are met. No checks based on  
            the content of item.val are performed here.   
            Content checking is done in the following places:  
            * context-insensitive checks based on configuration specifications  
              are performed during subsasgn/setval. This will happen during user  
              input or while resolving dependencies during harvest.   
            * context sensitive checks by a configuration .check function are  
              performed during harvest after all dependencies are resolved.  
            This function is identical for all in-tree items.  
             
            This code is part of a batch job configuration system for MATLAB. See  
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/all_set.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("all_set", self._as_matlab_object(), *args, **kwargs)

    def all_set_item(self, *args, **kwargs):
        """
          function ok = all_set_item(item)  
            Perform within-item all_set check. For choices, this is true, if item.val  
            has one element.  
             
            This code is part of a batch job configuration system for MATLAB. See  
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/all_set_item.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("all_set_item", self._as_matlab_object(), *args, **kwargs)

    def cfg2jobsubs(self, *args, **kwargs):
        """
          function jsubs = cfg2jobsubs(item, subs)  
            Return the subscript into the job tree for a given subscript vector into  
            the val part of the cfg tree. In a cfg_choice, this is a struct reference  
            to a field with the name of the tag of the corresponding child node.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/cfg2jobsubs.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("cfg2jobsubs", self._as_matlab_object(), *args, **kwargs)

    def cfg2struct(self, *args, **kwargs):
        """
          function sitem = cfg2struct(item)  
            Return a struct containing all fields of item plus a field type. This is  
            the method suitable for cfg_choice and repeat classes. It descends down  
            the values field to convert the cfg_items in this field into structs.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/cfg2struct.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("cfg2struct", self._as_matlab_object(), *args, **kwargs)

    def checksubs_job(self, *args, **kwargs):
        """
          function [sts vind] = checksubs_job(item, subs, dflag)  
            Check whether a subscript reference is a valid reference in a job  
            structure starting at item. subs(1) should have a subscript type of  
            '.', and the subscript reference should be a tagname from item.val or  
            item.values, depending on dflag.  
             
            This function is identical for cfg_branch and cfg_(m)choice classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/checksubs_job.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("checksubs_job", self._as_matlab_object(), *args, **kwargs)

    def clearval(self, *args, **kwargs):
        """
          function item = clearval(item, dflag)  
            Clear val field, thereby removing the currently selected configuration  
            subtree. If dflag is set, then also all val fields in the item.values{:}  
            cfg_item(s) are cleared.   
            This function is identical for cfg_choice and cfg_repeat items.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/clearval.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("clearval", self._as_matlab_object(), *args, **kwargs)

    def expand(self, *args, **kwargs):
        """
          function [item, sts] = expand(item, eflag, tropts)  
            Set/query expanded flag of item depending on eflag:  
            -1 - do not force eflag to any state, only child state will be inherited  
             0 - collapse  
             1 - expand val unconditionally  
             2 - expand metadata unconditionally  
             3 - expand val, if it is not set  
            Return status is (expanded > 0), i.e. if expanded, then no additional  
            info about expansion level or expansion reason is returned and parent  
            nodes are set to expanded = 1.  
             
            Traversal options  
            struct with fields  
            stopspec - match spec to stop traversal  
            dflag    - traverse val or values tree  
            clvl     - current level in tree  
            mlvl     - maximum level to traverse - range 1 (top level only) to  
                       Inf (all levels)  
            cnt (not set here)  
            mcnt (not evaluated here)  
            Traversal options are used here to control which items should be forced  
            to expand/unexpand. Traversal continues to child items, even if level or  
            stopspec criteria are met, but with an eflag of -1 (i.e. only 'expanded'  
            status is queried, but not changed).  
             
            This function is identical for all cfg_intree classes.  
             
            This code is part of a batch job configuration system for MATLAB. See  
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/expand.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("expand", self._as_matlab_object(), *args, **kwargs)

    def fieldnames(self, *args, **kwargs):
        """
          function fn = fieldnames(item)  
            Return a list of all (inherited and non-inherited) field names.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/fieldnames.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fieldnames", self._as_matlab_object(), *args, **kwargs)

    def fillvals(self, *args, **kwargs):
        """
          function [item, inputs] = fillvals(item, inputs, infcn)  
            If ~all_set_item, try to set item.val to the items listed in inputs{1}.  
            inputs{1} should be a cell array of indices into item.values. For  
            cfg_choice items, this list should only contain one item.  
            Validity checks are performed through setval. If inputs{1} is not  
            suitable for this item, it is discarded. If infcn is a function handle,  
            [val sts] = infcn(item)   
            will be called to obtain a value for this item. This call will be  
            repeated until either val can be assigned to item or sts is true.  
             
            This function is identical for all cfg_intree classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/fillvals.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fillvals", self._as_matlab_object(), *args, **kwargs)

    def gencode_item(self, *args, **kwargs):
        """
          function [str, tag, cind, ccnt] = gencode_item(item, tag, tagctx, stoptag, tropts)  
            Generate code to recreate a cfg_(m)choice item. This code does not deal with  
            arrays of cfg_items, such a configuration should not exist with the  
            current definition of a configuration tree.  
             
            Traversal options  
            struct with fields  
            stopspec - match spec to stop forced setting of eflag  
            dflag    - if set to true, don't create code for .val children (code  
                       for .val field is created)  
            clvl     - current level in tree  
            mlvl     - maximum level to force settings - range 1 (top level only) to  
                       Inf (all levels)  
            cnt      - item count - used for unique tags  
            mcnt     - (not evaluated here)  
             
            This function is identical for cfg_choice and cfg_mchoice classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/gencode_item.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("gencode_item", self._as_matlab_object(), *args, **kwargs)

    def harvest(self, *args, **kwargs):
        """
          function [tag, val, typ, dep, chk, cj] = harvest(item, cj, dflag, rflag)  
            Harvest a cfg_branch object.  
            Input arguments:  
            item  - item to be harvested  
            cj    - configuration tree (passed unmodified)  
            dflag - if true, harvest defaults tree, otherwise filled tree  
            rflag - if true, resolve dependencies in leaf nodes  
            Output arguments:  
            tag - tag of harvested item  
            val - harvested value  
            typ - class of harvested item (currently unused)  
            dep - list of unresolved dependencies  
            chk - meaningful if ~dflag and all dependencies are resolved. Then it  
                  returns success status of this item's .check function and its  
                  children's check functions. A job is ready to run if all  
                  dependencies are resolved and chk status is true.  
             
            This function is identical for cfg_branch and cfg_(m)choice classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/harvest.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("harvest", self._as_matlab_object(), *args, **kwargs)

    def initialise(self, *args, **kwargs):
        """
          function item = initialise(item, val, dflag)  
            Initialise a configuration tree with values. If val is a job  
            struct/cell, only the parts of the configuration that are present in  
            this job will be initialised. If dflag is true, then matching items  
            from item.values will be initialised. If dflag is false, the matching  
            item from item.values will be added to item.val and initialised after  
            copying.  
            If val has the special value '<DEFAULTS>', the entire configuration  
            will be updated with values from .def fields. If a .def field is  
            present in a cfg_leaf item, the current default value will be inserted,  
            possibly replacing a previously entered (default) value. If dflag is  
            true, defaults will only be set in item.values. If dflag is false,  
            defaults will be set for both item.val and item.values.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/initialise.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("initialise", self._as_matlab_object(), *args, **kwargs)

    def list(self, *args, **kwargs):
        """
          function [id, stop, val] = list(item, spec, tropts, fn)  
            Find items in a cfg tree rooted at item that match a specification spec.  
            By default, the filled configuration tree is searched (i.e. the  
            val-branches of cfg_repeat and cfg_choice nodes).   
            See MATCH for help about spec data structure.  
             
            Traversal options  
            struct with fields  
            stopspec - match spec to stop traversal  
            dflag    - traverse val or values tree  
            clvl     - current level in tree  
            mlvl     - maximum level to traverse - range 1 (top level only) to  
                       Inf (all levels)  
            cnt      - #items found so far  
            mcnt    - max #items to find  
            List will stop descending into subtrees if one of the conditions  
            following conditions are met: item matches stopspec, clvl >= mlvl, cnt >=  
            mcnt. Flag stop is true for nodes where traversal has stopped  
            (i.e. items where tropts has stopped further traversal).  
             
            A cell list of subsref ids to matching nodes will be returned. The id of  
            this node is returned before the id of its matching children.  
            If the root node of the tree matches, the first id returned will be an  
            empty substruct.  
            If a cell list of fieldnames is given, then the contents of these fields  
            will be returned in the cell array val. If one of the fields does not  
            exist, a cell with an empty entry will be returned.  
            There are five pseudo-fieldnames which allow to obtain information useful  
            to build e.g. a user interface for cfg trees:  
            'class' - returns the class of the current item  
            'level' - returns the level in the tree. Since data is collected  
                      pre-order, children are listed after their parents. Identical  
                      levels of subsequent nodes denote siblings, whereas decreasing  
                      levels of subsequent nodes denote siblings of the parent node.  
            'all_set' - return all_set status of subtree rooted at item, regardless  
                        whether list will descend into it or not  
            'all_set_item' - return all_set_item status of current node (i.e. whether  
                             all integrity conditions for this node are fulfilled).  
                             For in-tree nodes this can be different from all_set.  
            'showdoc' - calls showmydoc to display the help text and option hints for  
                        the current item (without recursive calls for .val/.values  
                        items).  
             
            This function is identical for all cfg_intree classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/list.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("list", self._as_matlab_object(), *args, **kwargs)

    def setval(self, *args, **kwargs):
        """
          function item = setval(item, val, dflag)  
            Set item.val{1} to item.values{val(1)}. If isempty(val), set item.val to {}.  
            dflag is ignored for cfg_choice items.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/setval.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("setval", self._as_matlab_object(), *args, **kwargs)

    def showdetail(self, *args, **kwargs):
        """
          function str = showdetail(item)  
            Display details for a cfg_choice and all of its options.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/showdetail.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("showdetail", self._as_matlab_object(), *args, **kwargs)

    def showdoc(self, *args, **kwargs):
        """
          function str = showdoc(item, indent)  
            Display help text for a cfg item and all of its options.  
             
            This function is identical for all cfg_intree classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/showdoc.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("showdoc", self._as_matlab_object(), *args, **kwargs)

    def showmydoc(self, *args, **kwargs):
        """
          function str = showmydoc(item, indent)  
            Display help text for a cfg_choice and all of its options, without  
            recursive calls to child nodes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/showmydoc.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("showmydoc", self._as_matlab_object(), *args, **kwargs)

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/subs_fields.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/subsasgn.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsasgn_check(self, *args, **kwargs):
        """
          function [sts, val] = subsasgn_check(item,subs,val)  
            Check assignments to item.values and item.val.   
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/subsasgn_check.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn_check", self._as_matlab_object(), *args, **kwargs)

    def subsasgn_job(self, *args, **kwargs):
        """
          function item = subsasgn_job(item, subs, val)  
            Treat a subscript reference as a reference in a job structure instead  
            of a cfg_item structure. If subs is empty, then the subtree  
            beginning at item will be initialised with val. Otherwise, subs(1)  
            should have a subscript type of '.' in combination with a tagname from  
            item.val.   
             
            This function is identical for cfg_branch and cfg_(m)choice classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/subsasgn_job.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn_job", self._as_matlab_object(), *args, **kwargs)

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/subsref.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

    def subsref_job(self, *args, **kwargs):
        """
          function [ritem varargout] = subsref_job(item, subs, c0)  
            Treat a subscript reference as a reference in a job structure instead  
            of a cfg_item structure. If subs is empty, then the harvested subtree  
            beginning at item will be returned. Otherwise, subs(1) should have a  
            subscript type of '.' in combination with a tagname from item.val.  
            The third argument c0 is a copy of the entire job configuration. This  
            is only used to reference dependencies properly.  
            The first values returned is the referenced cfg_item object. The  
            following values are the results of sub-referencing into item.val{x}.  
             
            This function is identical for cfg_branch and cfg_(m)choice classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/subsref_job.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref_job", self._as_matlab_object(), *args, **kwargs)

    def tag2cfgsubs(self, *args, **kwargs):
        """
          function [id, stop, rtaglist] = tag2cfgsubs(item, taglist, finalspec, tropts)  
            Return the index into the values branch of a configuration tree which  
            corresponds to a list of tags.   
            Traversal stops if taglist contains only one element or item matches a  
            non-empty tropts.stopspec. In this case, stop returns the match status.  
            Id is an empty substruct, if gettag(item) matches taglist{1} and item  
            matches finalspec, otherwise it is an empty cell.  
            If taglist contains more than one element and taglist{2} matches any tag  
            of a .val element, then the subscript index to this element is returned.  
            If the recursive match was unsuccessful, it returns an empty cell and  
            stop = true.  
            rtaglist contains the remaining tags that were not matched due to a  
            stopping criterion.  
             
            This function is identical for all cfg_intree classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/tag2cfgsubs.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("tag2cfgsubs", self._as_matlab_object(), *args, **kwargs)

    def tagnames(self, *args, **kwargs):
        """
          function tn = tagnames(item, dflag)  
            Return the tags of all children in the job tree of an item. dflag  
            indicates whether the filled (false) or defaults (true) part of the  
            tree should be searched.   
             
            This function is identical for all cfg_intree classes.  
            It is not defined for leaf items.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/tagnames.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("tagnames", self._as_matlab_object(), *args, **kwargs)

    def treepart(self, *args, **kwargs):
        """
          function tname = treepart(item, dflag)  
            tree part to search - for cfg_repeat/cfg_choice this is val for filled  
            cfg_items and values for default cfg_items.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/treepart.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("treepart", self._as_matlab_object(), *args, **kwargs)

    def update_deps(self, *args, **kwargs):
        """
          function item = update_deps(item, varargin)  
            This function will run cfg_dep/update_deps in all leaf (cfg_entry,  
            cfg_menu, cfg_files) nodes of a configuration tree and update their  
            dependency information (mod_job_ids) if necessary.  
             
            This function is identical for all cfg_intree classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/update_deps.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("update_deps", self._as_matlab_object(), *args, **kwargs)

    def val2def(self, *args, **kwargs):
        """
          function [item, defaults] = val2def(item, defaults, funname, deftag)  
            If a cfg_leaf item has a value, extract it and generate code for defaults  
            retrieval. This function works in a way similar to harvest, but with a  
            much simpler logic. Also, it modifies the returned configuration tree by  
            clearing the .val fields if they are moved to defaults.  
            Initially, defaults and deftag should be empty.  
             
            This function is identical for cfg_branch and cfg_(m)choice classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/val2def.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("val2def", self._as_matlab_object(), *args, **kwargs)

    def _mysubs_fields(self, *args, **kwargs):
        """
          function [fnames, defaults] = mysubs_fields  
            Additional fields for class cfg_choice. See help of  
            @cfg_item/subs_fields for general help about this function.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_choice/private/mysubs_fields.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mysubs_fields", self._as_matlab_object(), *args, **kwargs)
