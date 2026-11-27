from spm._runtime import Runtime


def read_ctf_shm(*args, **kwargs):
    r"""
      READ_CTF_SHM reads metainformation or selected blocks of data from  
        shared memory. This function can be used for real-time processing of  
        data while it is being acquired.  
         
        Use as  
          [msgType msgId sampleNumber numSamples numChannels] = read_ctf_shm  
        or  
          [data] = read_ctf_shm(msgNumber)  
          [data] = read_ctf_shm(msgNumber, numValues)  
         
        See also WRITE_CTF_SHM  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/src/read_ctf_shm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("read_ctf_shm", *args, **kwargs)
