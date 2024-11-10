from spm.__wrapper__ import Runtime


def spm_file(*args, **kwargs):
    """
      Character array (or cell array of strings) handling facility  
        FORMAT str = spm_file(str,option)  
        str        - character array, or cell array of strings  
        option     - string of requested item - one among:  
                     {'path', 'cpath', 'fpath', 'basename', 'ext', 'filename',  
                     'number', 'shortxx', 'unique'}  
         
        FORMAT str = spm_file(str,opt_key,opt_val,...)  
        str        - character array, or cell array of strings  
        opt_key    - string of targeted item - one among:  
                     {'path', 'basename', 'ext', 'filename', 'number', 'prefix',  
                     'suffix','link','local'}  
        opt_val    - string of new value for feature  
       __________________________________________________________________________  
         
        Definitions:  
         
        <cpath> = <fpath>filesep<filename>  
        <filename> = <basename>.<ext><number>  
        <path> = empty or full path or relative path  
         
        'shortxx' produces a string of at most xx characters long. If the input  
        string is longer than n, then it is prefixed with '..' and the last xx-2  
        characters are returned. If the input string is a path, the leading  
        directories are replaced by './'.  
         
        'unique' returns an unique filename by adding an incremental _%03d suffix.  
       __________________________________________________________________________  
         
        Examples:  
         
        spm_file('C:\data\myimage.nii', 'prefix','rp_', 'ext','.txt')  
        returns 'C:\data\rp_myimage.txt' on a Windows platform  
         
        spm_file({'/home/karl/software/spm.m'},'path','/home/karl/spm')  
        returns {'/home/karl/spm/spm.m'}  
         
        spm_file('/home/karl/software/spm/spm.m','filename')  
        returns 'spm.m', and  
        spm_file('/home/karl/software/spm/spm.m','basename')  
        returns 'spm'  
         
        spm_file('SPM.mat','fpath')  
        returns '/home/karl/data/stats' (i.e. pwd), while  
        spm_file('SPM.mat','path')  
        returns '', and  
        spm_file('SPM.mat','cpath')  
        returns '/home/karl/data/stats/SPM.mat'  
       __________________________________________________________________________  
         
        See also: spm_fileparts, spm_select, spm_file_ext, spm_existfile  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_file.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_file", *args, **kwargs)
