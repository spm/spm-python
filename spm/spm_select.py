from spm.__wrapper__ import Runtime


def spm_select(*args, **kwargs):
    """
      File selector  
        FORMAT [t,sts] = spm_select(n,typ,mesg,sel,wd,filt,frames)  
        n      - number of files [Default: Inf]  
                 A single value or a range.  e.g.  
                 1       - select one file  
                 Inf     - select any number of files  
                 [1 Inf] - select 1 to Inf files  
                 [0 1]   - select 0 or 1 files  
                 [10 12] - select from 10 to 12 files  
        typ    - file type [Default: 'any']  
                 'any'   - all files  
                 'image' - Image files (".img" and ".nii")  
                           Note that it gives the option to select individuals  
                           volumes of the images.  
                 'mesh'  - Surface mesh files (".gii")  
                 'xml'   - XML files  
                 'mat'   - MATLAB .mat files or .txt files (assumed to contain  
                           ASCII representation of a 2D-numeric array)  
                 'batch' - SPM batch files (.m or .mat)  
                 'dir'   - select a directory  
                 Other strings act as a filter to regexp. This means that  
                 e.g. DCM*.mat files should have a typ of '^DCM.*\.mat$'  
        mesg   - a prompt [Default: 'Select files...']  
        sel    - list of already selected files [Default: {}]  
        wd     - directory to start off in [Default: pwd]  
        filt   - value for user-editable filter [Default: '.*']  
        frames - image frame numbers to include [Default: '1']  
         
        t      - selected files  
        sts    - status (1 means OK, 0 means window quit)  
         
        FORMAT [files,dirs] = spm_select('List',direc,filt)  
        Return files matching the filter 'filt' and directories within 'direc'  
        direc  - directory to search [Default: pwd]  
        filt   - filter to select files with regexp, e.g. '^w.*\.img$' [Default: '.*']  
         
        files  - files matching 'filt' in directory 'direc'  
        dirs   - subdirectories of 'direc'  
         
        FORMAT [files,dirs] = spm_select('ExtList',direc,filt,frames)  
        As above, but for selecting frames of 4D NIfTI files  
        frames - vector of frames to select (defaults to Inf, if not specified).  
                 If the frame number is Inf, all frames for the matching images  
                 are listed.   
         
        FORMAT [files,dirs] = spm_select('FPList',direc,filt)  
        FORMAT [files,dirs] = spm_select('ExtFPList',direc,filt,frames)  
        As above, but return files with full paths (i.e. prefixes 'direc' to each)  
         
        FORMAT [files,dirs] = spm_select('FPListRec',direc,filt)  
        FORMAT [files,dirs] = spm_select('ExtFPListRec',direc,filt,frames)  
        As above, but return files with full paths (i.e. prefixes 'direc' to each)  
        and search through sub directories recursively.  
         
        FORMAT [dirs] = spm_select('List',direc,'dir',filt)  
        FORMAT [dirs] = spm_select('FPList',direc,'dir',filt)  
        FORMAT [dirs] = spm_select('FPListRec',direc,'dir',filt)  
        Return directory names matching filter 'filt' within 'direc'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_select.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_select", *args, **kwargs)
