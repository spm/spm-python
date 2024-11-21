from spm.__wrapper__ import Runtime, MatlabClassWrapper


class slover(MatlabClassWrapper):
    def __init__(self, *args, **kwargs):
        """
          class constructor for slice overlay (slover) object  
            FORMAT [o, others] = slover(params, others, varargin)  
             
            Inputs  
            params    - either:  
                        - action string implementing class methods (see below)  
                        - array of image names / vol structs to display  
                        - structure with some fields for object (see below)  
            others    - structure, containing extra fields for object (or children)  
            varargin  - maybe some other parameters for action calls (see below)  
             
            Outputs  
            o       - slover object  
            others  - any unrecognized fields from params, others  
             
            Object fields are:  
             - img - array of structs with information for images to display  
                   - img structs contain fields  
                        type - one of {'truecolour' 'split', 'contour'};  
                              truecolour - displays transparent (see prop) image  
                                 overlaid with any previous  
                              split - in defined area, replaces image present (SPM  
                                 type activation display)  
                              contour - contour map of image overlaid.  See help  
                                 for contours function in matlab  
                        vol - vol struct info (see spm_vol)  
                              can also be vol containing image as 3d matrix  
                              set with add_blobs method  
                        cmap - colormap for this image  
                        nancol - color for NaN. If scalar, this is an index into  
                               the image cmap.  If 1x3 vector, it's a colour  
                        prop - proportion of intensity for this cmap/img  
                        func - function to apply to image before scaling to cmap  
                               (and therefore before min/max thresholding. E.g. a func of  
                               'i1(i1==0)=NaN' would convert zeros to NaNs  
                        range - 2x1 vector of values for image to distribute colormap across  
                               the first row of the colormap applies to the first  
                               value in 'range', and the last value to the second  
                               value in 'range'  
                        outofrange - behavior for image values to the left and  
                               right of image limits in 'range'.  Left means  
                               colormap values < 1, i.e for image values <  
                               range(1), if (range(1)<range(2)), and image values >  
                               range(1) where (range(1)>range(2)). If missing,  
                               display min (for Left) and max (for Right) value from colormap.  
                               Otherwise should be a 2 element cell array, where  
                               the first element is the colour value for image values  
                               left of 'range', and the second is for image values  
                               right of 'range'.  Scalar values for  
                               colour index the colormap, 3x1 vectors are colour  
                               values.  An empty array attracts default settings  
                               appropriate to the mode - i.e. transparent colour (where  
                               img(n).type is truecolour), or split colour.  Empty cells  
                               default to 0. 0 specifies that voxels with this  
                               colour do not influence the image (split =  
                               background, true = black)  
                       hold  - resampling order for image (see spm_sample_vol) -  
                               default 1  
                       background - value when resampling outside image - default  
                               NaN  
                       linespec - string, applies only to contour map,  
                               e.g. 'w-' for white continuous lines  
                       contours - vector, applies to contour map only, defines  
                               values in image for which to show contours  
                               (see help contours)  
                       linewidth - scalar, width in points of contour lines  
             
            - transform - either - 4x4 transformation to apply to image slice position,  
                        relative to mm given by slicedef, before display  
                          or     - text string, one of axial, coronal, sagittal  
                                   These orientations assume the image is currently  
                                   (after its mat file has been applied) axially  
                                   oriented  
            - slicedef - 2x3 array specifying dimensions for slice images in mm  
                        where rows are x,and y of slice image, and cols are neg max dim,  
                        slice separation and pos max dim  
            - slices   - vector of slice positions in mm in z (of transformed image)  
            - figure    - figure handle for slice display figure  
                          The object used for the display is attached as 'UserData'  
                          to this figure  
            - figure_struct - stored figure parameters (in case figure dies and  
                          needs to be recreated)  
            - refreshf  - flag - if set or empty, refresh axis info for figure  
                        else assume this is OK  
            - clf       - flag, non zero -> clear figure before display.  Redundant  
                          if refreshf == 0  
            - resurrectf - if not zero, and figure (above) does not exist, will  
                          attempt to recreate figure with same area properties.  
                          Otherwise painting will give an error.  
            - userdata  - flag, non zero -> attaches object to figure when plotting,  
                          for use by callbacks (default is 1)  
            - area      - struct with fields  
                             position - bottom left, x size y size 1x4 vector of  
                                 area in which to display slices  
                             units    - one of  
                               inches,centimeters,normalized,points,{pixels}  
                             halign - one of left,{center},right  
                             valign - one of top,{middle},bottom  
            - xslices  - no of slices to display across figure (defaults to an optimum)  
            - cbar      - if empty, missing, no colourbar.  If an array of integers, then  
                        indexes img array, and makes colourbar for each cmap for  
                        that img.  Cbars specified in order of appearance L->R  
            - labels - struct can be:  
                             - empty (-> default numerical labels)  
                             - 'none' (string) (no labels)  
                             - or contain fields:  
                             colour - colour for label text  
                             size - font size in units normalized to slice axes  
                             format - if = cell array of strings =  
                             labels for each slice in Z.  If is string, specifies  
                             sprintf format string for labelling in distance of the  
                             origin (Xmm=0, Ymm=0) of each slice from plane containing  
                             the AC, in mm, in the space of the transformed image  
            - callback - callback string for button down on image panels. THe  
                         following examples assume that you have the 'userdata'  
                         field set to 1, giving you access to underlying object  
                         To print to the matlab window the equivalent position in  
                         mm of the position of a mouse click on one of the image  
                         slices, set callback to:  
                              'get_pos(get(gcf, ''UserData''))'  
                         To print the intensity values of the images at the clicked point:  
                              ['so_obj = get(gcf, ''UserData''); ' ...  
                               'point_vals(so_obj, get_pos(so_obj))']  
            - printstr - string for printing slice overlay figure window, e.g.  
                         'print -dpsc -painters -noui' (the default)  
            - printfile - name of file to print output to; default 'slices.ps'  
             
            Action string formats:  
            FORMAT [cmap warnstr] = slover('getcmap', cmapname)  
            Gets colormap named in cmapname string  
             
            FORMAT [mx mn] = slover('volmaxmin', vol)  
            Returns maximum and minimum finite values from vol struct 'vol'  
             
            FORMAT vol = slover('blobs2vol', XYZ, vals, mat)  
            returns (pseudo) vol struct for 3d blob volume specified  
            in matrices as above  
             
            FORMAT vol = slover('matrix2vol', mat3d, mat)  
            returns (pseudo) vol struct for 3d matrix  
            input matrices as above  
             
            FORMAT obj = slover('basic_ui' [,dispf])  
            Runs basic UI to fetch some parameters, does display, returns object  
            If optional dispf parameter = 0, suppresses display  
           __________________________________________________________________________  
            
              Documentation for slover  
                 doc slover  
            
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/slover.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        super().__init__()

    def add_blobs(self, *args, **kwargs):
        """
          Add SPM blobs to img no 'imgno', as specified in  
            FORMAT obj = add_blobs(obj, xyz, vals, mat, imgno)  
             
            Inputs  
            XYZ   - 3xN voxel coordinates of N blob values  
            vals  - N blob intensity values  
            mat   - 4x4 matrix specifying voxels -> mm  
            imgno - slice overlay img number to add to (defaults last in object)  
             
            Outputs  
            obj   - modified object  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/add_blobs.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("add_blobs", self._as_matlab_object(), *args, **kwargs)

    def add_matrix(self, *args, **kwargs):
        """
          Add 3d matrix image vol to slice overlay  
            FORMAT obj = add_matrix(obj, mat3d, mat, imgno)  
             
            Inputs  
            obj          - object  
            mat3d        - 3D matrix to add as img  
            mat          - optional 4x4 voxel->world translation  
            imgno        - optional img no to add to (defaults to last in object)  
             
            Outputs  
            obj          - modified object  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/add_matrix.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("add_matrix", self._as_matlab_object(), *args, **kwargs)

    def add_spm(self, *args, **kwargs):
        """
          Add SPM blobs as new img to object, split effect, 'hot' colormap  
            FORMAT obj = add_spm(obj)  
             
            SPM results are fetched from the workspace  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/add_spm.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("add_spm", self._as_matlab_object(), *args, **kwargs)

    def display(self, *args, **kwargs):
        """
          Display method for slice overlay object  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/display.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("display", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def fill_defaults(self, *args, **kwargs):
        """
          Check and fill fields in object  
            FORMAT obj = fill_defaults(obj)  
             
            Input  
            obj    - object to fill  
             
            Output  
            obj    - object filled  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/fill_defaults.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("fill_defaults", self._as_matlab_object(), *args, **kwargs)

    def get_pos(self, *args, **kwargs):
        """
          Return point location from last click, in mm  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/get_pos.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("get_pos", self._as_matlab_object(), *args, **kwargs)

    def paint(self, *args, **kwargs):
        """
          Method to display slice overlay  
            FORMAT obj = paint(obj, params)  
             
            Inputs  
            obj         - slice overlay object  
            params      - optional structure containing extra display parameters  
                          - refreshf - overrides refreshf in object  
                          - clf      - overrides clf in object  
                          - userdata - if 0, does not add object to userdata field  
                          (see below)  
             
            Outputs  
            obj         - which may have been filled with defaults  
             
            paint attaches the object used for painting to the 'UserData' field of  
            the figure handle, unless instructed not to with 0 in userdata flag  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/paint.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("paint", self._as_matlab_object(), *args, **kwargs)

    def point_vals(self, *args, **kwargs):
        """
          Return values from all the images at points given in XYZmm  
            FORMAT vals = point_vals(obj, XYZmm, holdlist)  
             
            (for the following,  I is number of images in object, N is the number  
            of points to resample from)  
            Input  
            obj         - object  
            XYZmm       - 3xN XYZ natrix of points (in mm)  
            holdlist    - optional 1xI vector of resample hold values  
             
            Outputs  
            vals        - IxN vector of values in images  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/point_vals.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("point_vals", self._as_matlab_object(), *args, **kwargs)

    def print_fig(self, *args, **kwargs):
        """
          Print slice overlay figure  
            FORMAT print_fig(obj, filename, printstr)  
             
            Input  
            obj       - object  
            filename  - optional filename to print to (obj.filename)  
            printstr  - optional string giving print command (obj.printstr)  
             
            Based on spm_figure print, and including fix from thence for ps  
            printing  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/print_fig.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("print_fig", self._as_matlab_object(), *args, **kwargs, nargout=0)

    def subsasgn(self, *args, **kwargs):
        """
          Method to overload . notation in assignments.  
            . assignment works directly on object fields  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/subsasgn.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsasgn", self._as_matlab_object(), *args, **kwargs)

    def subsref(self, *args, **kwargs):
        """
          Method to overload the . notation.  
            . reference works directly on object fields  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/subsref.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("subsref", self._as_matlab_object(), *args, **kwargs)

    def _mars_struct(self, *args, **kwargs):
        """
          Multifunction function for manipulating structures  
             
            To help the exposition a bit:  
            'fill' in a name, means that values empty or missing  
            in one structure are fetched from another  
             
            'merge' means simply that missing fields are added, with  
            values, from a second structure (but not filled if empty)  
             
            Each function needs to deal with the case of empty arguments  
             
            FORMAT c = mars_struct('fillafromb', a, b, fieldns, flags)  
            fills structure fields empty or missing in a from those present in b  
            a, b are structures  
            fieldns (optional) is cell array of field names to fill from in b  
            c is returned structure  
            Is recursive, will fill struct fields from struct fields  
            flags may contain 'f', which Force fills a from b (all non empty  
            fields in b overwrite those in a)  
            flags may also contain 'r', which Restricts fields to write from b, to  
            those that are already present in a  
             
            FORMAT [c, d] = mars_struct('split', a, b)  
            split structure a into two, according to fields in b  
            so that c becomes a structure which contains the fields  
            in a, that are also present in b, and d contains the fields  
            in a that are not present in b.  b can be a structure  
            or a cell array of fieldnames  
             
            FORMAT [d] = mars_struct('strip', a, b)  
            strips all fields present in b from those in a,  
            returning denuded structure as d. b can be a structure  
            or a cell array of fieldnames.  'strip' is just 'split'  
            but returning only the second argument  
             
            FORMAT c = mars_struct('merge', a, b)  
            merges structure a and b (fields present in b added to a)  
             
            FORMAT [c,d] = mars_struct('ffillsplit', a, b)  
            force fill, followed by split  
            All fields from a, that are also present in b, and not empty in b,  
            are replaced with the values in b; the result is returned as c  
            Any fields present in a, but not present in b, are returned in d  
             
            FORMAT c = mars_struct('ffillmerge', a, b)  
            force fill followed by merge  
            performs 'ffillsplit' on a and b, then merges a and b  
            All fields present in a or b are returned in c, but  
            any fields present in both, now have the value from b  
             
            FORMAT [c d] = mars_struct('splitmerge', a, b)  
            performs 'split' on a and b, creating c and d  
            then merges c with b.  
            d contains fields in a that were not present in b  
            c contains fields present in both, or just in b  
             
            FORMAT z = mars_struct('isthere', a, b [, c [, d ...])  
            returns 1 if field named in b is present in a  
            and field value is not empty.  
            The call is recursive if more than two arguments are passed  
            Thus with structure s = struct('one', struct('two', 3))  
            mars_struct('isthere', s, 'one', 'two') returns 1  
             
            FORMAT z = mars_struct('getifthere', a, b [, c [, d ...])  
            returns value of field named in b from a or [] if absent  
            Call is recursive, like 'isthere' above.  
             
            FORMAT strs = mars_struct('celldisp', a)  
            returns output like disp(a) as a cell array  
            Useful for printing text description of structure  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/private/mars_struct.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("mars_struct", self._as_matlab_object(), *args, **kwargs)

    def _pr_basic_ui(self, *args, **kwargs):
        """
          GUI to request parameters for slover routine  
            FORMAT obj = pr_basic_ui(imgs, dispf)  
             
            GUI requests choices while accepting many defaults  
             
            imgs  - string or cell array of image names to display  
                    (defaults to GUI select if no arguments passed)  
            dispf - optional flag: if set, displays overlay (default = 1)  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/private/pr_basic_ui.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("pr_basic_ui", self._as_matlab_object(), *args, **kwargs)

    def _pr_blobs2vol(self, *args, **kwargs):
        """
          Take XYZ matrix and values and return SPM matrix vol struct  
            FORMAT vol = pr_blobs2vol(xyz,vals,mat)  
             
            Inputs  
            xyz      - 3xN X Y Z coordinate matrix (in voxels)  
            vals     - 1xN values, one per coordinate  
            mat      - 4x4 voxel->world space transformation  
             
            Outputs  
            vol      - vol struct, with matrix data 'imgdata' field  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/private/pr_blobs2vol.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("pr_blobs2vol", self._as_matlab_object(), *args, **kwargs)

    def _pr_get_spm_results(self, *args, **kwargs):
        """
          Fetch SPM results and return as point list  
            FORMAT [XYZ, Z, M] = pr_get_spm_results  
             
            Outputs  
            XYZ    - XYZ point list in voxels (empty if not found)  
            Z      - values at points in XYZ  
            M      - 4x4 voxel -> world transformation matrix  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/private/pr_get_spm_results.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("pr_get_spm_results", self._as_matlab_object(), *args, **kwargs)

    def _pr_getcmap(self, *args, **kwargs):
        """
          Get colormap of name acmapname  
            FORMAT [cmap, warnstr] = pr_getcmap(acmapname)  
             
            Inputs  
            acmapname   - string.  Can be (in order of precedence)  
                          - matrix name in base workspace  
                          - colour name; one of 'red','green','blue','cyan',  
                            'magenta', 'yellow', 'black', 'white'  
                          - filename of .mat or .lut file.  If filename has no  
                            extension, assumes '.mat' extension  
             
            Outputs  
            cmap        - Nx3 colormap matrix  
                          or empty if fails  
            warnstr     - warning message if fails  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/private/pr_getcmap.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("pr_getcmap", self._as_matlab_object(), *args, **kwargs)

    def _pr_matrix2vol(self, *args, **kwargs):
        """
          Return (pseudo) vol struct for 3d matrix  
            FORMAT vol = pr_matrix2vol(mat3d,mat)  
             
            Inputs  
            mat3d   - 3D matrix  
            mat     - optional 4x4 voxel -> world transformation  
             
            Outputs  
            vol     - kind of SPM vol struct with matrix data added  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/private/pr_matrix2vol.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("pr_matrix2vol", self._as_matlab_object(), *args, **kwargs)

    def _pr_scaletocmap(self, *args, **kwargs):
        """
          Scale image data to colormap, returning colormap indices  
            FORMAT [img, badvals]=pr_scaletocmap(inpimg,mn,mx,cmap,lrn)  
             
            Inputs  
            inpimg     - matrix containing image to scale  
            mn         - image value that maps to first value of colormap  
            mx         - image value that maps to last value of colormap  
            cmap       - 3xN colormap  
            lrn        - 1x3 vector, giving colormap indices that should fill:  
                         - lrn(1) (L=Left) - values less than mn  
                         - lrn(2) (R=Right) - values greater than mx  
                         - lrn(3) (N=NaN) - NaN values  
                        If lrn value is 0, then colormap values are set to 1, and  
                        indices to these values are returned in badvals (below)  
             
            Output  
            img        - inpimg scaled between 1 and (size(cmap, 1))  
            badvals    - indices into inpimg containing values out of range, as  
                         specified by lrn vector above  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/private/pr_scaletocmap.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("pr_scaletocmap", self._as_matlab_object(), *args, **kwargs)

    def _pr_volmaxmin(self, *args, **kwargs):
        """
          Return max and min value in image volume  
            FORMAT [mx,mn] = pr_volmaxmin(vol)  
             
            Input  
            vol      - image name or vol struct  
             
            Outputs  
            mx       - maximum  
            mn       - minimum  
           __________________________________________________________________________  
          

        [Matlab code]( https://github.com/spm/spm/blob/main/@slover/private/pr_volmaxmin.m )

        Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
        """
        return Runtime.call("pr_volmaxmin", self._as_matlab_object(), *args, **kwargs)
