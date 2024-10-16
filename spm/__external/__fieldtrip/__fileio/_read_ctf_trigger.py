from spm.__wrapper__ import Runtime


def _read_ctf_trigger(*args, **kwargs):
  """  READ_CTF_TRIGGER reads the STIM channel from a dataset and detects  
    the trigger moments and values  
     
    [backpanel, frontpanel] = read_ctf_trigger(dataset)  
      
    This returns all samples of the STIM channel, converted to backpanel  
    and frontpanel trigger values. Triggers are placed at the rising flank  
    of the STIM channel.  
     
    Triggers should be at least 9 samples long (for 1200Hz samplerate) and  
    should not overlap each other.  
     
    See also READ_CTF_MEG4, READ_CTF_RES4  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_trigger.m)
  """

  return Runtime.call("read_ctf_trigger", *args, **kwargs)
