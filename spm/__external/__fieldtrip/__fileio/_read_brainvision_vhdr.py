from spm.__wrap__ import _Runtime


def _read_brainvision_vhdr(*args, **kwargs):
  """  READ_BRAINVISION_VHDR reads the known items from the BrainVision EEG  
    header file and returns them in a structure.  
     
    Use as  
      vhdr = read_brainvision_vhdr(filename)  
     
    See also READ_BRAINVISION_EEG, READ_BRAINVISION_VMRK  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_brainvision_vhdr.m)
  """

  return _Runtime.call("read_brainvision_vhdr", *args, **kwargs)
