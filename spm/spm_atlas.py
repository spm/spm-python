from spm._runtime import Runtime


def spm_atlas(*args, **kwargs):
    r"""
      Atlas multi-function  
        FORMAT xA = spm_atlas('load',atlas)  
        FORMAT L = spm_atlas('list')  
        FORMAT [S,sts] = spm_atlas('select',xA,label)  
        FORMAT Q = spm_atlas('query',xA,XYZmm)  
        FORMAT [Q,P] = spm_atlas('query',xA,xY)  
        FORMAT VM = spm_atlas('mask',xA,label,opt)  
        FORMAT V = spm_atlas('prob',xA,label)  
        FORMAT V = spm_atlas('maxprob',xA,thresh)  
        FORMAT D = spm_atlas('dir')  
         
        FORMAT url = spm_atlas('weblink',XYZmm,website)  
        FORMAT labels = spm_atlas('import_labels',labelfile,fmt)  
        FORMAT spm_atlas('save_labels',labelfile,labels)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_atlas.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_atlas", *args, **kwargs)
