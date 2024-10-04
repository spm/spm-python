from spm.__wrap__ import _Runtime


def mne_ex_read_write_raw(*args, **kwargs):
  """   
    function mne_ex_read_write_raw(infile,outfile);  
     
    Read and write raw data in 60-sec blocks  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_ex_read_write_raw.m)
  """

  return _Runtime.call("mne_ex_read_write_raw", *args, **kwargs, nargout=0)
