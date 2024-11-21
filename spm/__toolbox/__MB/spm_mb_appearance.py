from spm.__wrapper__ import Runtime


def spm_mb_appearance(*args, **kwargs):
    """
       
        FORMAT chan       = spm_mb_appearance('inu_basis',T,df,Mat,reg,samp)  
        FORMAT [inu,ll]   = spm_mb_appearance('inu_field',T,chan,d,varargin)  
        FORMAT z          = spm_mb_appearance('responsibility',m,b,W,n,f,mu,msk_chn)  
        FORMAT dat        = spm_mb_appearance('restart',dat,sett)  
        FORMAT [z,dat]    = spm_mb_appearance('update',dat,mu,sett)  
        FORMAT dat        = spm_mb_appearance('update_prior',dat,sett)  
        FORMAT            = spm_mb_appearance('debug_show',img,img_is,modality,fig_title,do)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_appearance.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mb_appearance", *args, **kwargs)
