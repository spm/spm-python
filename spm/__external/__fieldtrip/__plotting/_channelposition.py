from spm.__wrap__ import _Runtime


def _channelposition(*args, **kwargs):
  """  CHANNELPOSITION computes the channel positions and orientations from the  
    MEG coils, EEG electrodes or NIRS optodes  
     
    Use as  
      [pos, ori, lab] = channelposition(sens)  
    where sens is an gradiometer, electrode, or optode array.  
     
    See also FT_DATATYPE_SENS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/channelposition.m)
  """

  return _Runtime.call("channelposition", *args, **kwargs)
