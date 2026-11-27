from spm._runtime import Runtime


def spm_file_ext(*args, **kwargs):
    r"""
      Return or set file extension for SPM images  
        FORMAT ext = spm_file_ext  
        ext   - file extension (e.g. '.img' or '.nii' for NIfTI images)  
         
        FORMAT spm_file_ext(ext)  
        ext   - file extension (e.g. '.img' or '.nii' for NIfTI images)  
       __________________________________________________________________________  
         
        The file extension returned by this function is defined in spm_defaults.m  
        in field 'defaults.images.format'.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_file_ext.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_file_ext", *args, **kwargs)
