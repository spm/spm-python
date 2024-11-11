from spm.__wrapper__ import Runtime


def spm_file_ext(*args, **kwargs):
    """
      Return or set file extension for SPM images  
        FORMAT ext = spm_file_ext  
        ext   - file extension (e.g. '.img' or '.nii' for NIfTI images)  
         
        FORMAT spm_file_ext(ext)  
        ext   - file extension (e.g. '.img' or '.nii' for NIfTI images)  
       __________________________________________________________________________  
         
        The file extension returned by this function is defined in spm_defaults.m  
        in field 'defaults.images.format'.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_file_ext.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_file_ext", *args, **kwargs)
