from spm._runtime import Runtime


def _volumewrite_spm(*args, **kwargs):
    r"""
      VOLUMEWRITE_SPM writes anatomical or functional MRI volume data to analyze or nifti format  
        using the SPM toolbox.  
         
        Use as  
          [Va] = volumewrite_spm(filename, data, transform)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/private/volumewrite_spm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumewrite_spm", *args, **kwargs)
