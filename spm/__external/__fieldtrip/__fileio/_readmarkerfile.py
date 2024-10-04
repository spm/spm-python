from spm.__wrap__ import _Runtime


def _readmarkerfile(*args, **kwargs):
  """  Read the MarkerFile.mrk file in a CTF dataset.  
     
    Use as  
      marker = readmarkerfile(folder)  
     
    Creates a marker structure which contains number_markers,  
    number_samples, marker_names, and trial_times.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/readmarkerfile.m)
  """

  return _Runtime.call("readmarkerfile", *args, **kwargs)
