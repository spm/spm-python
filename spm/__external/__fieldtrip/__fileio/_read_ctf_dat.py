from spm.__wrapper__ import Runtime


def _read_ctf_dat(*args, **kwargs):
    """
      READ_CTF_DAT reads MEG data from an ascii format CTF file  
         
        meg = read_ctf_dat(filename)  
          
        returns a structure with the following fields:  
          meg.data        Nchans x Ntime  
          meg.time        1xNtime in miliseconds  
          meg.trigger     1xNtime with trigger values  
          meg.label       1xNchans cell-array with channel labels (string)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_ctf_dat.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_ctf_dat", *args, **kwargs)
