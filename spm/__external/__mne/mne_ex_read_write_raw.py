from spm.__wrapper__ import Runtime


def mne_ex_read_write_raw(*args, **kwargs):
  """   
    function mne_ex_read_write_raw(infile,outfile);  
     
    Read and write raw data in 60-sec blocks  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/mne/mne_ex_read_write_raw.m)
  """

  return Runtime.call("mne_ex_read_write_raw", *args, **kwargs, nargout=0)
