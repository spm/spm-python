from spm.__wrapper__ import Runtime, MatlabClassWrapper


class cfg_item(MatlabClassWrapper):
    def __init__(self, *args, **kwargs):
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
        super().__init__()

    def all_leafs(self, *args, **kwargs):
        """
          function ok = all_leafs(item)  
            Generic all_leafs function that returns true. This is suitable for all  
            leaf items. No content specific checks are performed.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/all_leafs.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("all_leafs", self._as_matlab_object(), *args, **kwargs)

    def all_set(self, *args, **kwargs):
        """
          function ok = all_set(item)  
            Generic all_set function - checks whether item.val is not empty. No  
            checks based on the content of item.val are performed here.  
            Content checking is done in the following places:  
            * context-insensitive checks based on configuration specifications  
              are performed during subsasgn/setval. This will happen during user  
              input or while resolving dependencies during harvest.   
            * context sensitive checks by a configuration .check function are  
              performed during harvest after all dependencies are resolved.  
            This function is suitable for all leaf configuration items.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/all_set.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("all_set", self._as_matlab_object(), *args, **kwargs)

    def all_set_item(self, *args, **kwargs):
        """
          function ok = all_set_item(item)  
            Perform within-item all_set check. For generic items, this is the same  
            as all_set.  
             
            This code is part of a batch job configuration system for MATLAB. See  
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/all_set_item.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("all_set_item", self._as_matlab_object(), *args, **kwargs)

    def cat(self, *args, **kwargs):
        """
          function varargout = cat(varargin)  
            Prevent cat for cfg_item objects.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/cat.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("cat", self._as_matlab_object(), *args, **kwargs)

    def cfg2jobsubs(self, *args, **kwargs):
        """
          function jsubs = cfg2jobsubs(item, subs)  
            Return the subscript into the job tree for a given subscript vector into  
            the val part of the cfg tree. This generic function should be called only  
            for leafs (cfg_entry, cfg_file, cfg_menu) of the cfg tree. It returns the  
            subscripts that remain after item.val{1} has been addressed.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/cfg2jobsubs.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("cfg2jobsubs", self._as_matlab_object(), *args, **kwargs)

    def cfg2struct(self, *args, **kwargs):
        """
          function sitem = cfg2struct(item)  
            Return a struct containing all fields of item plus a field type. This is  
            the generic method.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/cfg2struct.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("cfg2struct", self._as_matlab_object(), *args, **kwargs)

    def clearval(self, *args, **kwargs):
        """
          function item = clearval(item, dflag)  
            This is a generic function to clear the contents of the val field of a  
            cfg_item. It is usable for all leaf cfg_item classes (cfg_entry,  
            cfg_files, cfg_menu).  
            dflag is ignored for leaf entries - the val field is cleared  
            unconditionally.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/clearval.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("clearval", self._as_matlab_object(), *args, **kwargs)

    def disp(self, *args, **kwargs):
        """
          function disp(obj)  
            Disp a configuration object. This function is generic, but it will be  
            called also for derived objects except cfg_exbranch. It will first  
            display fields inherited from cfg_item and then fields from the derived  
            item.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/disp.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("disp", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def display(self, *args, **kwargs):
        """
          function display(item)  
            Display a configuration object  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/display.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("display", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def docheck(self, *args, **kwargs):
        """
          function chk = docheck(item, val)  
            Run item specific check function, if present.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/docheck.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("docheck", self._as_matlab_object(), *args, **kwargs)

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
             
            This code is part of a batch job configuration system for MATLAB. See  
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/expand.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/fieldnames.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fieldnames", self._as_matlab_object(), *args, **kwargs)

    def fillvals(self, *args, **kwargs):
        """
          function [item, inputs] = fillvals(item, inputs, infcn)  
            If ~all_set_item, try to set item.val{1} to inputs{1}. Validity checks  
            are performed through subsasgn. If inputs{1} is not suitable for this  
            item, it is discarded. If infcn is a function handle,  
            [val sts] = infcn(item)   
            will be called to obtain a value for this item. This call will be  
            repeated until either val can be assigned to item or sts is true. val  
            should be a cell array with 1 item and val{1} the value that is to be  
            assigned to item.val{1}.  
            This function is suitable for all cfg_leaf items.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/fillvals.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fillvals", self._as_matlab_object(), *args, **kwargs)

    def gencode(self, *args, **kwargs):
        """
          function [str, tag, cind] = gencode(item, tag, tagctx)  
            Generate code to recreate a cfg_item object. This function calls the  
            cfg_item specific gencode_item method. Instead of creating one large,  
            deeply nested struct/cell array, it creates separate variables for each  
            cfg_item.  
             
            Input arguments:  
            item - MATLAB variable to generate code for (the variable itself, not its  
                   name)  
            tag     - optional: name of the variable, i.e. what will be displayed left  
                      of the '=' sign. This can also be a valid struct/cell array  
                      reference, like 'x(2).y'. If not provided, inputname(1) will be  
                      used.  
            tagctx  - optional: variable names not to be used (e.g. keywords,  
                      reserved variables). A cell array of strings.  
             
            Output arguments:  
            str  - cellstr containing code lines to reproduce   
            tag  - name of the generated variable  
            cind - index into str to the line where the variable assignment is coded  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/gencode.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("gencode", self._as_matlab_object(), *args, **kwargs)

    def gencode_item(self, *args, **kwargs):
        """
          function [str, tag, cind, ccnt] = gencode_item(item, tag, tagctx, stoptag, tropts)  
            Generate code to recreate a generic item. This code should be suitable  
            for all derived classes. Derived classes that add their own fields should  
            first call this code and then add code to recreate their additional  
            fields. This code does not deal with arrays of cfg_items, such a  
            configuration should not exist with the current definition of a  
            configuration tree.  
             
            Traversal options  
            struct with fields  
            stopspec - match spec to stop code generation  
            dflag    - (not used here)  
            clvl     - current level in tree  
            mlvl     - maximum level to generate - range 1 (top level only) to  
                       Inf (all levels)  
            cnt      - item count - used for unique tags  
            mcnt     - (not evaluated here)  
            Code generation stops at this item, if item matches tropts.stopspec or  
            tropts.clvl > tropts.mlvl. In this case, the tag of the item is  
            generated from genvarname(sprintf('%s%s', stoptag, tag), tagctx), but  
            no code is generated.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/gencode_item.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("gencode_item", self._as_matlab_object(), *args, **kwargs)

    def gettag(self, *args, **kwargs):
        """
          function tag = gettag(item)  
            Return the tag of the input item.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/gettag.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("gettag", self._as_matlab_object(), *args, **kwargs)

    def harvest(self, *args, **kwargs):
        """
          function [tag, val, typ, dep, chk, cj] = harvest(item, cj, dflag, rflag)  
            Generic harvest function, suitable for all const/entry items.  
            The configuration tree cj is passed unmodified. If rflag is true and a  
            dependency can be resolved, the resolved value will be returned,  
            otherwise the cfg_dep object will be returned in val and dep.  
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
             
            This code is part of a batch job configuration system for MATLAB. See  
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/harvest.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("harvest", self._as_matlab_object(), *args, **kwargs)

    def horzcat(self, *args, **kwargs):
        """
          function varargout = horzcat(varargin)  
            Prevent horzcat for cfg_item objects.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/horzcat.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("horzcat", self._as_matlab_object(), *args, **kwargs)

    def initialise(self, *args, **kwargs):
        """
          function item = initialise(item, val, dflag)  
            This is a generic initialisation function to insert values into the val  
            field of a cfg_item. It is usable for all leaf cfg_item classes  
            (cfg_entry, cfg_files, cfg_menu). Assignment checks are done through  
            subsasgn.  
            dflag is ignored for leaf entries - the passed value is assigned  
            unconditionally.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/initialise.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("initialise", self._as_matlab_object(), *args, **kwargs)

    def list(self, *args, **kwargs):
        """
          function [id, stop, val] = list(item, spec, tropts, fn)  
            This function searches the cfg tree for certain entries.  
             
            [id stop val] = list(item, spec, tropts[, fieldname])  
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
                             all integrity conditions for this node are fulfilled)  
                             For in-tree nodes this can be different from all_set.  
            'showdoc' - calls showdoc to display the help text and option hints for  
                        the current item.  
            This code is the generic list function, suitable for all cfg_leaf items.  
            To ensure that the correct val (val{1}, dependency or default value)  
            is listed, the val field is treated in a special way.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/list.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("list", self._as_matlab_object(), *args, **kwargs)

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
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/match.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("match", self._as_matlab_object(), *args, **kwargs)

    def resolve_deps(self, *args, **kwargs):
        """
          function [val, sts] = resolve_deps(item, cj)  
            Resolve dependencies for an cfg item. This is a generic function that  
            returns the contents of item.val{1} if it is an array of cfg_deps. If  
            there is more than one dependency, they will be resolved in order of  
            appearance. The returned val will be the concatenation of the values of  
            all dependencies. A warning will be issued if this concatenation fails  
            (which would happen if resolved dependencies contain incompatible  
            values).  
            If any of the dependencies cannot be resolved, val will be empty and sts  
            false.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/resolve_deps.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("resolve_deps", self._as_matlab_object(), *args, **kwargs)

    def setval(self, *args, **kwargs):
        """
          function item = setval(item, val, dflag)  
            set item.val{1} to val. Validity checks are performed through subsasgn.  
            If val == {}, set item.val to {}.   
            If dflag is true, and item.def is not empty, set the default setting for  
            this item instead by calling feval(item.def{:}, val). If val == {}, use  
            the string '<UNDEFINED>' as in a harvested tree. If dflag is true, but  
            no item.def defined, set item.val{1} instead.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/setval.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("setval", self._as_matlab_object(), *args, **kwargs)

    def showdetail(self, *args, **kwargs):
        """
          function str = showdetail(item)  
            Generic showdetail function for cfg_item classes. It displays the  
            name, tag, class and default function call for this item..  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/showdetail.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("showdetail", self._as_matlab_object(), *args, **kwargs)

    def showdoc(self, *args, **kwargs):
        """
          function str = showdoc(item, indent)  
            Generic showdoc function for cfg_item classes. It displays the  
            (indented) name of the item and the justified help text for this item.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/showdoc.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/subs_fields.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/subsasgn.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsasgn_check(self, *args, **kwargs):
        """
          function [sts, val] = subsasgn_check(item,subs,val)  
            Do a check for proper assignments of values to fields. This routine  
            will be called for derived objects from @cfg_.../subsasgn with the  
            original object as first argument and the proposed subs and val fields  
            before an assignment is made. It is up to each derived class to  
            implement assignment checks for both its own fields and fields  
            inherited from cfg_item. If used for assignment checks for inherited  
            fields, these must be dealt with in special cases in @cfg_.../subsasgn  
              
            This routine is a both a check for cfg_item fields and a fallback  
            placeholder in cfg_item if a derived class does not implement its own  
            checks. In this case it always returns true. A derived class may also  
            check assignments to cfg_item fields (e.g. to enforce specific validity  
            checks for .val fields). subsasgn_check of the derived class is called  
            before this generic subsasgn_check is called and both checks need to be  
            passed.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/subsasgn_check.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn_check", self._as_matlab_object(), *args, **kwargs)

    def subsasgn_checkstr(self, *args, **kwargs):
        """
          function checkstr = subsasgn_checkstr(item, subs)  
            Preformat a warning message suitable for all subsasgn_check functions  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/subsasgn_checkstr.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn_checkstr", self._as_matlab_object(), *args, **kwargs)

    def subsasgn_job(self, *args, **kwargs):
        """
          function item = subsasgn_job(item, subs, val)  
            Treat a subscript reference as a reference in a job structure instead  
            of a cfg_item structure. This generic cfg_item method treats subs as a  
            subscript reference into item.val{1}. This is suitable for all cfg_leaf  
            items.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/subsasgn_job.m )

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
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/subsref.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

    def subsref_job(self, *args, **kwargs):
        """
          function [ritem varargout] = subsref_job(item, subs, c0)  
            Treat a subscript reference as a reference in a job structure instead  
            of a cfg_item structure. This generic cfg_item method treats subs as a  
            subscript reference into item.val{1}. This is suitable for all cfg_leaf  
            items.  
            The third argument c0 is a copy of the entire job configuration. This  
            is only used to reference dependencies properly.  
            The first value returned is the referenced cfg_item object. The  
            following values are the results of sub-referencing into item.val{1}.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/subsref_job.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref_job", self._as_matlab_object(), *args, **kwargs)

    def tag2cfgsubs(self, *args, **kwargs):
        """
          function [id, stop, rtaglist] = tag2cfgsubs(item, taglist, finalspec, tropts)  
            Return the index into the values branch of a configuration tree which  
            corresponds to a list of tags.   
            This is the generic tag2cfgsubs function, suitable for all leaf  
            cfg_items. It stops with success, if the first element in taglist  
            matches gettag(item) and item matches finalspec. In this case, it  
            returns an empty substruct. If item matches tropts.stopspec or taglist  
            has more than one element then stop = true, else stop = false.  
            If unsuccessful, it returns an empty cell and stop = true.  
            rtaglist contains the remaining tags that were not matched due to a  
            stopping criterion.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/tag2cfgsubs.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("tag2cfgsubs", self._as_matlab_object(), *args, **kwargs)

    def update_deps(self, *args, **kwargs):
        """
          function item = update_deps(item, varargin)  
            This function will run cfg_dep/update_deps in all leaf (cfg_entry,  
            cfg_menu, cfg_files) nodes of a configuration tree and update their  
            dependency information (mod_job_ids) if necessary.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/update_deps.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("update_deps", self._as_matlab_object(), *args, **kwargs)

    def val2def(self, *args, **kwargs):
        """
          function [item, defaults] = val2def(item, defaults, funname, deftag)  
            If a cfg_leaf item has a value, extract it and generate code for defaults  
            retrieval. This function works in a way similar to harvest, but with a  
            much simpler logic. Also, it modifies the returned configuration tree by  
            clearing the .val fields if they are moved to defaults. If a .def field  
            is already present, its value will be evaluated and a new callback will  
            be installed.  
            Initially, defaults and deftag should be empty.  
            This function is identical for all cfg_leaf classes.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/val2def.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("val2def", self._as_matlab_object(), *args, **kwargs)

    def vertcat(self, *args, **kwargs):
        """
          function varargout = vertcat(varargin)  
            Prevent vertcat for cfg_item objects.  
             
            This code is part of a batch job configuration system for MATLAB. See   
                 help matlabbatch  
            for a general overview.  
           _______________________________________________________________________  
            Copyright (C) 2007 Freiburg Brain Imaging  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/@cfg_item/vertcat.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("vertcat", self._as_matlab_object(), *args, **kwargs)

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
        return Runtime.call("mysubs_fields", self._as_matlab_object(), *args, **kwargs)
