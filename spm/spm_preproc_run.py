from spm.__wrapper__ import Runtime


def spm_preproc_run(*args, **kwargs):
    """
      Segment a bunch of images  
        FORMAT spm_preproc_run(job)  
        job.channel(n).vols{m}  
        job.channel(n).biasreg  
        job.channel(n).biasfwhm  
        job.channel(n).write  
        job.tissue(k).tpm  
        job.tissue(k).ngaus  
        job.tissue(k).native  
        job.tissue(k).warped  
        job.warp.mrf  
        job.warp.cleanup  
        job.warp.affreg  
        job.warp.reg  
        job.warp.fwhm  
        job.warp.samp  
        job.warp.write  
        job.warp.bb  
        job.warp.vox  
        job.iterations  
        job.alpha  
         
        See the batch interface for a description of the fields.  
         
        See also spm_preproc8.m amd spm_preproc_write8.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_preproc_run.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_preproc_run", *args, **kwargs)
