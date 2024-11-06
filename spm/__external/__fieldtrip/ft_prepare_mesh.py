from spm.__wrapper__ import Runtime


def ft_prepare_mesh(*args, **kwargs):
    """
      FT_PREPARE_MESH creates a triangulated surface mesh or tetrahedral/hexahedral  
        volume mesh that can be used as geometrical description for a volume conduction  
        model. The mesh can either be created manually from anatomical MRI data or can be  
        generated starting from a segmented MRI. This function can also be used to create a  
        cortex hull, i.e. the smoothed envelope around the pial surface created by  
        freesurfer.  
         
        Use as  
          mesh = ft_prepare_mesh(cfg)  
          mesh = ft_prepare_mesh(cfg, mri)  
          mesh = ft_prepare_mesh(cfg, seg)  
        where the mri input argument is the result from FT_READ_MRI, FT_VOLUMEREALIGN or  
        FT_VOLUMERESLICE and the seg input argument is from FT_VOLUMESEGMENT. If you  
        specify an anatomical MRI, it will be segmented on the fly.  
         
        The cfg argument is a structure that can contain:  
          cfg.method      = string, can be 'interactive', 'projectmesh', 'iso2mesh', 'isosurface',  
                            'headshape', 'hexahedral', 'tetrahedral', 'cortexhull' or 'fittemplate'  
          cfg.tissue      = cell-array with strings representing the tissue types, or numeric vector with integer values  
          cfg.numvertices = numeric vector, should have same number of elements as the number of tissues  
         
        When providing an anatomical MRI or a segmentation, you should specify  
          cfg.downsample  = integer number (default = 1, i.e. no downsampling), see FT_VOLUMEDOWNSAMPLE  
          cfg.spmversion  = string, 'spm2', 'spm8', 'spm12' (default = 'spm12')  
         
        For method 'headshape' you should specify  
          cfg.headshape   = a filename containing headshape, a Nx3 matrix with surface  
                            points, or a structure with a single or multiple boundaries  
         
        For method 'cortexhull' you should not give input data, but specify  
          cfg.headshape   = string, filename containing the pial surface computed by freesurfer recon-all  
         
        For method 'fittemplate' you should specify  
          cfg.headshape   = a filename containing headshape  
          cfg.template    = a filename containing headshape  
        With this method you are fitting the headshape from the configuration to the template;  
        the resulting affine transformation is applied to the input mesh (or set of meshes),  
        which is subsequently returned as output variable.  
         
        To facilitate data-handling and distributed computing you can use  
          cfg.inputfile   =  ...  
          cfg.outputfile  =  ...  
        If you specify one of these (or both) the input data will be read from a *.mat  
        file on disk and/or the output data will be written to a *.mat file. These mat  
        files should contain only a single variable, corresponding with the  
        input/output structure.  
         
        Example  
          mri             = ft_read_mri('Subject01.mri');  
         
          cfg             = [];  
          cfg.output      = {'scalp', 'skull', 'brain'};  
          segmentation    = ft_volumesegment(cfg, mri);  
         
          cfg             = [];  
          cfg.tissue      = {'scalp', 'skull', 'brain'};  
          cfg.numvertices = [800, 1600, 2400];  
          mesh            = ft_prepare_mesh(cfg, segmentation);  
         
          cfg             = [];  
          cfg.method      = 'cortexhull';  
          cfg.headshape   = '/path/to/surf/lh.pial';  
          cfg.fshome      = '/path/to/freesurfer dir';  
          cortex_hull     = ft_prepare_mesh(cfg);  
         
        See also FT_VOLUMESEGMENT, FT_PREPARE_HEADMODEL, FT_PLOT_MESH  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_prepare_mesh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_prepare_mesh", *args, **kwargs)
