from spm.__wrapper__ import Runtime


def cfg_serial(*args, **kwargs):
    """
      This function is deprecated.  
        The functionality should replaced by the following sequence of calls:  
         
        Instead of  
        cfg_serial(guifcn, job, varargin)  
        use  
        cjob = cfg_util('initjob', job);  
        sts  = cfg_util('filljobui', cjob, guifcn, varargin);  
        if sts  
             cfg_util('run', cjob);  
        end;  
        cfg_util('deljob', cjob);  
         
        Instead of  
        cfg_serial(guifcn, tagstr, varargin)  
        use  
        cjob = cfg_util('initjob');  
        mod_cfg_id = cfg_util('tag2cfg_id', tagstr);  
        cfg_util('addtojob', cjob, mod_cfg_id);  
        sts  = cfg_util('filljobui', cjob, guifcn, varargin);  
        if sts  
             cfg_util('run', cjob);  
        end;  
        cfg_util('deljob', cjob);  
         
        Instead of  
        cfg_serial(guifcn, mod_cfg_id, varargin)  
        use  
        cjob = cfg_util('initjob');  
        cfg_util('addtojob', cjob, mod_cfg_id);  
        sts  = cfg_util('filljobui', cjob, guifcn, varargin);  
        if sts  
             cfg_util('run', cjob);  
        end;  
        cfg_util('deljob', cjob);  
         
        If no guifcn is specified, use cfg_util('filljob',... instead.  
         
        GuiFcn semantics  
        [val sts] = guifcn(item)  
        val should be suitable to set item.val{1} using setval(item, val,  
        false) for all cfg_leaf items. For cfg_repeat/cfg_choice items, val  
        should be a cell array of indices into item.values. For each element of  
        val, setval(item, [val{k} Inf], false)  
        will be called and thus item.values{k} will be appended to item.val.  
        sts should be set to true, if guifcn returns with success (i.e. a  
        valid value is returned or input should continue for the next item,  
        regardless of value validity).  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_serial.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_serial", *args, **kwargs, nargout=0)
