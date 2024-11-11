from spm.__wrapper__ import Runtime


def _copy_brainvision_files(*args, **kwargs):
    """
      COPY_BRAINVISION_FILES copies a BrainVision EEG dataset, which consists of a vhdr  
        header file, vmrk marker file and a data file with the extension dat, eeg or seg.  
         
        Use as  
          copy_brainvision_files(oldname, newname, deleteflag)  
         
        Both the old and the new filename should be strings corresponding to the header  
        file, i.e. including the vhdr extension.  
         
        The third "deleteflag" argument is optional, it should be a boolean  
        that specifies whether the original files should be deleted after  
        copying or not (default = false).  
         
        An earlier version of this function can be found on  
          - https://gist.github.com/robertoostenveld/e31637a777c514bf1e86272e1092316e  
          - https://gist.github.com/CPernet/e037df46e064ca83a49fb4c595d4566a  
         
        See also COPY_CTF_FILES  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/copy_brainvision_files.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("copy_brainvision_files", *args, **kwargs, nargout=0)
