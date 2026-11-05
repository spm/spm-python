from spm._runtime import Runtime


def DEM_music_compression(*args, **kwargs):
    r"""
      Structure learning from sound files with active learning  
       __________________________________________________________________________  
         
        This routine illustrates the use of renormalizable generative models to  
        recognise, compress and generate sound files or auditory streams. This  
        application uses a blocking or grouping operator, which operates on the  
        neighbouring frequencies of a sonogram (i.e., time frequency  
        representation of a sound file). This means that local frequencies are  
        grouped together over time and assimilated using fast structure learning.  
         
        This particular demonstration ingests a sound file of music discretising  
        it into a few hundred time-frequency voxels, which are subsequently  
        re-normalised to a succession of (high-level) episodes corresponding  
        roughly to a bar of music. This demonstration includes active learning,  
        after structure learning to illustrate how transitions from the final  
        episode to a subsequent episode can be learnt in an experience -dependent  
        fashion.  
       __________________________________________________________________________  
        Copyright (C) 2019 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DEM/DEM_music_compression.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("DEM_music_compression", *args, **kwargs)
