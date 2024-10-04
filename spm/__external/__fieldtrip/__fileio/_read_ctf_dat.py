from spm.__wrap__ import _Runtime


def _read_ctf_dat(*args, **kwargs):
  """  READ_CTF_DAT reads MEG data from an ascii format CTF file  
     
    meg = read_ctf_dat(filename)  
      
    returns a structure with the following fields:  
      meg.data        Nchans x Ntime  
      meg.time        1xNtime in miliseconds  
      meg.trigger     1xNtime with trigger values  
      meg.label       1xNchans cell-array with channel labels (string)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_dat.m)
  """

  return _Runtime.call("read_ctf_dat", *args, **kwargs)
