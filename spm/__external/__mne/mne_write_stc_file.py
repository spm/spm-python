from spm.__wrapper__ import Runtime


def mne_write_stc_file(*args, **kwargs):
  """   
    mne_write_stc_file(filename,stc)  
      
    writes an stc file  
     
        filename      output file  
        stc           a stucture containing the stc data with fields:  
     
        tmin          The time of the first frame in seconds  
        tstep         Time between frames in seconds  
        vertices      Vertex indices (0 based)  
        data          The data matrix nvert * ntime  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_write_stc_file.m)
  """

  return Runtime.call("mne_write_stc_file", *args, **kwargs, nargout=0)
