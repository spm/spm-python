from spm.__wrapper__ import Runtime


def read_ctf_shm(*args, **kwargs):
    """
      READ_CTF_SHM reads metainformation or selected blocks of data from  
        shared memory. This function can be used for real-time processing of  
        data while it is being acquired.  
         
        Use as  
          [msgType msgId sampleNumber numSamples numChannels] = read_ctf_shm;  
        or  
          [data] = read_ctf_shm(msgNumber);  
          [data] = read_ctf_shm(msgNumber, numValues);  
         
        See also WRITE_CTF_SHM  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/read_ctf_shm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_shm", *args, **kwargs)
