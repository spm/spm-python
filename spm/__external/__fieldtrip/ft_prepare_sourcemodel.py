from spm.__wrapper__ import Runtime


def ft_prepare_sourcemodel(*args, **kwargs):
    """
      FT_PREPARE_SOURCEMODEL constructs a source model, for example a 3D grid or a  
        cortical sheet. The source model that can be used for source reconstruction,  
        beamformer scanning, linear estimation and MEG interpolation.  
         
        Use as  
          sourcemodel = ft_prepare_sourcemodel(cfg)  
        where the details of the configuration structure determine how the source  
        model will be constructed.  
         
        The different approaches for constructing a source model are  
          cfg.method = 'basedongrid'        regular 3D grid with explicit specification  
                       'basedonresolution'  regular 3D grid with specification of the resolution  
                       'basedonpos'         place dipoles at the predefined positions  
                       'basedonmri'         regular 3D grid, based on segmented MRI, restricted to gray matter  
                       'basedonmni'         regular 3D grid, based on a warped template grid, based on the MNI brain  
                       'basedoncortex'      cortical sheet from external software such as Caret or FreeSurfer, can also be two separate hemispheres  
                       'basedonshape'       surface mesh based on inward shifted head surface from an external file  
                       'basedonvol'         surface mesh based on inward shifted brain surface from volume conductor  
                       'basedonfile'        the sourcemodel should be read from file  
                       'basedoncentroids'   irregular 3D grid based on volumetric mesh  
        The default method is determined automatically based on the configuration options  
        that you specify.  
         
        BASEDONGRID - uses an explicitly specified grid, according to the following  
        configuration options:  
          cfg.xgrid         = vector (e.g. -20:1:20) or 'auto' (default = 'auto')  
          cfg.ygrid         = vector (e.g. -20:1:20) or 'auto' (default = 'auto')  
          cfg.zgrid         = vector (e.g.   0:1:20) or 'auto' (default = 'auto')  
         
        BASEDONRESOLUTION - uses an grid with the desired resolution, according  
        to the following configuration options:  
          cfg.resolution    = number (e.g. 1 cm) for automatic grid generation  
         
        BASEDONPOS - places sources on positions that you explicitly specify, according to  
        the following configuration options:  
          cfg.sourcemodel.pos       = N*3 matrix with position of each source  
          cfg.sourcemodel.inside    = N*1 vector with boolean value whether position is inside brain (optional)  
          cfg.sourcemodel.dim       = [Nx Ny Nz] vector with dimensions in case of 3D grid (optional)  
        The following fields (from FT_PRERARE_LEADFIELD or FT_SOURCEANALYSIS) are  
        not used in this function, but will be copied along to the output:  
          cfg.sourcemodel.leadfield = cell-array  
          cfg.sourcemodel.filter    = cell-array  
          cfg.sourcemodel.subspace  
          cfg.sourcemodel.lbex  
         
        BASEDONMNI - uses source positions from a template sourcemodel that is inversely  
        warped from MNI coordinates to the individual subjects MRI. It uses the following  
        configuration options:  
          cfg.mri             = structure with the anatomical MRI, or the filename of the MRI, see FT_READ_MRI  
          cfg.nonlinear       = 'no' (or 'yes'), use non-linear normalization  
          cfg.resolution      = number (e.g. 6) of the resolution of the template MNI grid, defined in mm  
          cfg.template        = structure with the template sourcemodel, or the filename of a template sourcemodel (defined in MNI space)  
          cfg.templatemri     = string, filename of the MNI template (default = 'T1.mnc' for SPM2 or 'T1.nii' for SPM8 and SPM12)  
          cfg.spmversion      = string, 'spm2', 'spm8', 'spm12' (default = 'spm12')  
          cfg.spmmethod       = string, 'old', 'new' or 'mars', see FT_VOLUMENORMALISE  
          cfg.nonlinear       = string, 'yes' or 'no', see FT_VOLUMENORMALISE  
        Either cfg.resolution or cfg.template needs to be defined; if both are defined, cfg.template prevails.  
         
        BASEDONMRI - makes a segmentation of the individual anatomical MRI and places  
        sources in the grey matter. It uses the following configuration options:  
          cfg.mri             = can be filename, MRI structure or segmented MRI structure  
          cfg.threshold       = 0.1, relative to the maximum value in the segmentation  
          cfg.smooth          = 5, smoothing in voxels  
         
        BASEDONCORTEX - places sources on the vertices of a cortical surface description  
          cfg.headshape       = string, should be a *.fif file  
         
        BASEDONCENTROIDS - places sources on the centroids of a volumetric mesh  
          cfg.headmodel       = tetrahedral or hexahedral mesh  
          cfg.headmodel.type  = 'simbio';  
         
        Other configuration options include  
          cfg.unit            = string, can be 'mm', 'cm', 'm' (default is automatic)  
          cfg.tight           = 'yes' or 'no' (default is automatic)  
          cfg.inwardshift     = number, amount to shift the innermost surface of the headmodel inward when determining  
                                whether sources are inside or outside the source compartment (default = 0)  
          cfg.moveinward      = number, amount to move sources inward to ensure a certain minimal distance to the innermost  
                                surface of the headmodel (default = 0)  
          cfg.movetocentroids = 'yes' or 'no', move the dipoles to the centroids of the hexahedral  
                                or tetrahedral mesh (default = 'no')  
          cfg.spherify        = 'yes' or 'no', scale the source model so that it fits inside a sperical  
                                volume conduction model (default = 'no')  
          cfg.symmetry        = 'x', 'y' or 'z' symmetry for two dipoles, can be empty (default = [])  
          cfg.headshape       = a filename for the headshape, a structure containing a single surface,  
                                or a Nx3 matrix with headshape surface points (default = [])  
          cfg.spmversion      = string, 'spm2', 'spm8', 'spm12' (default = 'spm12')  
         
        The EEG or MEG sensor positions can be present in the data or can be specified as  
          cfg.elec          = structure with electrode positions or filename, see FT_READ_SENS  
          cfg.grad          = structure with gradiometer definition or filename, see FT_READ_SENS  
         
        The headmodel or volume conduction model can be specified as  
          cfg.headmodel     = structure with volume conduction model or filename, see FT_PREPARE_HEADMODEL  
         
        The cfg.inwardshift option can be used for 3D grids to specify a positive (inward)  
        or negative (outward) number to shift the innermost surface of the headmodel  
        (usually the skull) when determining whether sources are to be flagged as inside or  
        outside the source compartment. Only sources flagged as inside will be considered  
        for subsequent source reconstructions. An ourward shift can be useful for a  
        spherical or singleshell MEG headmodel. For a source model based on a cortical  
        sheet in general you want all sources to be considered inside. For a BEM headmodel  
        (EEG or MEG), there should never be any sources outside the actual source  
        compartment.  
         
        The cfg.moveinward option can be used for a source model based on a cortical sheet  
        to push the sources inward a little bit to ensure sufficient distance to the  
        innermost surface of a BEM headmodel (EEG or MEG).  
         
        See also FT_PREPARE_LEADFIELD, FT_PREPARE_HEADMODEL, FT_SOURCEANALYSIS,  
        FT_DIPOLEFITTING, FT_MEGREALIGN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/ft_prepare_sourcemodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_prepare_sourcemodel", *args, **kwargs)
