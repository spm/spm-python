from spm.__wrapper__ import Runtime


def spm_mb_shape(*args, **kwargs):
    """
      Shape model  
         
        FORMAT psi0      = spm_mb_shape('affine',d,Mat)  
        FORMAT B         = spm_mb_shape('affine_bases',code)  
        FORMAT psi       = spm_mb_shape('compose',psi1,psi0)  
        FORMAT id        = spm_mb_shape('identity',d)  
        FORMAT dat       = spm_mb_shape('init_def',dat,sett)  
        FORMAT l         = spm_mb_shape('LSE0',mu,ax)  
        FORMAT a1        = spm_mb_shape('pull1',a0,psi,r)  
        FORMAT [f1,w1]   = spm_mb_shape('push1',f,psi,d,r)  
        FORMAT sd        = spm_mb_shape('samp_dens',Mmu,Mn)  
        FORMAT varargout = spm_mb_shape('shoot',v0,kernel,args)  
        FORMAT mu1       = spm_mb_shape('shrink_template',mu,oMmu,sett)  
        FORMAT P         = spm_mb_shape('softmax0',mu,ax)  
        FORMAT E         = spm_mb_shape('template_energy',mu,sett, sampd)  
        FORMAT dat       = spm_mb_shape('update_affines',dat,mu,sett)  
        FORMAT [mu,dat]  = spm_mb_shape('update_mean',dat, mu, sett, sampd)  
        FORMAT dat       = spm_mb_shape('update_simple_affines',dat,mu,sett)  
        FORMAT dat       = spm_mb_shape('update_velocities',dat,mu,sett)  
        FORMAT dat       = spm_mb_shape('update_warps',dat,sett)  
        FORMAT [mu,te]   = spm_mb_shape('zoom_mean',mu,sett,oMmu)  
        FORMAT dat       = spm_mb_shape('zoom_defs',dat,sett,oMmu,d0)  
        FORMAT sz        = spm_mb_shape('zoom_settings', v_settings, mu, n)  
        FORMAT psi       = spm_mb_shape('get_def',dat,sett.ms.Mmu)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_shape.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mb_shape", *args, **kwargs)
