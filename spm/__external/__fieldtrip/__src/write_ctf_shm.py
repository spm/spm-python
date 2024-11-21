from spm.__wrapper__ import Runtime


def write_ctf_shm(*args, **kwargs):
    """
      WRITE_CTF_SHM writes metainformation and data as a packet to shared memory.  
        This function can be used for real-time processing of data while it is  
        being acquired.  
         
        Use as  
          write_ctf_shm(msgType, msgId, sampleNumber, numSamples, numChannels, data);  
         
        See also READ_CTF_SHM  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/write_ctf_shm.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("write_ctf_shm", *args, **kwargs)
