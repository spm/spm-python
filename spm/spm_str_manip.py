from spm.__wrapper__ import Runtime


def spm_str_manip(*args, **kwargs):
    """
      Miscellaneous string manipulation options  
        FORMAT string_out = spm_str_manip(string_in,options)  
        string_in    - input string, string matrix, or cell array of strings  
        options      - a string of options flags, see below  
         
        string_out   - output string, string matrix, or cell array of strings  
        R2           - extra output for 'c' and 'C' options  
       __________________________________________________________________________  
        Each of the options is performed from left to right.  
        The options are:  
          'r'              - remove trailing suffix  
          's'              - remove trailing suffix - only if it is either  
                             '.img', '.hdr', '.mat', '.nii' or '.gii'  
          'e'              - remove everything except the suffix  
          'h'              - remove trailing pathname component  
          'H'              - always remove trailing pathname component  
                             (returns '.' for straight filenames like 'test.img')  
                              (whereas 'h' option mimics csh & returns 'test.img' )  
          't'              - remove leading pathname component  
          ['f' num2str(n)] - remove all except first n characters  
          ['l' num2str(n)] - remove all except last n characters  
          ['k' num2str(n)] - produce a string of at most n characters long.  
                             If the input string is longer than n, then  
                             it is prefixed with '..' and the last n-2 characters  
                             are returned.  
          ['a' num2str(n)] - similar to above - except the leading directories  
                             are replaced by './'.  
                             eg. spm_str_manip('/dir1/dir2/file.img','a16') would  
                             produce '../dir2/file.img'.  
          'v'              - delete non valid filename characters  
                             Valid are '.a..zA..Z01..9_-: ' & filesep  
          'x'              - escape TeX special characters  
          'p'              - canonicalise pathname (see spm_select('CPath',...))  
          'c'              - remove leading components common to all strings  
                             returns leading component as a second output argument  
          'C'              - returns single string compressed version of a  
                             cellstr, such as '/data/pic{01,12,23}.img'.  
                             Second argument is a structure with fields:  
                               .s - start string (E.g. '/data/pic')  
                               .m - middle bits cellstr (E.g.{'01','02','03'})  
                               .e - end string (E.g. '.img')  
          'd'              - deblank - this is always done!  
       __________________________________________________________________________  
         
        This function is now deprecated, use spm_file when possible instead.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_str_manip.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_str_manip", *args, **kwargs)
