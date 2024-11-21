from spm.__wrapper__ import Runtime


def _copy_ctf_files(*args, **kwargs):
    """
      COPY_CTF_FILES copies a CTF dataset with all files and directories to a new CTF  
        dataset with another name.  
         
        Use as  
          copy_brainvision_files(oldname, newname, deleteflag)  
         
        Both the old and new name should refer to the CTF dataset directory, including  
        the .ds extension.  
         
        The third "deleteflag" argument is optional, it should be a boolean  
        that specifies whether the original files should be deleted after  
        copying or not (default = false).  
         
        See also COPY_BRAINVISION_FILES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/copy_ctf_files.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("copy_ctf_files", *args, **kwargs, nargout=0)
