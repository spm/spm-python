from spm.__wrapper__ import Runtime


def spm_mb_io(*args, **kwargs):
    """
      File I/O Multi-Brain functionalities  
         
        FORMAT fn      = spm_mb_io('get_image',datn)  
        FORMAT [out,M] = spm_mb_io('get_data',in)  
        FORMAT [d,M]   = spm_mb_io('get_size',fin)  
        FORMAT           spm_mb_io('save_template',mu,sett)  
        FORMAT fout    = spm_mb_io('set_data',fin,f)  
        FORMAT dat     = spm_mb_io('save_mat',dat,mat);  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_io.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mb_io", *args, **kwargs)
