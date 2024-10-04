from spm.__wrap__ import _Runtime


def mne_read_stc_file1(*args, **kwargs):
  """   
    [stc] = mne_read_stc_file1(filename)  
      
    Reads an stc file. The returned structure has the following fields  
     
        tmin           The first time point of the data in seconds  
        tstep          Time between frames in seconds  
        vertices       vertex indices (1 based)  
        data           The data matrix (nvert * ntime)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_read_stc_file1.m)
  """

  return _Runtime.call("mne_read_stc_file1", *args, **kwargs)
