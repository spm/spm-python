from spm.__wrap__ import _Runtime


def _read_ctf_shm(*args, **kwargs):
  """  READ_CTF_SHM reads metainformation or selected blocks of data from  
    shared memory. This function can be used for real-time processing of  
    data while it is being acquired.  
     
    Use as  
      [msgType msgId sampleNumber numSamples numChannels] = read_ctf_shm;  
    or  
      [data] = read_ctf_shm(msgNumber);  
      [data] = read_ctf_shm(msgNumber, numValues);  
     
    See also WRITE_CTF_SHM  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_shm.m)
  """

  return _Runtime.call("read_ctf_shm", *args, **kwargs)
