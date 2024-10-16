from spm.__wrapper__ import Runtime


def read_eep_rej(*args, **kwargs):
  """  READ_EEP_REJ reads rejection marks from an EEProbe *.rej file  
     
    This function returns a Nx2 matrix with the begin and end latency  
    of N rejection marks. The latency is in miliseconds.  
     
    rej = read_eep_rej(filename)  
     
    An EEProbe rejection file is formatted like  
      0.0000-0.3640  
      2.4373-3.5471  
      ...   
    where rejection begin and end are given in seconds. This function   
    converts the latency in miliseconds.  
     
    Author: Robert Oostenveld, Aalborg University, Denmark, 11 March 2003  
     
    See also READ_EEP_CNT, READ_EEP_TRG, READ_EEP_AVR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/eeprobe/read_eep_rej.m)
  """

  return Runtime.call("read_eep_rej", *args, **kwargs)
