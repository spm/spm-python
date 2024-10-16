from spm.__wrapper__ import Runtime


def _read_trk(*args, **kwargs):
  """ read TrackVis .trk format data  
    fillPath: filename of track to read.  
   for format details http://www.trackvis.org/docs/?subsect=fileformat  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_trk.m)
  """

  return Runtime.call("read_trk", *args, **kwargs)
