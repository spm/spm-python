from spm.__wrapper__ import Runtime


def _warp_fsaverage_sym(*args, **kwargs):
    """
      WARP_FSAVERAGE_SYM maps left or right hemisphere electrodes onto   
        FreeSurfer's fsaverage_sym's left hemisphere. To perform this mapping,   
        you first need to have processed the subject's MRI with FreeSurfer's   
        recon-all functionality and additionaly have registered the subject's resulting   
        surfaces to freesurfer fsaverage_sym template using surfreg as described   
        in section 1.2 of https://surfer.nmr.mgh.harvard.edu/fswiki/Xhemi  
         
        The configuration must contain the following options  
          cfg.headshape      = string, filename containing subject headshape  
                             (e.g. <path to freesurfer/surf/lh.pial>)  
          cfg.fshome         = string, path to freesurfer  
         
        See also FT_ELECTRODEREALIGN, WARP_FSAVERAGE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/warp_fsaverage_sym.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("warp_fsaverage_sym", *args, **kwargs)
