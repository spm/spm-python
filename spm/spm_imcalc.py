from spm.__wrapper__ import Runtime


def spm_imcalc(*args, **kwargs):
    """
      Perform algebraic functions on images  
        FORMAT Vo = spm_imcalc(Vi, Vo, f [,flags [,extra_vars...]])  
        Vi            - struct array (from spm_vol) of images to work on  
                        or a char array of input image filenames  
        Vo (input)    - struct array (from spm_vol) containing information on  
                        output image  
                        ( pinfo field is computed for the resultant image data, )  
                        ( and can be omitted from Vo on input.  See spm_vol     )  
                        or output image filename  
        f             - MATLAB expression to be evaluated  
        flags         - cell array of flags: {dmtx,mask,interp,dtype,descrip}  
                        or structure with these fieldnames  
             dmtx     - read images into data matrix?  
                        [defaults (missing or empty) to 0 - no]  
             mask     - implicit zero mask?  
                        [defaults (missing or empty) to 0 - no]  
                         ( negative value implies NaNs should be zeroed )  
             interp   - interpolation hold (see spm_slice_vol)  
                        [defaults (missing or empty) to 0 - nearest neighbour]  
             dtype    - data type for output image (see spm_type)  
                        [defaults (missing or empty) to 4 - 16 bit signed shorts]  
             descrip  - content of the 'descrip' field of the NIfTI header  
                        [defaults (missing or empty) to 'spm - algebra']  
        extra_vars... - additional variables which can be used in expression  
         
        Vo (output)   - spm_vol structure of output image volume after  
                        modifications for writing  
       __________________________________________________________________________  
         
        spm_imcalc performs user-specified algebraic manipulations on a set of  
        images, with the result being written out as an image.   
        The images specified in Vi, are referred to as i1, i2, i3,...  in the  
        expression to be evaluated, unless the dmtx flag is setm in which  
        case the images are read into a data matrix X, with images in rows.  
         
        Computation is plane by plane, so in data-matrix mode, X is a NxK  
        matrix, where N is the number of input images [prod(size(Vi))], and K  
        is the number of voxels per plane [prod(Vi(1).dim(1:2))].  
         
        For data types without a representation of NaN, implicit zero masking  
        assumes that all zero voxels are to be treated as missing, and treats  
        them as NaN. NaN's are written as zero, for data types without a  
        representation of NaN.  
         
        With images of different sizes and orientations, the size and orientation  
        of the reference image is used. Reference is the first image, if  
        Vo (input) is a filename, otherwise reference is Vo (input). A  
        warning is given in this situation. Images are sampled into this  
        orientation using the interpolation specified by the interp parameter.  
       __________________________________________________________________________  
         
        Example expressions (f):  
         
           i)  Mean of six images (select six images)  
               f = '(i1+i2+i3+i4+i5+i6)/6'  
          ii)  Make a binary mask image at threshold of 100  
               f = 'i1>100'  
          iii) Make a mask from one image and apply to another  
               f = '(i1>100).*i2'  
               (here the first image is used to make the mask, which is applied  
                to the second image - note the '.*' operator)  
          iv)  Sum of n images  
               f = 'i1 + i2 + i3 + i4 + i5 + ...'  
          v)   Sum of n images (when reading data into data-matrix)  
               f = 'sum(X)'  
          vi)  Mean of n images (when reading data into data-matrix)  
               f = 'mean(X)'  
       __________________________________________________________________________  
         
        Furthermore, additional variables for use in the computation can be  
        passed at the end of the argument list. These should be referred to by  
        the names of the arguments passed in the expression to be evaluated.   
        E.g. if c is a 1xn vector of weights, then for n images, using the (dmtx)  
        data-matrix version, the weighted sum can be computed using:  
              Vi = spm_vol(spm_select(inf,'image'));  
              Vo = 'output.nii'  
              Q  = spm_imcalc(Vi,Vo,'c*X',{1},c)  
        Here we've pre-specified the expression and passed the vector c as an  
        additional variable (you'll be prompted to select the n images).  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_imcalc.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_imcalc", *args, **kwargs)
