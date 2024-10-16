from spm.__wrapper__ import Runtime


def _volumewrite_spm(*args, **kwargs):
  """  VOLUMEWRITE_SPM writes anatomical or functional MRI volume data to analyze or nifti format  
    using the SPM toolbox.  
     
    Use as  
      [Va] = volumewrite_spm(filename, data, transform)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/volumewrite_spm.m)
  """

  return Runtime.call("volumewrite_spm", *args, **kwargs)
