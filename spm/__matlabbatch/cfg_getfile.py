from spm.__wrapper__ import Runtime


def cfg_getfile(*args, **kwargs):
    """
      File selector  
        FORMAT [t,sts] = cfg_getfile(n,typ,mesg,sel,wd,filt,prms)  
            n    - Number of files  
                   A single value or a range.  e.g.  
                   1       - Select one file  
                   Inf     - Select any number of files  
                   [1 Inf] - Select 1 to Inf files  
                   [0 1]   - select 0 or 1 files  
                   [10 12] - select from 10 to 12 files  
            typ  - file type  
                   'any'   - all files  
                   'batch' - matlabbatch batch files (.m, .mat and XML)  
                   'dir'   - select a directory. By default, hidden ('.xyz') and  
                             MATLAB class directories are not shown.  
                   'mat'   - MATLAB .mat files or .txt files (assumed to contain  
                             ASCII representation of a 2D-numeric array)  
                   'xml'   - XML files  
                   Other strings act as a filter to regexp.  This means  
                   that e.g. DCM*.mat files should have a typ of '^DCM.*\.mat$'.  
                   A combination of types can be specified as a cellstr list of  
                   types. A file must match at least one of the specified types.  
            mesg - a prompt (default 'Select files...')  
            sel  - list of already selected files  
            wd   - Directory to start off in  
            filt - value for user-editable filter (default '.*'). Can be a  
                   string or cellstr. If it is a cellstr, filter expressions  
                   will be concatenated by '|' (regexp OR operator).  
            prms - Type specific parameters  
         
            t    - selected files  
            sts  - status (1 means OK, 0 means window quit)  
         
        FORMAT [t,ind] = cfg_getfile('Filter',files,typ,filt,prms,...)  
        filter the list of files (column cell array) in the same way as the  
        GUI would do. The 'prms...' argument(s) will be passed to a typ  
        specific filtering function, if available.  
        When filtering directory names, the filt argument will be applied to the  
        last directory in a path only.  
        t returns the filtered list (cell array), ind an index array, such that   
        t = files(ind).  
         
        FORMAT cpath = cfg_getfile('CPath',path,cwd)  
        function to canonicalise paths: Prepends cwd to relative paths, processes  
        '..' & '.' directories embedded in path.  
        path     - cellstr containing path names  
        cwd      - cellstr containing current working directory [default '.']  
        cpath    - conditioned paths, in same format as input path argument  
         
        FORMAT [files,dirs]=cfg_getfile('List'[,direc[,typ[,filt[,prms]]]])  
        Returns files matching the filter (filt) and directories within direc  
        direc    - directory to search. Defaults to pwd.  
        typ      - file type  
        filt     - additional filter to select files with (see regexp)  
                   e.g. '^w.*\.img$'   
        files    - files matching 'typ' and 'filt' in directory 'direc'  
        dirs     - subdirectories of 'direc'  
        FORMAT [files,dirs]=cfg_getfile('FPList'[,direc[,typ[,filt[,prms]]]])  
        As above, but returns files with full paths (i.e. prefixes direc to  
        each).  
        FORMAT [files,dirs]=cfg_getfile('FPListRec'[,direc[,typ[,filt[,prms]]]])  
        As above, but returns files with full paths (i.e. prefixes direc to  
        each) and searches through sub directories recursively.  
         
        FORMAT cfg_getfile('PrevDirs',dir)  
        Add directory dir to list of previous directories.  
        FORMAT dirs=cfg_getfile('prevdirs')  
        Retrieve list of previous directories.  
         
        FORMAT cfg_getfile('DirFilters', filter_list)  
        Specify a list of regular expressions to filter directory names. To show  
        all directories, use {'.*'}. Default is {'^[^.@]'}, i.e. directory names  
        starting with '.' or '@' will not be shown.  
         
        FORMAT cfg_getfile('ListDrives'[, reread])  
        On PCWIN(64) machines, list all available drive letters. If reread is  
        true, refresh internally cached list of drive letters.  
         
        This code is based on the file selection dialog in SPM5, with virtual  
        file handling turned off.  
       ____________________________________________________________________________  
        Copyright (C) 2005 Wellcome Department of Imaging Neuroscience  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_getfile.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_getfile", *args, **kwargs)
