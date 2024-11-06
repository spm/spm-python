from spm.__wrapper__ import Runtime


def _read_ctf_meg4(*args, **kwargs):
    """
      READ_CTF_MEG4 reads specified samples from a CTF continuous datafile  
        It neglects all trial boundaries as if the data was acquired in  
        non-continuous mode.  
         
        Use as  
          [meg] = read_ctf_meg4(filename, hdr, begsample, endsample, chanindx)  
        where  
          filename    name of the datafile, including the .meg4 extension  
          header      with all data information (from read_ctf_meg4)  
          begsample   index of the first sample to read  
          endsample   index of the last sample to read  
          chanindx    index of channels to read (optional, default is all)  
         
        See also READ_CTF_MEG4  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_meg4.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_meg4", *args, **kwargs)
