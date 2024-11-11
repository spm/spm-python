from spm.__wrapper__ import Runtime


def cfg_util(*args, **kwargs):
    """
      This is the command line interface to the batch system. It manages the  
        following structures:  
        * Generic configuration structure c0. This structure will be initialised  
          to an cfg_repeat with empty .values list. Each application should  
          provide an application-specific master configuration file, which  
          describes the executable module(s) of an application and their inputs.  
          This configuration will be rooted directly under the master  
          configuration node. In this way, modules of different applications can  
          be combined with each other.  
          CAVE: the root nodes of each application must have an unique tag -  
          cfg_util will refuse to add an application which has a root tag that is  
          already used by another application.  
        * Job specific configuration structure cj. This structure contains the  
          modules to be executed in a job, their input arguments and  
          dependencies between them. The layout of cj is not visible to the user.  
        To address executable modules and their input values, cfg_util will  
        return id(s) of unspecified type. If necessary, these id(s) should be  
        stored in cell arrays in a calling application, since their internal  
        format may change.  
         
        The commands to manipulate these structures are described below in  
        alphabetical order.  
         
         cfg_util('addapp', cfg[, def[, ver]])  
         
        Add an application to cfg_util. If cfg is a cfg_item, then it is used  
        as initial configuration. Alternatively, if cfg is a MATLAB function,  
        this function is evaluated. The return argument of this function must be  
        a single variable containing the full configuration tree of the  
        application to be batched.  
        Optionally, a defaults configuration struct or function can be supplied.  
        This function must return a single variable containing a (pseudo) job  
        struct/cell array which holds defaults values for configuration items.  
        These defaults should be rooted at the application's root node, not at  
        the overall root node. They will be inserted by calling initialise on the  
        application specific part of the configuration tree.  
        Optionally, a version string can be specified. This version string will  
        be documented in all batches that are saved as .m files.  
         
         mod_job_id = cfg_util('addtojob', job_id, mod_cfg_id)  
         
        Append module with id mod_cfg_id in the cfg tree to job with id  
        job_id. Returns a mod_job_id, which can be passed on to other cfg_util  
        callbacks that modify the module in the job.  
         
         [new_job_id] = cfg_util('clonejob', job_id)  
         
        Clone an already initialised job.   
         
         [mod_job_idlist, new2old_id] = cfg_util('compactjob', job_id)  
         
        Modifies the internal representation of a job by removing deleted modules  
        from the job configuration tree. This will invalidate all mod_job_ids and  
        generate a new mod_job_idlist.  
        A translation table new2old_id is provided, where   
         mod_job_idlist = old_mod_job_idlist{new2old_id}  
        translates between an old id list and the compact new id list.  
         
         cfg_util('dbstop', job_id, mod_job_id)  
         
        Set a breakpoint at the beginning of the function that executes the  
        module. If a module occurs more than once in a job or its .prog is a  
        multi-purpose function, execution will stop at all calls of that function.  
         
         cfg_util('delfromjob', job_id, mod_job_id)  
         
        Delete a module from a job.  
         
         cfg_util('deljob', job_id)  
         
        Delete job with job_id from the job list.   
         
         sts = cfg_util('filljob', job_id, input1, ..., inputN)  
         sts = cfg_util('filljobui', job_id, ui_fcn, input1, ..., inputN)  
         
        Fill missing inputs in a job from a list of input items. For  
        cfg_entry/cfg_files, each input should be suitable to be assigned to  
        item.val{1}. For cfg_menu, input should be an index into the menu list as  
        displayed in the GUI, starting with 1.   
        If an item can not be filled by the specified input, this input will be  
        discarded. If cfg_util('filljobui'...) is called, [val sts] =  
        ui_fcn(item) will be run and should return a value which is suitable for  
        setval(item, val, false). sts should be set to true if input should  
        continue with the next item. This can result in an partially filled job.  
        If ui_fcn is interrupted, the job will stay unfilled.  
        If cfg_util('filljob'...) is called, the current job can become partially  
        filled.  
        Returns the all_set status of the filled job, returns always false if  
        ui_fcn is interrupted.  
         
         cfg_util('gencode', fname, apptag|cfg_id[, tropts])  
         
        Generate code from default configuration structure, suitable for  
        recreating the tree structure. Note that function handles may not be  
        saved properly. By default, the entire tree is saved into a file fname.  
        If tropts is given as a traversal option specification, code generation  
        will be split at the nodes matching tropts.stopspec. Each of these nodes will  
        generate code in a new file with filename cfg_util_<tag of node>, and the  
        nodes up to tropts.stopspec will be saved into fname.  
        If a file named cfg_util_mlb_preamble.m exists in the folder where the  
        configuration code is being written, it will be read in literally  
        and its contents will be prepended to each of the created files. This  
        allows to automatically include e.g. copyright or revision.  
         
         cfg_util('genscript', job_id, scriptdir, filename)  
          
        Generate a script which collects missing inputs of a batch job and runs  
        the job using cfg_util('filljob', ...). The script will be written to  
        file filename.m in scriptdir, the job will be saved to filename_job.m in  
        the same folder. The script must be completed by adding code to collect  
        the appropriate inputs for the job.  
         
         outputs = cfg_util('getAllOutputs', job_id)  
          
        outputs - cell array with module outputs. If a module has not yet been  
                  run, a cfg_inv_out object is returned.  
         
         voutputs = cfg_util('getAllVOutputs', job_id[, mod_job_id])  
          
        voutputs - cell array with virtual output descriptions (cfg_dep objects).  
                   These describe the structure of the job outputs. To create  
                   dependencies, they can be entered into matching input objects  
                   in subsequent modules of the same job.  
                   If mod_job_id is supplied, only virtual output descriptions of  
                   the referenced module are returned.  
         
         cfg = cfg_util('getcfg')  
         
        Get internal cfg representation from cfg_util.  
         
         diary = cfg_util('getdiary', job_id)  
         
        diary - cellstr containing command window output of job execution.  
        If cfg_get_defaults('cfg_util.run_diary') is set to true, cfg_util will  
        use MATLABs diary function to capture all command line output of a  
        running job. cfg_util('getdiary', jobid) retrieves the last diary saved  
        for a job.  
         
         [mod_job_idlist, mod_names, mod_item_idx, ...  
          item_mod_idlists, item_names] = cfg_util('getopeninputs', cjob)  
         
        List all modules and input items that are not yet filled in a job  
        template. This is a combination of 'showjob' and parts of 'showmod' to  
        access only unset input items in an entire job.  
        mod_job_idlist - cell list of module ids with open inputs  
        mod_names      - names of modules with open inputs  
        mod_item_idx   - index into mod_job_idlist/mod_names to match a  
                         linearized version of item_mod_idlists/item_names  
        item_mod_idlists - cell list of item_mod_ids with open inputs. One cell  
                           entry per module, containing the within-module  
                           item_mod_idlist.  
        item_names     - cell list of item name lists for each item with open  
                         inputs.  
         
         [tag, val] = cfg_util('harvest', job_id[, mod_job_id[, item_mod_id]])  
         
        Harvest is a method defined for all 'cfg_item' objects. It collects the  
        entered values and dependencies of the input items in the tree and  
        assembles them in a struct/cell array.  
        If only job_id is supplied, the internal configuration tree will be  
        cleaned up before harvesting. Dependencies will not be resolved in this  
        case. The internal state of cfg_util is not modified in this case. The  
        structure returned in val may be saved to disk as a job and can be loaded  
        back into cfg_util using the 'initjob' command.  
        If a mod_job_id, but not an item_mod_id is supplied, only the relevant  
        part of the configuration tree is harvested, dependencies are resolved  
        and the internal state of cfg_util is updated. In this case, the val  
        output is only part of a job description. It can be used as an input  
        argument to the corresponding module's .prog function, but can not be  
        loaded back into cfg_util.  
        If all ids are supplied, the configuration tree starting at the  
        specified item will be harvested. No dependencies will be resolved, and  
        no cleanup will be done.  
         
         [tag, appdef] = cfg_util('harvestdef'[, apptag|cfg_id])  
         
        Harvest the defaults branches of the current configuration tree. If  
        apptag is supplied, only the subtree of that application whose root tag  
        matches apptag/whose id matches cfg_id is harvested. In this case,  
        appdef is a struct/cell array that can be supplied as a second argument  
        in application initialisation by cfg_util('addapp', appcfg,  
        appdef).   
        If no application is specified, defaults of all applications will be  
        returned in one struct/cell array.   
          
         [tag, val] = cfg_util('harvestrun', job_id)  
         
        Harvest data of a job that has been (maybe partially) run, resolving  
        all dependencies that can be resolved. This can be used to document  
        what has actually been done in a job and which inputs were passed to  
        modules with dependencies.  
        If the job has not been run yet, tag and val will be empty.  
         
         cfg_util('initcfg')  
         
        Initialise cfg_util configuration. All currently added applications and  
        jobs will be cleared.  
        Initial application data will be initialised to a combination of  
        cfg_mlbatch_appcfg.m files in their order found on the MATLAB path. Each  
        of these config files should be a function with calling syntax  
          function [cfg, def] = cfg_mlbatch_appcfg(varargin)   
        This function should do application initialisation (e.g. add  
        paths). cfg and def should be configuration and defaults data  
        structures or the name of m-files on the MATLAB path containing these  
        structures. If no defaults are provided, the second output argument  
        should be empty.  
        cfg_mlbatch_appcfg files are executed in the order they are found on  
        the MATLAB path with the one first found taking precedence over  
        following ones.  
         
         cfg_util('initdef', apptag|cfg_id[, defvar])  
         
        Set default values for application specified by apptag or  
        cfg_id. If defvar is supplied, it should be any representation of a  
        defaults job as returned by cfg_util('harvestdef', apptag|cfg_id),  
        i.e. a MATLAB variable, a function creating this variable...  
        Defaults from defvar are overridden by defaults specified in .def  
        fields.  
        New defaults only apply to modules added to a job after the defaults  
        have been loaded. Saved jobs and modules already present in the current  
        job will not be changed.  
         
         [job_id, mod_job_idlist] = cfg_util('initjob'[, job])  
         
        Initialise a new job. If no further input arguments are provided, a new  
        job without modules will be created.  
        If job is given as input argument, the job tree structure will be  
        loaded with data from the struct/cell array job and a cell list of job  
        ids will be returned.  
        The new job will be appended to an internal list of jobs. It must  
        always be referenced by its job_id.  
         
         sts = cfg_util('isjob_id', job_id)  
         sts = cfg_util('ismod_cfg_id', mod_cfg_id)  
         sts = cfg_util('ismod_job_id', job_id, mod_job_id)  
         sts = cfg_util('isitem_mod_id', item_mod_id)  
        Test whether the supplied id seems to be of the queried type. Returns  
        true if the id matches the data format of the queried id type, false  
        otherwise. For item_mod_ids, no checks are performed whether the id is  
        really valid (i.e. points to an item in the configuration  
        structure). This can be used to decide whether 'list*' or 'tag2*'  
        callbacks returned valid ids.  
         
         [mod_cfg_idlist, stop, [contents]] = cfg_util('listcfg[all]', mod_cfg_id, find_spec[, fieldnames])  
         
        List modules and retrieve their contents in the cfg tree, starting at  
        mod_cfg_id. If mod_cfg_id is empty, search will start at the root level  
        of the tree. The returned mod_cfg_id_list is always relative to the root  
        level of the tree, not to the mod_cfg_id of the start item. This search  
        is designed to stop at cfg_exbranch level. Its behaviour is undefined if  
        mod_cfg_id points to an item within an cfg_exbranch. See 'match' and  
        'cfg_item/find' for details how to specify find_spec. A cell list of  
        matching modules is returned.  
        If the 'all' version of this command is used, also matching  
        non-cfg_exbranch items up to the first cfg_exbranch are returned. This  
        can be used to build a menu system to manipulate configuration.  
        If a cell array of fieldnames is given, contents of the specified fields  
        will be returned. See 'cfg_item/list' for details. This callback is not  
        very specific in its search scope. To find a cfg_item based on the  
        sequence of tags of its parent items, use cfg_util('tag2mod_cfg_id',  
        tagstring) instead.  
         
         [item_mod_idlist, stop, [contents]] = cfg_util('listmod', job_id, mod_job_id, item_mod_id, find_spec[, tropts][, fieldnames])  
         [item_mod_idlist, stop, [contents]] = cfg_util('listmod', mod_cfg_id, item_mod_id, find_spec[, tropts][, fieldnames])  
         
        Find configuration items starting in module mod_job_id in the job  
        referenced by job_id or in module mod_cfg_id in the defaults tree,  
        starting at item item_mod_id. If item_mod_id is an empty array, start  
        at the root of a module. By default, search scope are the filled items  
        of a module. See 'match' and 'cfg_item/find' for details how to specify  
        find_spec and tropts and how to search the default items instead of the  
        filled ones. A cell list of matching items is returned.  
        If a cell array of fieldnames is given, contents of the specified fields  
        will be returned. See 'cfg_item/list' for details.  
         
         sts = cfg_util('match', job_id, mod_job_id, item_mod_id, find_spec)  
         
        Returns true if the specified item matches the given find spec and false  
        otherwise. An empty item_mod_id means that the module node itself should  
        be matched.  
         
         new_mod_job_id = cfg_util('replicate', job_id, mod_job_id[, item_mod_id, val])  
         
        If no item_mod_id is given, replicate a module by appending it to the  
        end of the job with id job_id. The values of all items will be  
        copied. This is in contrast to 'addtojob', where a module is added with  
        default settings. Dependencies where this module is a target will be  
        kept, whereas source dependencies will be dropped from the copied module.  
        If item_mod_id points to a cfg_repeat object within a module, its  
        setval method is called with val. To achieve replication, val(1) must  
        be finite and negative, and val(2) must be the index into item.val that  
        should be replicated. All values are copied to the replicated entry.  
         
         cfg_util('run'[, job|job_id])  
         
        Run the currently configured job. If job is supplied as argument and is  
        a harvested job, then cfg_util('initjob', job) will be called first. If  
        job_id is supplied and is a valid job_id, the job with this job id will  
        be run.  
        The job is harvested and dependencies are resolved if possible.  
        If cfg_get_defaults('cfg_util.runparallel') returns true, all  
        modules without unresolved dependencies will be run in arbitrary order.  
        Then the remaining modules are harvested again and run, if their  
        dependencies can be resolved. This process is iterated until no modules  
        are left or no more dependencies can resolved. In a future release,  
        independent modules may run in parallel, if there are licenses to the  
        Distributed Computing Toolbox available.  
        Note that this requires dependencies between modules to be described by  
        cfg_dep objects. If a module e.g. relies on file output of another module  
        and this output is already specified as a filename of a non-existent  
        file, then the dependent module may be run before the file is created.  
        Side effects (changes in global variables, working directories) are  
        currently not modeled by dependencies.  
        If a module fails to execute, computation will continue on modules that  
        do not depend on this module. An error message will be logged and the  
        module will be reported as 'failed to run' in the MATLAB command window.  
         
         cfg_util('runserial'[, job|job_id])  
         
        Like 'run', but force cfg_util to run the job as if each module was  
        dependent on its predecessor. If cfg_get_defaults('cfg_util.runparallel')  
        returns false, cfg_util('run',...) and cfg_util('runserial',...) are  
        identical.  
         
         cfg_util('savejob', job_id, filename)  
         
        The current job will be save to the .m file specified by filename. This  
        .m file contains MATLAB script code to recreate the job variable. It is  
        based on gencode (part of this MATLAB batch system) for all standard  
        MATLAB types. For objects to be supported, they must implement their own  
        gencode method.  
         
         cfg_util('savejobrun', job_id, filename)  
         
        Save job after it has been run, resolving dependencies (see  
        cfg_util('harvestrun',...)). If the job has not been run yet, nothing  
        will be saved.  
         
         sts = cfg_util('setval', job_id, mod_job_id, item_mod_id, val)  
         
        Set the value of item item_mod_id in module mod_job_id to val. If item is  
        a cfg_choice, cfg_repeat or cfg_menu and val is numeric, the value will  
        be set to item.values{val(1)}. If item is a cfg_repeat and val is a  
        2-vector, then the min(val(2),numel(item.val)+1)-th value will be set  
        (i.e. a repeat added or replaced). If val is an empty cell, the value of  
        item will be cleared.  
        sts returns the status of all_set_item after the value has been  
        set. This can be used to check whether the item has been successfully  
        set.  
        Once editing of a module has finished, the module needs to be harvested  
        in order to update dependencies from and to other modules.  
         
         cfg_util('setdef', mod_cfg_id, item_mod_id, val)  
          
        Like cfg_util('setval',...) but set items in the defaults tree. This is  
        only supported for cfg_leaf items, not for cfg_choice, cfg_repeat,  
        cfg_branch items.  
        Defaults only apply to new jobs, not to already configured ones.  
         
         doc = cfg_util('showdoc', tagstr|cfg_id|(job_id, mod_job_id[, item_mod_id]))  
         
        Return help text for specified item. Item can be either a tag string or  
        a cfg_id in the default configuration tree, or a combination of job_id,  
        mod_job_id and item_mod_id from the current job.  
        The text returned will be a cell array of strings, each string  
        containing one paragraph of the help text. In addition to the help  
        text, hints about valid values, defaults etc. are displayed.  
         
         doc = cfg_util('showdocwidth', handle|width, tagstr|cfg_id|(job_id, mod_job_id[, item_mod_id]))  
         
        Same as cfg_util('showdoc', but use handle or width to determine the  
        width of the returned strings.  
         
         [mod_job_idlist, str, sts, dep, sout] = cfg_util('showjob', job_id[, mod_job_idlist])  
         
        Return information about the current job (or the part referenced by the  
        input cell array mod_job_idlist). Output arguments  
        * mod_job_idlist - cell list of module ids (same as input, if provided)  
        * str            - cell string of names of modules   
        * sts            - array of all set status of modules  
        * dep            - array of dependency status of modules  
        * sout           - array of output description structures   
        Each module configuration may provide a callback function 'vout' that  
        returns a struct describing module output variables. See 'cfg_exbranch'  
        for details about this callback, output description and output structure.  
        The module needs to be harvested before to make output_struct available.  
        This information can be used by the calling application to construct a  
        dependency object which can be passed as input to other modules. See  
        'cfg_dep' for details about dependency objects.  
         
         [mod_cfg_id, item_mod_id] = cfg_util('tag2cfg_id', tagstr)  
         
        Return a mod_cfg_id for the cfg_exbranch item that is the parent to the  
        item in the configuration tree whose parents have tag names as in the  
        dot-delimited tag string. item_mod_id is relative to the cfg_exbranch  
        parent. If tag string matches a node above cfg_exbranch level, then  
        item_mod_id will be invalid and mod_cfg_id will point to the specified  
        node.  
        Use cfg_util('ismod_cfg_id') and cfg_util('isitem_mod_id') to determine  
        whether returned ids are valid or not.  
        Tag strings should begin at the root level of an application configuration,   
        not at the matlabbatch root level.  
         
         mod_cfg_id = cfg_util('tag2mod_cfg_id', tagstr)  
         
        Same as cfg_util('tag2cfg_id', tagstr), but it only returns a proper  
        mod_cfg_id. If none of the tags in tagstr point to a cfg_exbranch, then  
        mod_cfg_id will be invalid.  
         
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_util.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_util", *args, **kwargs)
