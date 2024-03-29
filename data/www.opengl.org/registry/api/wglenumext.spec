# Copyright (c) 1991-2005 Silicon Graphics, Inc. All Rights Reserved.
# Copyright (c) 2006-2010 The Khronos Group, Inc.
#
# This document is licensed under the SGI Free Software B License Version
# 2.0. For details, see http://oss.sgi.com/projects/FreeB/ .
#
# $Revision: 14504 $ on $Date: 2011-04-13 21:31:13 -0700 (Wed, 13 Apr 2011) $

# List of WGL enumerants for wglext.h header
#
# This is not the master WGL enumerant registry. Microsoft used
#   to maintain that, but given their limited interest in OpenGL, the
#   Khronos API Registrar maintains the registry in wglenum.spec.
#
# Unlike wglenum.spec, wglenumext.spec is
#   (1) In order by extension number
#   (2) Includes only WGL extensions.
#   (3) Has no 'Extensions' section, since enums are always
#	conditionally protected against multiple definition
#	by glextenum.pl.
#   (4) Is processed by glextenum.pl, which has evolved
#	from enum.pl - should merge back into one script.

# wglext.h version number - this should be automatically updated,
#   when changing either enum or template spec files.

passthru:
passthru: /* Header file version number */
passthru: /* wglext.h last updated 2011/04/13 */
passthru: /* Current version at http://www.opengl.org/registry/ */
passthru: #define WGL_WGLEXT_VERSION 23

###############################################################################
#
# ARB WGL extensions, in ARB extension order
#
###############################################################################

###############################################################################

# ARB Extension #4
WGL_ARB_buffer_region enum:
	WGL_FRONT_COLOR_BUFFER_BIT_ARB			= 0x00000001
	WGL_BACK_COLOR_BUFFER_BIT_ARB			= 0x00000002
	WGL_DEPTH_BUFFER_BIT_ARB			= 0x00000004
	WGL_STENCIL_BUFFER_BIT_ARB			= 0x00000008

###############################################################################

# ARB Extension #5
WGL_ARB_multisample enum:
	WGL_SAMPLE_BUFFERS_ARB				= 0x2041
	WGL_SAMPLES_ARB					= 0x2042

###############################################################################

# No new tokens
# ARB Extension #8
WGL_ARB_extensions_string enum:

###############################################################################

# ARB Extension #9
WGL_ARB_pixel_format enum:
	WGL_NUMBER_PIXEL_FORMATS_ARB			= 0x2000
	WGL_DRAW_TO_WINDOW_ARB				= 0x2001
	WGL_DRAW_TO_BITMAP_ARB				= 0x2002
	WGL_ACCELERATION_ARB				= 0x2003
	WGL_NEED_PALETTE_ARB				= 0x2004
	WGL_NEED_SYSTEM_PALETTE_ARB			= 0x2005
	WGL_SWAP_LAYER_BUFFERS_ARB			= 0x2006
	WGL_SWAP_METHOD_ARB				= 0x2007
	WGL_NUMBER_OVERLAYS_ARB				= 0x2008
	WGL_NUMBER_UNDERLAYS_ARB			= 0x2009
	WGL_TRANSPARENT_ARB				= 0x200A
	WGL_TRANSPARENT_RED_VALUE_ARB			= 0x2037
	WGL_TRANSPARENT_GREEN_VALUE_ARB			= 0x2038
	WGL_TRANSPARENT_BLUE_VALUE_ARB			= 0x2039
	WGL_TRANSPARENT_ALPHA_VALUE_ARB			= 0x203A
	WGL_TRANSPARENT_INDEX_VALUE_ARB			= 0x203B
	WGL_SHARE_DEPTH_ARB				= 0x200C
	WGL_SHARE_STENCIL_ARB				= 0x200D
	WGL_SHARE_ACCUM_ARB				= 0x200E
	WGL_SUPPORT_GDI_ARB				= 0x200F
	WGL_SUPPORT_OPENGL_ARB				= 0x2010
	WGL_DOUBLE_BUFFER_ARB				= 0x2011
	WGL_STEREO_ARB					= 0x2012
	WGL_PIXEL_TYPE_ARB				= 0x2013
	WGL_COLOR_BITS_ARB				= 0x2014
	WGL_RED_BITS_ARB				= 0x2015
	WGL_RED_SHIFT_ARB				= 0x2016
	WGL_GREEN_BITS_ARB				= 0x2017
	WGL_GREEN_SHIFT_ARB				= 0x2018
	WGL_BLUE_BITS_ARB				= 0x2019
	WGL_BLUE_SHIFT_ARB				= 0x201A
	WGL_ALPHA_BITS_ARB				= 0x201B
	WGL_ALPHA_SHIFT_ARB				= 0x201C
	WGL_ACCUM_BITS_ARB				= 0x201D
	WGL_ACCUM_RED_BITS_ARB				= 0x201E
	WGL_ACCUM_GREEN_BITS_ARB			= 0x201F
	WGL_ACCUM_BLUE_BITS_ARB				= 0x2020
	WGL_ACCUM_ALPHA_BITS_ARB			= 0x2021
	WGL_DEPTH_BITS_ARB				= 0x2022
	WGL_STENCIL_BITS_ARB				= 0x2023
	WGL_AUX_BUFFERS_ARB				= 0x2024
	WGL_NO_ACCELERATION_ARB				= 0x2025
	WGL_GENERIC_ACCELERATION_ARB			= 0x2026
	WGL_FULL_ACCELERATION_ARB			= 0x2027
	WGL_SWAP_EXCHANGE_ARB				= 0x2028
	WGL_SWAP_COPY_ARB				= 0x2029
	WGL_SWAP_UNDEFINED_ARB				= 0x202A
	WGL_TYPE_RGBA_ARB				= 0x202B
	WGL_TYPE_COLORINDEX_ARB				= 0x202C

###############################################################################

# ARB Extension #10
WGL_ARB_make_current_read enum:
	ERROR_INVALID_PIXEL_TYPE_ARB			= 0x2043
	ERROR_INCOMPATIBLE_DEVICE_CONTEXTS_ARB		= 0x2054

###############################################################################

# ARB Extension #11
WGL_ARB_pbuffer enum:
	WGL_DRAW_TO_PBUFFER_ARB				= 0x202D
	WGL_MAX_PBUFFER_PIXELS_ARB			= 0x202E
	WGL_MAX_PBUFFER_WIDTH_ARB			= 0x202F
	WGL_MAX_PBUFFER_HEIGHT_ARB			= 0x2030
	WGL_PBUFFER_LARGEST_ARB				= 0x2033
	WGL_PBUFFER_WIDTH_ARB				= 0x2034
	WGL_PBUFFER_HEIGHT_ARB				= 0x2035
	WGL_PBUFFER_LOST_ARB				= 0x2036
	WGL_TRANSPARENT_RED_VALUE_ARB			= 0x2037
	WGL_TRANSPARENT_GREEN_VALUE_ARB			= 0x2038
	WGL_TRANSPARENT_BLUE_VALUE_ARB			= 0x2039
	WGL_TRANSPARENT_ALPHA_VALUE_ARB			= 0x203A
	WGL_TRANSPARENT_INDEX_VALUE_ARB			= 0x203B

###############################################################################

# ARB Extension #20
WGL_ARB_render_texture enum:
	WGL_BIND_TO_TEXTURE_RGB_ARB			= 0x2070
	WGL_BIND_TO_TEXTURE_RGBA_ARB			= 0x2071
	WGL_TEXTURE_FORMAT_ARB				= 0x2072
	WGL_TEXTURE_TARGET_ARB				= 0x2073
	WGL_MIPMAP_TEXTURE_ARB				= 0x2074
	WGL_TEXTURE_RGB_ARB				= 0x2075
	WGL_TEXTURE_RGBA_ARB				= 0x2076
	WGL_NO_TEXTURE_ARB				= 0x2077
	WGL_TEXTURE_CUBE_MAP_ARB			= 0x2078
	WGL_TEXTURE_1D_ARB				= 0x2079
	WGL_TEXTURE_2D_ARB				= 0x207A
	WGL_MIPMAP_LEVEL_ARB				= 0x207B
	WGL_CUBE_MAP_FACE_ARB				= 0x207C
	WGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB		= 0x207D
	WGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB		= 0x207E
	WGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB		= 0x207F
	WGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB		= 0x2080
	WGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB		= 0x2081
	WGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB		= 0x2082
	WGL_FRONT_LEFT_ARB				= 0x2083
	WGL_FRONT_RIGHT_ARB				= 0x2084
	WGL_BACK_LEFT_ARB				= 0x2085
	WGL_BACK_RIGHT_ARB				= 0x2086
	WGL_AUX0_ARB					= 0x2087
	WGL_AUX1_ARB					= 0x2088
	WGL_AUX2_ARB					= 0x2089
	WGL_AUX3_ARB					= 0x208A
	WGL_AUX4_ARB					= 0x208B
	WGL_AUX5_ARB					= 0x208C
	WGL_AUX6_ARB					= 0x208D
	WGL_AUX7_ARB					= 0x208E
	WGL_AUX8_ARB					= 0x208F
	WGL_AUX9_ARB					= 0x2090

###############################################################################

# ARB Extension #39
WGL_ARB_pixel_format_float enum:
	WGL_TYPE_RGBA_FLOAT_ARB				= 0x21A0

###############################################################################

# ARB Extension #46
WGL_ARB_framebuffer_sRGB enum:
	WGL_FRAMEBUFFER_SRGB_CAPABLE_ARB		= 0x20A9

###############################################################################

# ARB Extension #55
WGL_ARB_create_context enum:
	WGL_CONTEXT_DEBUG_BIT_ARB			= 0x00000001
	WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB		= 0x00000002
	WGL_CONTEXT_MAJOR_VERSION_ARB			= 0x2091
	WGL_CONTEXT_MINOR_VERSION_ARB			= 0x2092
	WGL_CONTEXT_LAYER_PLANE_ARB			= 0x2093
	WGL_CONTEXT_FLAGS_ARB				= 0x2094
	ERROR_INVALID_VERSION_ARB			= 0x2095

###############################################################################

# ARB Extension #74
WGL_ARB_create_context_profile enum:
	WGL_CONTEXT_PROFILE_MASK_ARB			= 0x9126
	WGL_CONTEXT_CORE_PROFILE_BIT_ARB		= 0x00000001
	WGL_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB	= 0x00000002
	ERROR_INVALID_PROFILE_ARB			= 0x2096

###############################################################################

# ARB Extension #102
# All values are shared with GLX and GL
WGL_ARB_create_context_robustness enum:
	WGL_CONTEXT_ROBUST_ACCESS_BIT_ARB		= 0x00000004
	WGL_LOSE_CONTEXT_ON_RESET_ARB			= 0x8252
	WGL_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB	= 0x8256
	WGL_NO_RESET_NOTIFICATION_ARB			= 0x8261

###############################################################################
#
# non-ARB extensions follow, in registry order
#
###############################################################################

###############################################################################

# Extension #169
WGL_EXT_make_current_read enum:
	ERROR_INVALID_PIXEL_TYPE_EXT			= 0x2043

###############################################################################

# Extension #170
WGL_EXT_pixel_format enum:
	WGL_NUMBER_PIXEL_FORMATS_EXT			= 0x2000
	WGL_DRAW_TO_WINDOW_EXT				= 0x2001
	WGL_DRAW_TO_BITMAP_EXT				= 0x2002
	WGL_ACCELERATION_EXT				= 0x2003
	WGL_NEED_PALETTE_EXT				= 0x2004
	WGL_NEED_SYSTEM_PALETTE_EXT			= 0x2005
	WGL_SWAP_LAYER_BUFFERS_EXT			= 0x2006
	WGL_SWAP_METHOD_EXT				= 0x2007
	WGL_NUMBER_OVERLAYS_EXT				= 0x2008
	WGL_NUMBER_UNDERLAYS_EXT			= 0x2009
	WGL_TRANSPARENT_EXT				= 0x200A
	WGL_TRANSPARENT_VALUE_EXT			= 0x200B
	WGL_SHARE_DEPTH_EXT				= 0x200C
	WGL_SHARE_STENCIL_EXT				= 0x200D
	WGL_SHARE_ACCUM_EXT				= 0x200E
	WGL_SUPPORT_GDI_EXT				= 0x200F
	WGL_SUPPORT_OPENGL_EXT				= 0x2010
	WGL_DOUBLE_BUFFER_EXT				= 0x2011
	WGL_STEREO_EXT					= 0x2012
	WGL_PIXEL_TYPE_EXT				= 0x2013
	WGL_COLOR_BITS_EXT				= 0x2014
	WGL_RED_BITS_EXT				= 0x2015
	WGL_RED_SHIFT_EXT				= 0x2016
	WGL_GREEN_BITS_EXT				= 0x2017
	WGL_GREEN_SHIFT_EXT				= 0x2018
	WGL_BLUE_BITS_EXT				= 0x2019
	WGL_BLUE_SHIFT_EXT				= 0x201A
	WGL_ALPHA_BITS_EXT				= 0x201B
	WGL_ALPHA_SHIFT_EXT				= 0x201C
	WGL_ACCUM_BITS_EXT				= 0x201D
	WGL_ACCUM_RED_BITS_EXT				= 0x201E
	WGL_ACCUM_GREEN_BITS_EXT			= 0x201F
	WGL_ACCUM_BLUE_BITS_EXT				= 0x2020
	WGL_ACCUM_ALPHA_BITS_EXT			= 0x2021
	WGL_DEPTH_BITS_EXT				= 0x2022
	WGL_STENCIL_BITS_EXT				= 0x2023
	WGL_AUX_BUFFERS_EXT				= 0x2024
	WGL_NO_ACCELERATION_EXT				= 0x2025
	WGL_GENERIC_ACCELERATION_EXT			= 0x2026
	WGL_FULL_ACCELERATION_EXT			= 0x2027
	WGL_SWAP_EXCHANGE_EXT				= 0x2028
	WGL_SWAP_COPY_EXT				= 0x2029
	WGL_SWAP_UNDEFINED_EXT				= 0x202A
	WGL_TYPE_RGBA_EXT				= 0x202B
	WGL_TYPE_COLORINDEX_EXT				= 0x202C

###############################################################################

# Extension #171
WGL_EXT_pbuffer enum:
	WGL_DRAW_TO_PBUFFER_EXT				= 0x202D
	WGL_MAX_PBUFFER_PIXELS_EXT			= 0x202E
	WGL_MAX_PBUFFER_WIDTH_EXT			= 0x202F
	WGL_MAX_PBUFFER_HEIGHT_EXT			= 0x2030
	WGL_OPTIMAL_PBUFFER_WIDTH_EXT			= 0x2031
	WGL_OPTIMAL_PBUFFER_HEIGHT_EXT			= 0x2032
	WGL_PBUFFER_LARGEST_EXT				= 0x2033
	WGL_PBUFFER_WIDTH_EXT				= 0x2034
	WGL_PBUFFER_HEIGHT_EXT				= 0x2035

###############################################################################

# Extension #177
WGL_EXT_depth_float enum:
	WGL_DEPTH_FLOAT_EXT				= 0x2040

###############################################################################

# Extension #207
WGL_3DFX_multisample enum:
	WGL_SAMPLE_BUFFERS_3DFX				= 0x2060
	WGL_SAMPLES_3DFX				= 0x2061

###############################################################################

# Extension #209
WGL_EXT_multisample enum:
	WGL_SAMPLE_BUFFERS_EXT				= 0x2041
	WGL_SAMPLES_EXT					= 0x2042

###############################################################################

# Extension #250
WGL_I3D_digital_video_control enum:
	WGL_DIGITAL_VIDEO_CURSOR_ALPHA_FRAMEBUFFER_I3D	= 0x2050
	WGL_DIGITAL_VIDEO_CURSOR_ALPHA_VALUE_I3D	= 0x2051
	WGL_DIGITAL_VIDEO_CURSOR_INCLUDED_I3D		= 0x2052
	WGL_DIGITAL_VIDEO_GAMMA_CORRECTED_I3D		= 0x2053

###############################################################################

# Extension #251
WGL_I3D_gamma enum:
	WGL_GAMMA_TABLE_SIZE_I3D			= 0x204E
	WGL_GAMMA_EXCLUDE_DESKTOP_I3D			= 0x204F

###############################################################################

# Extension #252
WGL_I3D_genlock enum:
	WGL_GENLOCK_SOURCE_MULTIVIEW_I3D		= 0x2044
	WGL_GENLOCK_SOURCE_EXTENAL_SYNC_I3D		= 0x2045
	WGL_GENLOCK_SOURCE_EXTENAL_FIELD_I3D		= 0x2046
	WGL_GENLOCK_SOURCE_EXTENAL_TTL_I3D		= 0x2047
	WGL_GENLOCK_SOURCE_DIGITAL_SYNC_I3D		= 0x2048
	WGL_GENLOCK_SOURCE_DIGITAL_FIELD_I3D		= 0x2049
	WGL_GENLOCK_SOURCE_EDGE_FALLING_I3D		= 0x204A
	WGL_GENLOCK_SOURCE_EDGE_RISING_I3D		= 0x204B
	WGL_GENLOCK_SOURCE_EDGE_BOTH_I3D		= 0x204C

###############################################################################

# Extension #253
WGL_I3D_image_buffer enum:
	WGL_IMAGE_BUFFER_MIN_ACCESS_I3D			= 0x00000001
	WGL_IMAGE_BUFFER_LOCK_I3D			= 0x00000002

###############################################################################

# No new tokens
# Extension #254
WGL_I3D_swap_frame_lock enum:

###############################################################################

# Extension #263
WGL_NV_render_depth_texture enum:
	WGL_BIND_TO_TEXTURE_DEPTH_NV			= 0x20A3
	WGL_BIND_TO_TEXTURE_RECTANGLE_DEPTH_NV		= 0x20A4
	WGL_DEPTH_TEXTURE_FORMAT_NV			= 0x20A5
	WGL_TEXTURE_DEPTH_COMPONENT_NV			= 0x20A6
	WGL_DEPTH_COMPONENT_NV				= 0x20A7

###############################################################################

# Extension #264
WGL_NV_render_texture_rectangle enum:
	WGL_BIND_TO_TEXTURE_RECTANGLE_RGB_NV		= 0x20A0
	WGL_BIND_TO_TEXTURE_RECTANGLE_RGBA_NV		= 0x20A1
	WGL_TEXTURE_RECTANGLE_NV			= 0x20A2

###############################################################################

# Extension #278
WGL_ATI_pixel_format_float enum:
	WGL_TYPE_RGBA_FLOAT_ATI				= 0x21A0

###############################################################################

# Extension #281
WGL_NV_float_buffer enum:
	WGL_FLOAT_COMPONENTS_NV				= 0x20B0
	WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_R_NV	= 0x20B1
	WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RG_NV	= 0x20B2
	WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGB_NV	= 0x20B3
	WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGBA_NV	= 0x20B4
	WGL_TEXTURE_FLOAT_R_NV				= 0x20B5
	WGL_TEXTURE_FLOAT_RG_NV				= 0x20B6
	WGL_TEXTURE_FLOAT_RGB_NV			= 0x20B7
	WGL_TEXTURE_FLOAT_RGBA_NV			= 0x20B8

###############################################################################

# Extension #313
WGL_3DL_stereo_control enum:
	WGL_STEREO_EMITTER_ENABLE_3DL			= 0x2055
	WGL_STEREO_EMITTER_DISABLE_3DL			= 0x2056
	WGL_STEREO_POLARITY_NORMAL_3DL			= 0x2057
	WGL_STEREO_POLARITY_INVERT_3DL			= 0x2058

###############################################################################

# Extension #328
WGL_EXT_pixel_format_packed_float enum:
	WGL_TYPE_RGBA_UNSIGNED_FLOAT_EXT		= 0x20A8

###############################################################################

# Extension #337
WGL_EXT_framebuffer_sRGB enum:
	WGL_FRAMEBUFFER_SRGB_CAPABLE_EXT		= 0x20A9

###############################################################################

# Extension #347
WGL_NV_present_video enum:
	WGL_NUM_VIDEO_SLOTS_NV				= 0x20F0

###############################################################################

# Extension #349
WGL_NV_video_out enum:
	WGL_BIND_TO_VIDEO_RGB_NV			= 0x20C0
	WGL_BIND_TO_VIDEO_RGBA_NV			= 0x20C1
	WGL_BIND_TO_VIDEO_RGB_AND_DEPTH_NV		= 0x20C2
	WGL_VIDEO_OUT_COLOR_NV				= 0x20C3
	WGL_VIDEO_OUT_ALPHA_NV				= 0x20C4
	WGL_VIDEO_OUT_DEPTH_NV				= 0x20C5
	WGL_VIDEO_OUT_COLOR_AND_ALPHA_NV		= 0x20C6
	WGL_VIDEO_OUT_COLOR_AND_DEPTH_NV		= 0x20C7
	WGL_VIDEO_OUT_FRAME				= 0x20C8
	WGL_VIDEO_OUT_FIELD_1				= 0x20C9
	WGL_VIDEO_OUT_FIELD_2				= 0x20CA
	WGL_VIDEO_OUT_STACKED_FIELDS_1_2		= 0x20CB
	WGL_VIDEO_OUT_STACKED_FIELDS_2_1		= 0x20CC

###############################################################################

# No new tokens
# Extension #351
WGL_NV_swap_group enum:

###############################################################################

# Extension #355
WGL_NV_gpu_affinity enum:
	WGL_ERROR_INCOMPATIBLE_AFFINITY_MASKS_NV	= 0x20D0
	WGL_ERROR_MISSING_AFFINITY_MASK_NV		= 0x20D1

###############################################################################

# Extension #361
WGL_AMD_gpu_association enum:
	WGL_GPU_VENDOR_AMD				= 0x1F00
	WGL_GPU_RENDERER_STRING_AMD			= 0x1F01
	WGL_GPU_OPENGL_VERSION_STRING_AMD		= 0x1F02
	WGL_GPU_FASTEST_TARGET_GPUS_AMD			= 0x21A2
	WGL_GPU_RAM_AMD					= 0x21A3
	WGL_GPU_CLOCK_AMD				= 0x21A4
	WGL_GPU_NUM_PIPES_AMD				= 0x21A5
	WGL_GPU_NUM_SIMD_AMD				= 0x21A6
	WGL_GPU_NUM_RB_AMD				= 0x21A7
	WGL_GPU_NUM_SPI_AMD				= 0x21A8

###############################################################################

# Extension #374
WGL_NV_video_capture enum:
	WGL_UNIQUE_ID_NV				= 0x20CE
	WGL_NUM_VIDEO_CAPTURE_SLOTS_NV			= 0x20CF

###############################################################################

# No new tokens
# Extension #376
WGL_NV_copy_image enum:

###############################################################################

# Extension #393
WGL_NV_multisample_coverage enum:
	WGL_COVERAGE_SAMPLES_NV				= 0x2042
	WGL_COLOR_SAMPLES_NV				= 0x20B9

###############################################################################

# Extension #400
# All values are shared with GLX and GL
WGL_EXT_create_context_es2_profile enum:
	WGL_CONTEXT_ES2_PROFILE_BIT_EXT			= 0x00000004

###############################################################################

# Extension #407
# Not a bitfield but not from an assigned range, either
WGL_NV_DX_interop enum:
	WGL_ACCESS_READ_ONLY_NV				= 0x00000000
	WGL_ACCESS_READ_WRITE_NV			= 0x00000001
	WGL_ACCESS_WRITE_DISCARD_NV			= 0x00000002

